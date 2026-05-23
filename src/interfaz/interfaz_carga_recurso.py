import streamlit as st
from logica.calculo_capacidad import carga_proyecto

def mostrar_carga_recurso():
    st.header("Carga de trabajo por recurso")

    #--- Se valida si estan los ficheros cargados.
    if "df_equipo" not in st.session_state or "df_proyectos" not in st.session_state:
        st.warning("Primero debes cargar los datos del equipo y los proyectos en curso.")
        return

    df_equipo = st.session_state["df_equipo"]
    df_proyectos = st.session_state["df_proyectos"]

    #--- Selector de recurso
    recursos = df_equipo["Miembro del equipo"].unique()
    recurso_sel =st.selectbox("Selecciona un recurso: ",recursos)

    #--- Datos del recurso
    df_recurso = df_equipo[df_equipo["Miembro del equipo"] == recurso_sel]
    horas_disp = df_recurso["Horas disponibles"].iloc[0]

    #--- Se filtran los proyectos asignados al recurso seleccionado
    df_asignados = df_proyectos[df_proyectos["Recurso"] == recurso_sel]

    st.subheader ("Proyectos asignados")
    st.dataframe(df_asignados)

    #--- Calcular la carga total del recurso
    if df_asignados.empty:
        carga_total = 0
    else:
        carga_total = df_asignados.apply(carga_proyecto, axis=1).sum()

    ocupacion = (carga_total/horas_disp * 100) if horas_disp > 0 else 0
    disponibilidad = 100 - ocupacion

    #--- Métricas
    st.subheader("Resumen del recurso")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Horas disponibles",f"{horas_disp} h")
    col2.metric("Carga asignada",f"{carga_total} h")
    col3.metric("Ocupación",f"{ocupacion:.1f} %")
    col4.metric("Disponibilidad",f"{disponibilidad:.1f} %")

    #--- Alertas
    if ocupacion > 100:
        st.error("⚠ El recurso está sobrecargado.")
    elif ocupacion > 80:
        st.warning("⚠ El recurso está cerca de su límite de capacidad.")
    else:
        st.success("✔ El recurso está dentro de su capacidad.")