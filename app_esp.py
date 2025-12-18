#Comentar cada linea para que sirve
import streamlit as st
from textblob import TextBlob
from deep_translator import GoogleTranslator

# Configuración
st.set_page_config(page_title="NLP en Español", page_icon="🇪🇸")

st.title("🇪🇸 Analizador de Sentimientos")
st.markdown("Escribe una frase en **español** y la IA detectará el tono.")

# Input en Español
texto_espanol = st.text_area("Ingresa tu texto aquí:", "¡Estoy muy feliz de aprender inteligencia artificial!")

if st.button("Analizar Sentimiento"):
    if texto_espanol:
        try:
            # --- PASO 1: TRADUCCIÓN ---
            # Traducimos de español (es) a inglés (en)
            traductor = GoogleTranslator(source='es', target='en')
            texto_ingles = traductor.translate(texto_espanol)
            
            # Mostramos la traducción (útil para entender qué "ve" la IA)
            st.caption(f"⚙️ Procesado internamente como: *'{texto_ingles}'*")

            # --- PASO 2: ANÁLISIS (Usando el texto en inglés) ---
            blob = TextBlob(texto_ingles)
            polaridad = blob.sentiment.polarity
            subjetividad = blob.sentiment.subjectivity
            
            # --- PASO 3: MOSTRAR RESULTADOS ---
            st.write("---")
            st.subheader("Resultados:")
            
            # Coloreamos según la polaridad
            if polaridad > 0.1:
                st.success(f"😊 Positivo (Score: {polaridad:.2f})")
            elif polaridad < -0.1:
                st.error(f"😠 Negativo (Score: {polaridad:.2f})")
            else:
                st.warning(f"😐 Neutral (Score: {polaridad:.2f})")

            st.info(f"🧐 Subjetividad: {subjetividad:.2f} ({(subjetividad * 100):.0f}% opinión)")

        except Exception as e:
            st.error(f"Hubo un error con la traducción: {e}")
            
    else:
        st.warning("Escribe algo para analizar.")