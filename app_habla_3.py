import streamlit as st
import speech_recognition as sr
from textblob import TextBlob
import tempfile

st.set_page_config(page_title="NLP con Micrófono", page_icon="🎙️")
st.title("🎙️ Analizador de Sentimientos por Voz")

st.markdown("Presiona **Grabar**, habla y analiza el sentimiento.")

# 🎤 Micrófono nativo de Streamlit
audio_file = st.audio_input("Grabar audio")

if audio_file is not None:
    st.success("Audio capturado")

    recognizer = sr.Recognizer()

    # Guardar audio temporal
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_file.getbuffer())
        wav_path = tmp.name

    try:
        with sr.AudioFile(wav_path) as source:
            audio_data = recognizer.record(source)

        texto = recognizer.recognize_google(audio_data, language="es-EC")

        st.success("Texto reconocido:")
        st.write(texto)

        blob = TextBlob(texto)
        polaridad = blob.sentiment.polarity

        if polaridad > 0:
            st.success("😊 Sentimiento Positivo")
        elif polaridad < 0:
            st.error("😠 Sentimiento Negativo")
        else:
            st.warning("😐 Sentimiento Neutral")

    except sr.UnknownValueError:
        st.error("No se pudo entender el audio.")
    except sr.RequestError as e:
        st.error(f"Error del servicio: {e}")
