import streamlit as st

def mostrar_inicio():
    st.title("Prototipo de capacidad del equipo")
    st.write(
        "Este prototipo permite analizar la capacidad del equipo, visualizar la carga actual "
        "y simular el impacto de nuevos proyectos."
    )
    st.write(
        "Comienza cargando los datos del equipo y los proyectos en curso desde la sección 'Cargar Datos'. "
        "Después, navega por el menú para explorar las distintas funcionalidades."
    )
    st.markdown("---")