from transformers import pipeline

def translate(text_fr: str) -> str:
    translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")
    result = translator(text_fr)
    return result