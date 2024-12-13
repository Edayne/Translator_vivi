from record_voices import record_audio
from speech_2_text import transcribe_audio
from fr_2_en import translate
from text_2_speech import text_to_speech

record_audio(duration=5)
text = transcribe_audio("./output.wav")
text_traduit = translate(text)
text_traduit = text_traduit[0].get('translation_text')
print(f"Text en français : {text} \n Text en anglais : {text_traduit}")
text_to_speech(text_traduit)

