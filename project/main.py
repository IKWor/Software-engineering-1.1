import streamlit as st
import torch
import torchaudio

def main():
    st.title("Приложение для озвучки текста")

    # Форма для загрузки файла
    uploaded_file = st.file_uploader("Загрузка текстового файла", type="txt")

    if uploaded_file is not None:
        try:
            # Read the contents of the uploaded file
            text = uploaded_file.read().decode("utf-8")
            st.write(text)

            # Озвучиваем текст
            voice = voicer(text)

            # Convert torch tensor to WAV format
            wav_file = torchaudio.transforms.Resample(orig_freq=48000, new_freq=24000)(voice.unsqueeze(0))
            wav_file = wav_file.squeeze(0).numpy()

            # Форма для проигрывания звука
            if st.button("Проиграть звук"):
                st.audio(wav_file, format='audio/wav', sample_rate=24000)

        except Exception as e:
            st.error(f"An error occurred: {e}")

def voicer(text):
    language = 'ru'
    model_id = 'v4_ru'
    device = torch.device('cpu')

    sample_rate = 48000
    speaker = 'xenia'

    model, example_text = torch.hub.load(
        repo_or_dir='snakers4/silero-models',
        model='silero_tts',
        language=language,
        speaker=model_id
        )
    model.to(device)

    audio = model.apply_tts(text, speaker=speaker, sample_rate=sample_rate)
    return audio

if __name__ == "__main__":
    main()
