import streamlit as st
import plotly.express as px
from interfaz.visualizacion.estilos_tablas import tabla

#--- Funciones auxiliares ---

#--- Información del equipo ---
def mostrar_datos_equipo (df):
    tabla(df)

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
    st.write('Distribución, capacidad y disponibilidad por rol')
    st.markdown("---")

    if "df_equipo" not in st.session_state:
        st.warning("Primero debes cargar los datos del equipo.")
        return
    
    df = st.session_state["df_equipo"]
    
    #--- Paleta de colores ---
    colores = ["#7BC6A4","#3A6EA5","#C3CCD6","#A8DaDC"]

    #--- Bloque 1: Datos del equipo + Métrica ---
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Datos del equipo")
        mostrar_datos_equipo(df)
    
    with col2:
        st.subheader("Métricas generales")
        mostrar_horas_totales(df)

    st.markdown("---")

    #--- Bloque 2: Gráfico de barras ---
    st.header("Horas disponibles por rol")
    horas_por_rol = df.groupby("Rol")["Horas disponibles"].sum()
    
    fig_bar = px.bar(
        horas_por_rol.reset_index(),
        x="Rol",
        y="Horas disponibles",
        color="Rol",
        color_discrete_sequence=colores,
    )
    
    fig_bar.update_traces(
        texttemplate="%{y} h",
        textposition="outside"
    )

    fig_bar.update_layout(
        hoverlabel=dict(
            bgcolor="white",
            font_size = 16,
            font_color="black"
        )
    )    
    fig_bar.update_layout(
        margin=dict(t=40, b=40)
    )

    fig_bar.update_layout(
        showlegend=False,
        font=dict(size=18),
        xaxis=dict(tickfont=dict(size=16)),
        yaxis=dict(tickfont=dict(size=16)),
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown("---")

    #--- Bloque 3: Tarta + Tabla detalle ---
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Distribución por rol")

        fig = px.pie(
            horas_por_rol.reset_index(),
            names = "Rol",
            values = "Horas disponibles",
            color = "Rol",
            color_discrete_sequence=colores
        )

        fig.update_layout(
            hoverlabel=dict(
                bgcolor="white",
                font_size=16,
                font_color="black"
            )
        )

        fig.update_traces(
            hovertemplate="<b>%{label}</b><br>%{value} h<br>%{percent}"
        )
        
        fig.update_traces(
            textinfo="label+percent",
            textfont_size=16
        )
        
        fig.update_layout(
            showlegend=False,
            font=dict(size=18)
        )
        st.plotly_chart(fig, use_container_width=True)
        
    
    with col4:
        st.subheader ("Detalle por rol")
        detalle = horas_por_rol.reset_index().rename(
            columns={"Horas disponibles": "Horas disponibles (h)"}
        )
        tabla(detalle)