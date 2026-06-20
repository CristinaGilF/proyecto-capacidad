import streamlit as st
from interfaz.visualizacion.estilos_tablas import tabla

from logica.calculo_capacidad import(
    capacidad_por_rol,
    carga_total_por_rol,
    resumen_capacidad
)

def mostrar_capacidad():
    st.title("Capacidad disponible del equipo")

    st.markdown("---")

    #---Se valida que haya datos cargados
    if "df_equipo" not in st.session_state or "df_proyectos" not in st.session_state:
        st.warning("Primero debes cargar los datos del equipo y los proyectos en curso.")
        return

    #---Se recuperan los dataframes cargados previamente
    df_equipo = st.session_state.df_equipo
    df_proyectos = st.session_state.df_proyectos
    
    #---Cálculos
    df_cap_rol = capacidad_por_rol(df_equipo)
    carga_roles = carga_total_por_rol(df_proyectos)
    df_resumen = resumen_capacidad(df_cap_rol, carga_roles)

    #---Tabla principal
    st.subheader("Capacidad y carga por rol")
    tabla(df_resumen)

    st.markdown("<div style='margin-top:-10px'></div>", unsafe_allow_html=True)

    #---Resumen global
    cap_global = df_resumen["Capacidad (h)"].sum()
    carga_global = df_resumen["Carga (h)"].sum()
    ocup_global = (carga_global/cap_global) * 100 if cap_global > 0 else 0
    disp_global = 100 - ocup_global

    st.markdown("---")
    
    st.subheader("Resumen global del equipo")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Capacidad total",f"{cap_global:.1f} h")
    with col2:
        st.write("Carga total",f"{carga_global:.1f} h")

    col3, col4 = st.columns(2)
    with col3:
        st.write("Ocupación global",f"{ocup_global:.1f} %")
    with col4:
        st.write("Disponibilidad global",f"{disp_global:.1f} %")

    st.markdown("<div style='margin-bottom:20px;'></div>", unsafe_allow_html=True)