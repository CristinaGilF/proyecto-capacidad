import streamlit as st

def mostrar_inicio():
    st.title("Prototipo de capacidad del equipo")
    st.subheader("Análisis, visualización y simulación de carga")

    st.markdown("---")   

    st.markdown("<div style='margin-top: 20px'></div>", unsafe_allow_html=True)

    st.markdown(
        """
        Este prototipo permite:
        
        - Analizar la **capacidad del equipo**.
        - Visualizar la **carga actual**.
        - Simular el impacto de **nuevos proyectos**.
        
        Para comenzar:

        1. Ve a la sección **'Cargar de datos'**
        2. Sube la información del equipo y los proyectos en curso
        3. Naveha por el menú para explorar las funcionalidades
        """
    )
    
    st.markdown("---")