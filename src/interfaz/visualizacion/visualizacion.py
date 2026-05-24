import streamlit as st
import plotly.express as px

#--- Funciones auxiliares ---

#--- Información del equipo ---
def mostrar_datos_equipo (df):
    st.dataframe(df)

#--- Horas totales ---
def mostrar_horas_totales (df):
    horas_totales = df["Horas disponibles"].sum()
    st.metric("Horas totales disponibles del equipo", horas_totales)

#--- Horas por rol ---
def mostrar_horas_por_rol (df):
    st.subheader ("Horas disponibles por rol")
    horas_por_rol = df.groupby("Rol")["Horas disponibles"].sum()
    st.bar_chart(horas_por_rol)
    
#--- Pantalla principal ---
def mostrar_visualizacion():
    st.title("Visualización general del equipo")
    st.write(
        "En esta sección puedes ver una visión general del equipo, incluyendo la distribución de roles "
        "y las horas disponibles por cada uno."
    )
    st.markdown("---")

    if "df_equipo" not in st.session_state:
        st.warning("Primero debes cargar los datos del equipo.")
        return
    
    df = st.session_state["df_equipo"]

    #--- Bloque 1: Datos del equipo + Métrica ---
    col1, col2 = st.columns([2, 1])
    with col1:
        st.header("Datos del equipo")
        mostrar_datos_equipo(df)
        st.markdown("<div style='margin-bottom:40px;'></div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<h2 style='text-align: center;'>Métricas generales</h2>", unsafe_allow_html=True)

        sub1, sub2 = st.columns([1, 2])
        with sub2:
            mostrar_horas_totales(df)

    st.markdown("---")

    #--- Bloque 2: Gráfico de barras ---
    st.header("Horas disponibles por rol")
    horas_por_rol = df.groupby("Rol")["Horas disponibles"].sum()
    st.bar_chart(horas_por_rol, height=250)
    st.markdown("---")

    #--- Bloque 3: Tarta + Tabla detalle ---
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Distribución por rol (tarta)")

        fig = px.pie(
            horas_por_rol.reset_index(),
            names = "Rol",
            values = "Horas disponibles",
            color = "Rol",
            title= "Distribución de horas por rol"
        )
        
        fig.update_layout(
            margin=dict(l=10, r=10, t=30, b=10)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col4:
        st.subheader ("Detalle por rol")
        st.dataframe(horas_por_rol.reset_index())