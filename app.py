
import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Portafolio", page_icon="💼", layout="centered")

st.title("💼 Portafolio de Equipo")
st.write("Presentamos a nuestro equipo de desarrolladores:")

# --- Persona 1 ---
st.subheader("Daniel Alvarez")
st.write("**Carrera:** Ingeniería en sistemas y computación")
st.write("**Proyectos:**")
st.markdown("- [Quiz Game](https://github.com/analopez/inventario)")

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
st.markdown("- [Aplicación de Tareas con Django](https://github.com/carlosruiz/tareas)")

st.divider()

st.caption("© 2025 Todos los derechos reservados.")

