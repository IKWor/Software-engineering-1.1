from transformers import pipeline

en_fr_translator = pipeline("Helsinki-NLP/opus-mt-en-ru")
en_fr_translator("How old are you?")
