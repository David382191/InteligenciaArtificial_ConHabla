import streamlit as st
from textblob import TextBlob

# Configuración básica de la página
st.set_page_config(page_title="NLP Básico", page_icon="🧠")

# Título y descripción
st.title("🧠 Analizador de Sentimientos")
st.markdown("Escribe una frase en **inglés** (TextBlob funciona mejor en inglés) y la IA detectará el tono.")

# Área de texto para el input del usuario
texto_usuario = st.text_area("Ingresa tu texto aquí:", "I love programming in Python, it makes me feel powerful!")

# Botón para analizar
if st.button("Analizar Sentimiento"):
    if texto_usuario:
        # --- LÓGICA DE NLP ---
        # Creamos el objeto TextBlob
        blob = TextBlob(texto_usuario)
        
        # Obtenemos la polaridad (-1 a 1) y subjetividad (0 a 1)
        polaridad = blob.sentiment.polarity
        subjetividad = blob.sentiment.subjectivity
        
        # --- MOSTRAR RESULTADOS ---
        st.write("---")
        
        # 1. Determinamos si es Positivo, Negativo o Neutral
        st.subheader("Resultados:")
        if polaridad > 0:
            st.success(f"😊 Sentimiento Positivo (Score: {polaridad:.2f})")
        elif polaridad < 0:
            st.error(f"😠 Sentimiento Negativo (Score: {polaridad:.2f})")
        else:
            st.warning(f"😐 Sentimiento Neutral (Score: {polaridad:.2f})")

        # 2. Explicación de Subjetividad
        st.info(f"🧐 Subjetividad: {subjetividad:.2f} (0 = Hecho objetivo, 1 = Opinión personal)")
        
        # 3. Datos crudos (Opcional, para aprender)
        with st.expander("Ver detalles técnicos"):
            st.json(blob.sentiment)
            
    else:
        st.warning("Por favor, escribe algo para analizar.")

# Nota al pie
st.write("---")
st.caption("Hecho con ❤️ usando Streamlit y TextBlob")