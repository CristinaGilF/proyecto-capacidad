import pandas as pd
from logica.calculo_capacidad import carga_total_por_rol, capacidad_por_rol

def simular_proyecto(
        tipologia,
        df_equipo,
        df_proyectos,
        df_duraciones_fases,
        df_roles_necesarios,
        df_dedicacion_fases
):

    #--------------------------------------------------------------------------------
    #--- Simula el impacto de añadir un nuevo proyecto de la tipología seleccionada--
    #---Devuelve un datafrane con: --------------------------------------------------
    #-------capacidad por rol, carga actual por rol, carga simulada de la nueva -----
    #-------petición, carga total y ocupación resultante ----------------------------
    #--------------------------------------------------------------------------------

    #--- Capacidad actual por rol

    df_capacidad=capacidad_por_rol(df_equipo)
    capacidad_por_rol_dict = dict(zip(df_capacidad["Rol"], df_capacidad["Capacidad (h)"]))

    #--- Carga actual por rol

    carga_actual_por_rol = carga_total_por_rol(df_proyectos)

    #--- Carga simulada del nuevo proyecto

    carga_simulada_por_rol = {}

    #--- Fases del modelo

    fases = df_duraciones_fases.columns

    for fase in fases:
        duracion = df_duraciones_fases.loc[tipologia, fase]
        if duracion == 0:
            continue #la fase no aplica

        for rol in df_roles_necesarios.columns:
            n_roles = df_roles_necesarios.loc[tipologia, rol]
            if n_roles == 0:
                continue

            dedicacion = df_dedicacion_fases.loc[rol, fase]/100
            horas = duracion * dedicacion * n_roles

            carga_simulada_por_rol[rol] = carga_simulada_por_rol.get(rol,0) + horas

    #--- Unificar roles

    roles = (
        set(capacidad_por_rol_dict.keys()) | 
        set(carga_actual_por_rol.keys()) | 
        set(carga_simulada_por_rol.keys())
    )

    resultados = []

    for rol in sorted(roles):
        cap = capacidad_por_rol_dict.get(rol, 0)
        actual = carga_actual_por_rol.get(rol, 0)
        nuevo = carga_simulada_por_rol.get(rol, 0)
        total = actual + nuevo
        ocupacion = (total/cap*100) if cap > 0 else 0

        resultados.append({
            "Rol": rol,
            "Capacidad (h)": cap,
            "Carga actual (h)": round(actual, 1),
            "Carga nuevo proyecto (h)": round(nuevo, 1),
            "Carga total (h)": round (total, 1),
            "Ocupación (%)": round(ocupacion, 1)
        })

    return pd.DataFrame(resultados)