import streamlit as st
import pyttsx3
from io import BytesIO
from streamlit_lottie import st_lottie
import json

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
lottie_download = load_lottiefile("fun.json")

def text_to_speech(text, gender, speed):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if gender == 'Male':
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', speed)
    engine.setProperty('volume', 0.9)

    audio_file = BytesIO()
    engine.save_to_file(text, 'output.mp3')
    engine.runAndWait()

    with open('output.mp3', 'rb') as f:
        audio_file.write(f.read())
    audio_file.seek(0)
    return audio_file

st.set_page_config(page_title="text2speech", page_icon="🙊", layout="centered", initial_sidebar_state="auto")
st.image("title.png", use_column_width=True)
st_lottie(lottie_download, height=300, key="download_animation")

text = st.text_area("Enter the text you want to convert to speech", "")
gender = st.radio("Select Voice", ('Male', 'Female'))
speed = st.slider("Speed", min_value=50, max_value=300, value=150)
file_name = st.text_input("Enter the name for the audio file (without extension)", "")

if st.button("Convert"):
    if text:
        audio_file = text_to_speech(text, gender, speed)
        if not file_name:
            file_name = "output"
        full_file_name = f"{file_name}.mp3"
        st.success("Conversion completed!")

        st.audio(audio_file, format='audio/mp3')

        st.download_button(
            label="Download Audio",
            data=audio_file,
            file_name=full_file_name,
            mime="audio/mp3"
        )
    elif not text:
        st.error("Please enter some text to convert")

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
