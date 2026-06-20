import streamlit as st

#--- Importación de pantallas ---

from interfaz.inicio import mostrar_inicio
from interfaz.cargar_datos import mostrar_cargar_datos
from interfaz.visualizacion.visualizacion import mostrar_visualizacion
from interfaz.interfaz_capacidad import mostrar_capacidad
from interfaz.interfaz_carga_recurso import mostrar_carga_recurso
from interfaz.interfaz_simulacion import mostrar_simulacion

#--- Configuración básica ---

st.set_page_config(page_title="Prototipo de Capacidad", page_icon="📊",layout="wide")

#--- Estilos globales ---

global_styles= """
<style>

    /* Ocultar iconos de anclaje */
    a.anchor-link {
        display: none !important;
    }

    .block-container a {
        display: none !important;
    }

    /* Fondo general */
    .main {
        background-color: #F7F9FC;
    }

    /* Sidebar */
        section[data-testid="stSidebar"]
        {
            background-color: #E1ECF7 !important;
            padding-top: 1rem !important;
        }

    /* Títulos */
    h1{
        font-size: 2.2rem !important;
        color: #333333 !important;
        font-weight: 700 !important;   
    } 
    
    h2{
        font-size: 1.8rem !important;
        color: #7BC6A4 !important;
        font-weight: 650 !important;       
    }
    
    h3 {
        font-size: 1.5rem !important;
        color: #5F6C7B !important;
        font-weight: 600 !important;   
    }

    hr {
        border: 1px solid #7BC6A4 !important;
    }

    ul li::marker{
        color: #7BC6A4 !important;
    }
    
    /* Texto general*/
    .block-container p,
    .block-container li,
    .block-container span,
    .stMarkdown p,
    .stMarkdown li,
    .stMarkdown span {
        font-size: 1.25rem !important;
        line-height: 1.7 !important;
        color: #333333 !important;
    }

    /* Ajuste de texto en widgets */
    .stTextInput label,
    .stSelectbox label,
    .stNumerInput label,
    .stTextInput input,
    .stSelectbox div,
    .stNumberInput input {
        font-size: 1.15rem !important;
    }
    
    /* Tamaño de letra para tablas */
    table {
        font-size: 1.15rem !important;
    }

    thead th {
        font-size: 1.2rem !important;
        font-weight: 600 !important;
    }

    tbody td {
        font-size: 1.15rem !important;
    }

</style>
"""
st.markdown(global_styles, unsafe_allow_html=True)

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