import streamlit as st
import speech_recognition as sr
from textblob import TextBlob
import tempfile

st.set_page_config(page_title="NLP con Micrófono", page_icon="🎙️")
st.title("🎙️ Analizador de Sentimientos por Voz")

st.markdown("Graba una frase **corta y clara** (3–6 segundos).")

audio_file = st.audio_input("🎤 Grabar audio")

if audio_file is not None:
    st.success("Audio grabado")

    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = True

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_file.getbuffer())
        audio_path = tmp.name

    try:
        with sr.AudioFile(audio_path) as source:
            # 🔥 AJUSTE CLAVE
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio_data = recognizer.record(source)

        # ⚠️ Idioma correcto
        texto = recognizer.recognize_google(
            audio_data,
            language="es-EC"
        )

        st.success("Texto reconocido:")
        st.write(texto)

        # --- SENTIMIENTO ---
        blob = TextBlob(texto)
        polaridad = blob.sentiment.polarity

        if polaridad > 0:
            st.success("😊 Sentimiento Positivo")
        elif polaridad < 0:
            st.error("😠 Sentimiento Negativo")
        else:
            st.warning("😐 Sentimiento Neutral")

    except sr.UnknownValueError:
        st.error("❌ No se pudo entender el audio. Intenta hablar más claro y más cerca.")
    except sr.RequestError as e:
        st.error(f"⚠️ Error del servicio: {e}")
