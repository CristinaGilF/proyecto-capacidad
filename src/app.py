import streamlit as st

# --- Importación de pantallas ---

from interfaz.inicio import mostrar_inicio
from interfaz.cargar_datos import mostrar_cargar_datos
from interfaz.visualizacion.visualizacion import mostrar_visualizacion
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
    padding-top: 1rem !important;
}
    section[data-testid="stSidebar"].css-1d391kg{
        padding-top: 1rem !important;
    }
</style>
"""
st.markdown(hide_anchor_links, unsafe_allow_html=True)

#--- Menú lateral ---

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

#--- Selecciones

if option == "Inicio":
    mostrar_inicio()

elif option == "Cargar Datos":
    mostrar_cargar_datos()

elif option == "Visualización del equipo":
    mostrar_visualizacion()

elif option == "Capacidad del equipo":
    mostrar_capacidad()

elif option == "Carga por recurso":
    mostrar_carga_recurso()
    
elif option == "Simulación de capacidad":
    mostrar_simulacion()