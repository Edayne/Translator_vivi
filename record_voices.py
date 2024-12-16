import sounddevice as sd
import wave
import numpy as np
from pynput import keyboard 
def record_audio(filename='output.wav', sample_rate=44100):
    """
    Record audio using the microphone, starting and stopping with the space bar.
    Save the recording to a WAV file.
    """
    print("Appuyez sur 'Espace' pour commencer l'enregistrement et sur 'Espace' à nouveau pour arrêter.")

    recording = False
    audio_frames = []

    def on_press(key):
        nonlocal recording, audio_frames
        try:
            if key == keyboard.Key.space and not recording:
                print("Enregistrement démarré...")
                recording = True
                audio_frames = []  # Réinitialise les données audio

            elif key == keyboard.Key.space and recording:
                print("Enregistrement terminé.")
                recording = False
                return False  # Arrête l'écoute du clavier
        except AttributeError:
            pass

    def record_audio():
        nonlocal recording, audio_frames
        while recording:
            # Enregistrement audio en continu
            audio_data = sd.rec(int(sample_rate / 10), samplerate=sample_rate, channels=2, dtype='int16')
            sd.wait()  # Attends la fin de l'enregistrement du buffer
            audio_frames.append(audio_data)

    with keyboard.Listener(on_press=on_press) as listener:
        while listener.running:
            record_audio()

    # Combine les frames audio en un seul tableau numpy
    full_audio = np.concatenate(audio_frames, axis=0)

    # Sauvegarde des données audio dans un fichier WAV
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(2)  # Stéréo
        wf.setsampwidth(2)  # 16 bits PCM
        wf.setframerate(sample_rate)
        wf.writeframes(full_audio.tobytes())

    print(f"Audio sauvegardé sous {filename}")

if __name__ == "__main__":
    record_audio(filename='output.wav')