import streamlit as st
from textblob import TextBlob
import streamlit.components.v1 as components

st.set_page_config(page_title="NLP con Micrófono", page_icon="🎙️")
st.title("🎙️ Analizador de Sentimientos por Voz")

st.markdown("Presiona el botón y **habla**. El navegador convertirá tu voz en texto.")

# --- HTML + JS con micrófono ---
html_code = """
<!DOCTYPE html>
<html>
<body>
<button onclick="startRecognition()">🎤 Hablar</button>
<p id="output"></p>

<script>
let recognition;

function startRecognition() {
    window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    recognition = new SpeechRecognition();
    recognition.lang = 'es-EC';
    recognition.interimResults = false;

    recognition.start();

    recognition.onresult = function(event) {
        const text = event.results[0][0].transcript;
        document.getElementById("output").innerText = text;
        window.parent.postMessage(text, "*");
    };

    recognition.onerror = function(event) {
        alert("Error de reconocimiento: " + event.error);
    };
}
</script>
</body>
</html>
"""

texto = components.html(html_code, height=150)

# --- Analizar texto ---
if texto:
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
