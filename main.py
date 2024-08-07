import streamlit as st
import pyttsx3
from io import BytesIO
from streamlit_lottie import st_lottie
import json



def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
lottie_download = load_lottiefile("fun.json")

def text_to_speech(text, gender, speed, file_name):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    if gender == 'Male':
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)

    engine.setProperty('rate', speed)
    engine.setProperty('volume', 0.9)
    engine.save_to_file(text, file_name)
    engine.runAndWait()

st.set_page_config(page_title="text2speech", page_icon = "🙊", layout = "centered", initial_sidebar_state = "auto")
# st.title("Text to Speech Converter")
st.image("title.png", use_column_width=True)
st_lottie(lottie_download, height=300, key="download_animation")

text = st.text_area("Enter the text you want to convert to speech", "")
gender = st.radio("Select Voice", ('Male', 'Female'))
speed = st.slider("Speed", min_value=50, max_value=300, value=150)
file_name = st.text_input("Enter the name for the audio file (without extension)", "")

if st.button("Convert"):
    if text and file_name:
        full_file_name = f"{file_name}.mp3"
        text_to_speech(text, gender, speed, full_file_name)
        st.success("Conversion completed!")

        audio_file = open(full_file_name, 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')

        st.download_button(
            label="Download Audio",
            data=audio_bytes,
            file_name=full_file_name,
            mime="audio/mp3"
        )
    elif not text:
        st.error("Please enter some text to convert")
    elif not file_name:
        st.error("Please enter a name for the audio file")

if st.button("About Creator🧐", key="about_creator_button"):
    with st.expander("kalkeesh jami"):
        st.image("mepic.jpg", use_column_width=True)
        st.write("""
        Hello! I'm KALKEESH JAMI #AKA Kalki, a passionate developer exploring the world of AI and programming.
        
        - I love building applications that make life easier.
        - I'm good at Python and data analysis.
        - Don't misunderstand me as a nerd; I'm socially adept too! 😄
        - Thank you for checking out my app!
        
        Do check out my [LinkedIn](https://www.linkedin.com/in/kalkeesh-jami-42891b260/) and [GitHub](https://github.com/kalkeesh/).
        """)