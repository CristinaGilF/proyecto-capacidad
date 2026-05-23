import streamlit as st
import plotly.express as px

#--- Tabla del equipo ---

def mostrar_datos_equipo (df):
    st.subheader("Datos del equipo")
    st.dataframe(df)

#--- Horas totales ---

def mostrar_horas_totales (df):
    horas_totales = df["Horas disponibles"].sum()
    st.metric("Horas totales disponibles del equipo", horas_totales)


def mostrar_horas_por_rol (df):
    st.subheader ("Horas disponibles por rol")
    horas_por_rol = df.groupby("Rol")["Horas disponibles"].sum()
    st.bar_chart(horas_por_rol)
    
    st.subheader ("Distribución de horas por rol (Gráfico de tarta)")
    fig = px.pie(
            horas_por_rol.reset_index(),
            names = "Rol",
            values = "Horas disponibles",
            color = "Rol",
            title= "Distribución de horas por rol"
    )
    
    st.plotly_chart(fig, use_container_width=True)        
    st.subheader ("Detalle por rol")
    st.dataframe(horas_por_rol.reset_index())

def mostrar_visualizacion():
    if "df_equipo" not in st.session_state:
        st.warning("Primero debes cargar los datos del equipo.")
        return
    df = st.session_state["df_equipo"]
    mostrar_datos_equipo(df)
    mostrar_horas_totales(df)
    mostrar_horas_por_rol(df)

