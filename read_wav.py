import sounddevice as sd
import wave

def play_audio(filename):
    """
    Play a WAV audio file using sounddevice.

    Parameters:
        filename (str): Path to the WAV file to be played.
    """
    # Open the WAV file
    with wave.open(filename, 'rb') as wf:
        # Extract audio parameters
        sample_rate = wf.getframerate()
        channels = wf.getnchannels()
        dtype = 'int16'

        # Read all frames from the file
        audio_data = wf.readframes(wf.getnframes())

        # Convert audio data to NumPy array
        import numpy as np
        audio_array = np.frombuffer(audio_data, dtype=dtype)

        # Reshape audio array if stereo
        if channels > 1:
            audio_array = audio_array.reshape(-1, channels)

        # Play audio
        print("Playing audio...")
        sd.play(audio_array, samplerate=sample_rate)
        sd.wait()  # Wait for playback to finish
        print("Playback complete.")

# Example usage
if __name__ == "__main__":
    play_audio("output.wav")
