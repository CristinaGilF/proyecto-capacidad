import pandas as pd

#---Se definen los tiempos de dedicación estimados en cada fase para cada rol existente en el equipo
# R: Requisitos | V: Viabilidad | A: Aprobaciones | D: Diseño | S: Pruebas Unitarias | U: Pruebas de usuario
# P: Paso a producción | E: Estabilización | C: Configuración
df_dedicacion_fases = pd.DataFrame({
    "fase":["R","V","A","D","S","U","P","E"],
    "Gestion":[0.50,0.60,0.10,0.50,0.30,0.40,0.10,0.10],
    "Desarrollador CRM":[0.30,0.30,0.00,0.75,0.60,0.80,0.50,0.10],
    "Desarrollador Facturacion":[0.30,0.20,0.00,0.50,0.40,0.50,0.50,0.10]
}).set_index("fase").T

#---Tipologías de proyecto
#---Se definen las diferentes tipologías que existen de proyecto

df_tipologias = pd.DataFrame({
    "Tipologia":[
        "SF",
        "Servicio",
        "Servicio complejo",
        "Automatizacion",
        "Modificaciones",
        "Flash"
    ],
    "R":[1,1,1,1,1,1],
    "V":[1,1,1,1,1,0],
    "A":[1,1,1,1,1,0],
    "D":[1,1,1,1,1,0],
    "S":[1,1,1,1,1,0],
    "U":[1,1,1,1,1,0],
    "P":[1,1,1,1,1,1],
    "E":[1,1,1,1,1,1],
})

df_duraciones_fases = pd.DataFrame({
    "Tipologia": ["SF", "Servicio", "Servicio complejo", "Automatizacion", "Modificaciones", "Flash"],
    "R": [40, 40, 120, 40, 80, 8],
    "V": [40, 40, 80, 80, 80, 0],
    "A": [40, 40, 40, 40, 40, 0],
    "D": [16, 20, 80, 80, 120, 0],
    "S": [16, 20, 80, 40, 120, 0],
    "U": [0, 40, 40, 40, 80, 0],
    "P": [8, 40, 40, 40, 40, 8],
    "E": [40, 480, 480,480,480,40]
    }).set_index("Tipologia")

df_roles_necesarios = pd.DataFrame({
    "Tipologia": ["SF", "Servicio", "Servicio complejo", "Automatizacion", "Modificaciones", "Flash"],
    "Gestion": [1, 1, 1, 1, 1, 0],
    "Desarrollador CRM": [0, 1, 2, 2, 3, 1],
    "Desarrollador Facturacion": [0, 1, 1, 1, 2, 0]
    }).set_index("Tipologia")