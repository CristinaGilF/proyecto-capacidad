import pandas as pd
from logica.modelo_capacidad import df_tipologias, df_dedicacion_fases

HORAS_POR_SEMANA = 40

#-----------------------------------------
#--- HORAS POR FASE (Semanas -> horas) ---
#-----------------------------------------

def horas_fase(tipologia, fase):
    fila = df_tipologias[df_tipologias["Tipologia"] == tipologia]
    if fila.empty:
        return 0
    semanas = fila.iloc[0][fase]
    return semanas * HORAS_POR_SEMANA

#-----------------------------------------
#------- HORAS POR ROL EN UNA FASE -------
#-----------------------------------------

def horas_por_rol_en_fase(tipologia, fase, rol):
    horas = horas_fase(tipologia, fase)
    dedicacion = df_dedicacion_fases.loc[rol,fase]
    return horas * dedicacion

#-----------------------------------------
#--------- CARGA DE UN PROYECTO ----------
#-----------------------------------------

def carga_proyecto(row):
    tipologia = row["Tipologia"]
    fase = row["Fase"]
    rol = row["Rol"]
    return horas_por_rol_en_fase(tipologia, fase, rol)

#-----------------------------------------
#---------- CARGA TOTAL POR ROL ----------
#-----------------------------------------

def carga_total_por_rol(df_proyectos):
    carga ={}
    for _, row in df_proyectos.iterrows():
        rol = row["Rol"]
        carga.setdefault(rol, 0)
        carga[rol] += carga_proyecto(row)
    
    return carga

#-----------------------------------------
#----- CAPACIDAD POR ROL (del equipo) ----
#-----------------------------------------

def capacidad_por_rol(df_equipo):
    return(
        df_equipo.groupby("Rol")["Horas disponibles"]
        .sum()
        .reset_index()
        .rename(columns={"Horas disponibles": "Capacidad (h)"})
    )

#--------------------------------------------
#---- RESUMEN FINAL (Capacidad vs carga) ----
#--------------------------------------------

def resumen_capacidad(df_cap_rol, carga_por_rol_dict):
    df=df_cap_rol.copy()
    
    #---Carga total por rol
    
    df["Carga (h)"] = df["Rol"].map(carga_por_rol_dict).fillna(0)
    
    #---Cálculos de ocupación y disponibilidad
    
    df["% Ocupación"] = (df["Carga (h)"] / df["Capacidad (h)"]*100).round(1)
    df["% Disponibilidad"] = (100-df["% Ocupación"]).round(1)
    return df