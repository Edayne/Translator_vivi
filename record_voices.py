import sounddevice as sd
import wave

def record_audio(filename='output.wav', duration=5, sample_rate=44100):
    """
    Record audio from the microphone and save it to a WAV file.

    Parameters:
        filename (str): The name of the output WAV file.
        duration (int): Duration of the recording in seconds.
        sample_rate (int): Sampling rate in Hz (default is 44100).
    """
    print("Recording...")
    # Record audio data
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')
    sd.wait()  # Wait until the recording is finished
    print("Recording complete.")
    
    # Save the audio data to a WAV file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(2)  # Stereo
        wf.setsampwidth(2)  # 16-bit PCM
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())
    
    print(f"Audio saved as {filename}")

# Example usage
if __name__ == "__main__":
    record_audio(filename='output.wav', duration=5)
