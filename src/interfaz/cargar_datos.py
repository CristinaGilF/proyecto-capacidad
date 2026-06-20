import streamlit as st

from interfaz.visualizacion.esquemas import ESQUEMAS
from datos.validaciones import validar_fichero, limpiar_filas_vacias
from datos.cargar_datos import carga_datos
from interfaz.visualizacion.estilos_tablas import tabla

def mostrar_cargar_datos():
    st.title("Cargar Datos")
    st.write(
        "En esta sección puedes cargar los datos del equipo y los proyectos en curso. "
        "Estos datos son necesarios para realizar los cálculos de capacidad y las simulaciones posteriores."
    )
    st.markdown("---")
    
    #--- Datos del equipo ---
    st.subheader("Carga de datos del equipo (CSV o Excel).")

    uploaded_file =st.file_uploader(
        "Sube el archivo con la información de tu equipo", 
        type=["csv","xlsx"]
    )
    
    if uploaded_file is not None:
        df = carga_datos(uploaded_file)
        df = limpiar_filas_vacias(df)

        esquema = ESQUEMAS["equipo"]
        ok, mensaje = validar_fichero(df, esquema["columnas"],esquema["tipos"])

        if not ok:
            st.error(mensaje)        
        else:
            st.success("Datos cargados correctamente")
            tabla(df)
            st.session_state["df_equipo"] = df
    
    st.markdown ("---")
    
    #--- Datos del proyectos en curso ---
    st.subheader("Carga de proyectos en curso (CSV o Excel)")

    uploaded_proyectos = st.file_uploader(
        "Sube el archivo con los proyectos en curso",
        type=["csv","xlsx"],
        key="proyectos"
    )
    
    if uploaded_proyectos is not None:
        df_proyectos = carga_datos(uploaded_proyectos)
        df_proyectos = limpiar_filas_vacias(df_proyectos)

        esquema = ESQUEMAS["proyectos"]
        ok, mensaje = validar_fichero(df_proyectos, esquema["columnas"])

        if not ok:
            st.error(mensaje)
        else:
            st.success("Proyectos cargados correctamente")
            tabla(df_proyectos)
            st.session_state["df_proyectos"] = df_proyectos
    
    # --- Mensaje final cuando todo está listo ---
    if "df_equipo" in st.session_state and "df_proyectos" in st.session_state:
        st.markdown ("---")
        st.success("Datos cargados correctamente. Ya puedes navegar al resto de secciones del menú.")
    