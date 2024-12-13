from transformers import pipeline
from datasets import load_dataset
import torch
import soundfile as sf
from read_wav import play_audio

def text_to_speech(text:str):
    synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts")
    embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
    speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

    speech = synthesiser(text, forward_params={"speaker_embeddings": speaker_embedding})

    sf.write("speech.wav", speech["audio"], samplerate=speech["sampling_rate"])

    play_audio("./speech.wav")