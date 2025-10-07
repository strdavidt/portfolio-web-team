
import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Portafolio", page_icon="💼", layout="centered")

st.title("💼 Portafolio de Equipo")
st.write("Presentamos a nuestro equipo de desarrolladores:")

# --- Persona 1 ---
st.subheader("Daniel Alvarez")
st.write("**Carrera:** Ingeniería en sistemas y computación")
st.write("**Proyectos:**")
st.markdown("- [Quiz Game](https://calculardistancia-da.streamlit.app/")

st.divider()

# --- Persona 2 ---
st.subheader("David Merino")
st.write("**Carrera:** Ingeniería en sistemas y computación")
st.write("**Proyectos:**")
st.markdown("- [Weather App](https://weather-app-dm-f73zftwcwfams9xfn2hcjs.streamlit.app/)")


st.divider()

# --- Persona 3 ---
st.subheader("Kevin Benitez")
st.write("**Carrera:** Ingeniería en sistemas y computación")
st.write("**Proyectos:**")
st.markdown("- [Juego de adivinar](https://adivina-el-clima-ae4qyah2psguwwqp2nazvr.streamlit.app/)")

st.divider()

st.caption("© 2025 Todos los derechos reservados.")

