import pandas as pd

def limpiar_filas_vacias(df):
    return df.dropna(how="all")

def validar_fichero(df, columnas_obligatorias, tipos=None):
    if df.empty or len(df.dropna(how="all")) ==0:
        return False, "El fichero está vacío o no contiene datos válidos"
    
    if not all(col in df.columns for col in columnas_obligatorias):
        return False,(
            "El fichero no tiene las columnas necesarias: " + ", ".join(columnas_obligatorias)
        )
    
    if tipos:
        for columna, tipo in tipos.items():
            if tipo == "numerico" and not pd.api.types.is_numeric_dtype(df[columna]):
                return False, f"La columna '{columna}' debe ser numérica."
    
    return True, "OK"