import streamlit as st
from textblob import TextBlob
from openai import OpenAI
import tempfile

# Cliente OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="NLP con Micrófono", page_icon="🎙️")
st.title("🎙️ Analizador de Sentimientos por Voz")

st.markdown("Habla una frase corta y clara (3–6 segundos).")

# 🎤 MICRÓFONO
audio = st.audio_input("Grabar audio")

if audio:
    st.success("Audio grabado correctamente")

    # Guardar audio temporal
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio.read())
        audio_path = f.name

    # 🔊 VOZ → TEXTO (WHISPER)
    with open(audio_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )

    texto = transcript.text
    st.subheader("📝 Texto reconocido:")
    st.write(texto)

    # 🧠 SENTIMIENTO (TU MODELO ORIGINAL)
    blob = TextBlob(texto)
    polaridad = blob.sentiment.polarity
    subjetividad = blob.sentiment.subjectivity

    st.write("---")
    if polaridad > 0:
        st.success(f"😊 Sentimiento Positivo ({polaridad:.2f})")
    elif polaridad < 0:
        st.error(f"😠 Sentimiento Negativo ({polaridad:.2f})")
    else:
        st.warning(f"😐 Sentimiento Neutral ({polaridad:.2f})")

    st.info(f"🧐 Subjetividad: {subjetividad:.2f}")
