# import necessary libraries for the title-page rendering
import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(layout='wide')

# --- Annimation block ---
lottie_url = "https://lottie.host/9c23b545-e68c-4331-be05-cf380fdca662/DzM7njoiGD.json"

# Function to load Lottie animation data
def load_lottie_url(url):
    response = requests.get(url)
    return None if response.status_code != 200 else response.json()

# Load Lottie animation data
lottie_data = load_lottie_url(lottie_url)


# --- Introduction part ---
st.write("---")
with st.container():
    left_columns, right_columns = st.columns((1, 1))
    with left_columns:
        st.header("Project:")
        st.write("The purpose of the project is to show how to deploy pre-trained model with Streamlit library.")
        st.header("Model:")
        st.write("In the project Silero Text-To-Speech is used as a pre-trained model. To find out more, please follow the link below:")
        st.write("[Silero >](https://pytorch.org/hub/snakers4_silero-models_tts/)")
        st.header("Description:")
        st.write("Users are prompted to insert any text with russian language in a form, and get a voiced audio in reply.")
 
    with right_columns:
        # Display Lottie animation
        if lottie_data is not None:
            st_lottie(lottie_data, height=400, key='coding')
        else:
            st.error("Failed to load Lottie animation.")

st.write("---")


# --- Model creation block ---
# import necessary libraries for the pre-trained model
import torch
import soundfile as sf
from pydub import AudioSegment

# Download and save the model
language = 'ru'
model_id = 'v4_ru'
device = torch.device('cpu')

model, example_text = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model='silero_tts',
                                     language=language,
                                     speaker=model_id)
model.to(device)

#Generate audio
sample_rate = 24000
speaker = 'random'


st.title("Sound Generator App")


# Form to get user input with customized styling
example_text = st.text_area("Enter text:", '',
                          key="user_input",
                          help="Type your text here.",
                          height=10)
# Apply black text color using HTML styling
st.markdown("""
    <style>
        textarea {
            color: black !important;
            font-size: 26px !important;
            caret-color: black !important;
        }
    </style>
""", unsafe_allow_html=True)

# Button to generate and play sound
if st.button("Generate and Play Sound"):
    # Generate audio based on user input
    audio = model.apply_tts(text=example_text,
                        speaker=speaker,
                        sample_rate=sample_rate)
    
    # Save the audio to a file
    sf.write("temp.wav", audio, sample_rate)
    
    # Load the saved audio file and play
    st.audio("temp.wav", format="audio/wav")

    # Clear the text area after sound generation
    example_text = ''