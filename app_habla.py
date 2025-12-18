import streamlit as st
from textblob import TextBlob
import speech_recognition as sr

# Configuración
st.set_page_config(page_title="NLP con Voz", page_icon="🎙️")
st.title("🎙️ Analizador de Sentimientos por Voz")

st.markdown("Habla en **inglés** y el sistema analizará tu sentimiento.")

# Inicializamos reconocedor
recognizer = sr.Recognizer()

# Botón para grabar
if st.button("🎤 Grabar Audio"):
    with st.spinner("Escuchando..."):
        try:
            with sr.Microphone(device_index=20) as source:

                recognizer.adjust_for_ambient_noise(source, duration=1.5)

            audio = recognizer.listen(source, timeout=5)

            # Convertimos voz a texto
            texto = recognizer.recognize_google(audio, language="es-ES")


            st.success("Texto reconocido:")
            st.write(texto)

            # --- NLP ---
            blob = TextBlob(texto)
            polaridad = blob.sentiment.polarity
            subjetividad = blob.sentiment.subjectivity

            st.subheader("Resultados")

            if polaridad > 0:
                st.success(f"😊 Positivo ({polaridad:.2f})")
            elif polaridad < 0:
                st.error(f"😠 Negativo ({polaridad:.2f})")
            else:
                st.warning(f"😐 Neutral ({polaridad:.2f})")

            st.info(f"🧐 Subjetividad: {subjetividad:.2f}")

        except sr.WaitTimeoutError:
            st.error("No se detectó audio.")
        except sr.UnknownValueError:
            st.error("No se pudo entender el audio.")
        except sr.RequestError:
            st.error("Error con el servicio de reconocimiento.")

