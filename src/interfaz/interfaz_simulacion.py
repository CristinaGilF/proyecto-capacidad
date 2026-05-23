import streamlit as st
from logica.calculo_simulacion import simular_proyecto
from logica.modelo_capacidad import(
    df_duraciones_fases,
    df_roles_necesarios,
    df_dedicacion_fases
)

def mostrar_simulacion():
    st.header("Simulación de impacto de un nuevo proyecto")

    #--- Validación de datos cargados por el usuario
    if "df_equipo" not in st.session_state or "df_proyectos" not in st.session_state:
        st.warning("Primero deben estar cargados todos los datos necesarios (equipo, proyectos en curso y parámetros del modelo.)")
        return
    
    #--- Datos cargados por el usuario
    df_equipo = st.session_state["df_equipo"]
    df_proyectos = st.session_state["df_proyectos"]

    #--- Selector de tipología de proyecto
    
    tipologias = df_duraciones_fases.index.unique()
    tipologia_sel = st.selectbox("Selecciona la tipología del nuevo proyecto: ",tipologias)

    #--- Botón de simulación
    if st.button ("Simular impacto"):
        df_resultado = simular_proyecto(
            tipologia_sel,
            df_equipo,
            df_proyectos,
            df_duraciones_fases,
            df_roles_necesarios,
            df_dedicacion_fases
        )

        st.subheader("Resultado de la simulación")
        st.dataframe(df_resultado)

        #--- Alertas de sonrecarga
        sobrecargados = df_resultado[df_resultado["Ocupación (%)"] > 100]
        casi_sobrecargados = df_resultado[(df_resultado["Ocupación (%)"] > 80) & (df_resultado["Ocupación (%)"] <= 100)]

        if not sobrecargados.empty:
            st.error ("⚠ Algunos roles quedarían sobrecargados con este nuevo proyecto.")
            st.dataframe(sobrecargados)
        
        elif not casi_sobrecargados.empty:
            st.warning ("⚠ Algunos roles quedarían cerca del límite de capacidad.")
            st.dataframe(casi_sobrecargados)
        
        else:
            st.success ("✔ El equipo puede asumir este nuevo proyecto sin problemas.")