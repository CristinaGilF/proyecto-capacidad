
import pandas as pd

# -- "Carga de Datos":

def carga_datos(uploaded_file):
    file_name = uploaded_file.name.lower()
    
    if file_name.endswith(".csv"):        
        df = pd.read_csv(uploaded_file,sep=";",encoding="latin-1")
    elif file_name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
    
    return df


