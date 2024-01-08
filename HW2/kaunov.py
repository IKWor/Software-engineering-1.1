import io
import streamlit as st
from transformers import pipeline
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ru")

st.title('Translation App')

# поле для ввода текста
text_input = st.text_area("Введите текст для перевода:", value="", height=200)
if text_input:
   result = pipe(text_input)[0]['translation_text'] # перевод текста
   st.write(result) # вывод перевода
else:
   st.warning("Please enter text to translate.")
