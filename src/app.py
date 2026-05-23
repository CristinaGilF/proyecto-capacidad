import streamlit as st

from interfaz.visualizacion.esquemas import ESQUEMAS
from datos.validaciones import validar_fichero, limpiar_filas_vacias
from datos.cargar_datos import carga_datos
from interfaz.visualizacion.visualizacion import mostrar_visualizacion
from logica.calculo_capacidad import(
    capacidad_por_rol,
    carga_total_por_rol,
    resumen_capacidad
)
from interfaz.interfaz_capacidad import mostrar_capacidad
from interfaz.interfaz_carga_recurso import mostrar_carga_recurso
from interfaz.interfaz_simulacion import mostrar_simulacion

#--- Configuración básica ---

st.set_page_config(page_title="Prototipo de Capacidad", layout="wide")

#Oculta los iconos de enlace en los encabezados
hide_anchor_links= """
<style>
.block-container a {
    display: none !important;
}
</style>
"""
st.markdown(hide_anchor_links, unsafe_allow_html=True)

#--- Barra lateral ---

st.sidebar.title ("MENÚ")
option = st.sidebar.radio(
    "Selecciona una sección: ",
    ["Inicio",
     "Cargar Datos",
     "Visualización del equipo",
     "Capacidad del equipo",
     "Carga por recurso", 
     "Simulación de capacidad"]
)

#--- Sección: Inicio ---

if option == "Inicio":
    st.title("Prototipo de capacidad del equipo")
    st.write("Este prototipo permite analizar la capacidad del equipo, visualizar la carga actual y simular el impacto de nuevos proyectos.")
    st.write("Comienza cargando los datos del equipo y los proyectos en curso desde la sección 'Cargar Datos'. Después, navega por el menú para explorar las distintas funcionalidades.")
    st.markdown("---")

#--- Sección: Cargar Datos ---

elif option == "Cargar Datos":
    st.title("Cargar Datos")
    st.write("En esta sección puedes cargar los datos del equipo y los proyectos en curso. Estos datos son necesarios para realizar los cálculos de capacidad y las simulaciones posteriores.")
    st.markdown("---")
    
    #--- Datos del equipo ---
    st.subheader("Carga de datos del equipo (CSV o Excel).")

    uploaded_file =st.file_uploader("Sube el archivo con la información de tu equipo", type=["csv","xlsx"])
    if uploaded_file is not None:
        df = carga_datos(uploaded_file)
        df = limpiar_filas_vacias(df)

        esquema = ESQUEMAS["equipo"]
        ok, mensaje = validar_fichero(df, esquema["columnas"],esquema["tipos"])

        if not ok:
            st.error(mensaje)        
        else:
            st.success("Datos cargados correctamente")
            st.dataframe(df)
            st.session_state["df_equipo"] = df

    #--- Datos del proyectos en curso ---

    st.subheader("Carga de proyectos en curso (CSV o Excel)")

    uploaded_proyectos = st.file_uploader("Sube el archivo con los proyectos en curso",type=["csv","xlsx"],key="proyectos")
    if uploaded_proyectos is not None:
        df_proyectos = carga_datos(uploaded_proyectos)
        df_proyectos = limpiar_filas_vacias(df_proyectos)

        esquema = ESQUEMAS["proyectos"]
        ok, mensaje = validar_fichero(df_proyectos, esquema["columnas"])

        if not ok:
            st.error(mensaje)
        else:
            st.success("Proyectos cargados correctamente")
            st.dataframe(df_proyectos)
            st.session_state["df_proyectos"] = df_proyectos
    
    # --- Mensaje final cuando todo está listo ---
    if "df_equipo" in st.session_state and "df_proyectos" in st.session_state:
        st.markdown ("---")
        st.success("Datos cargados correctamente. Ya puedes navegar al resto de secciones del menú.")


#--- Sección: Visualización general del estado del equipo ---

elif option == "Visualización del equipo":
    st.title("Visualización general del equipo")
    st.write("En esta sección puedes ver una visión general del equipo, incluyendo la distribución de roles y las horas disponibles por cada uno.")
    st.markdown("---")
    mostrar_visualizacion()

elif option == "Capacidad del equipo":
    mostrar_capacidad()

elif option == "Carga por recurso":
    mostrar_carga_recurso()
    
elif option == "Simulación de proyecto":
    mostrar_simulacion()