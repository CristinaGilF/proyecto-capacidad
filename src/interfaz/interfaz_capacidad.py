import streamlit as st
from logica.calculo_capacidad import(
    capacidad_por_rol,
    carga_total_por_rol,
    resumen_capacidad
)

def mostrar_capacidad():
    st.header("Capacidad disponible del equipo")

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
    st.dataframe(df_resumen)

    def color_ocupacion(col):
        return[
            "background-color: #b6f2b6" if val < 50 else #verde suave
            "background-color: #fff3b0" if val < 80 else #amarillo suave
            "background-color: #f7b2b0" #rojo suave
            for val in col
        ]
    
    st.subheader("Capacidad y carga por rol")

    styled_df = df_resumen.style.apply(
        color_ocupacion, subset=["% Ocupación"]
    )

    st.dataframe(styled_df)

    #---Resumen global
    cap_global = df_resumen["Capacidad (h)"].sum()
    carga_global = df_resumen["Carga (h)"].sum()
    ocup_global = (carga_global/cap_global) * 100 if cap_global > 0 else 0
    disp_global = 100 - ocup_global

    st.subheader("Resumen global del equipo")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Capacidad total",f"{cap_global:.1f} h")
    col2.metric("Carga total",f"{carga_global:.1f} h")
    col3.metric("Ocupación global",f"{ocup_global:.1f} %")
    col4.metric("Disponibilidad global",f"{disp_global:.1f} %")