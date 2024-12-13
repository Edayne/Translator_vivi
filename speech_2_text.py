from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torch
import librosa

# Load the processor and model
model_name = "openai/whisper-small"
processor = WhisperProcessor.from_pretrained(model_name)
model = WhisperForConditionalGeneration.from_pretrained(model_name)


def preprocess_audio(file_path, target_sampling_rate=16000):
    """
    Load and preprocess the audio file for Whisper model.
    
    Args:
        file_path (str): Path to the audio file.
        target_sampling_rate (int): Desired sampling rate (default 16 kHz for Whisper).
    
    Returns:
        np.ndarray: Resampled audio array.
    """
    audio, sr = librosa.load(file_path, sr=target_sampling_rate)  # Load and resample
    return audio

def transcribe_audio(file_path: str) -> str:
    # Preprocess the audio
    audio = preprocess_audio(file_path)

    # Tokenize the audio input
    inputs = processor(audio, sampling_rate=16000, return_tensors="pt")

    # Perform transcription
    with torch.no_grad():
        predicted_ids = model.generate(inputs["input_features"])

    # Decode the transcription
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
    return transcription
