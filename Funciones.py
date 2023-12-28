
# le doy la primera funcion para API (PlayTimeGenre)

import pandas as pd
import numpy as np


df_PlayTimeGenre = pd.read_csv("DATA FUNCIONES/PlayTimeGenre.csv")

def play_time_genre(x: str):

    # Filtrar el DataFrame para el género específico
    df_genero = df_PlayTimeGenre.loc[df_PlayTimeGenre['Genero'] == x]

    # Encontrar el año con más horas jugadas para ese género
    año_max_playtime = df_genero.loc[df_genero['playtime_forever'].idxmax(), 'Año_Lanzamiento']

    # Crear la leyenda
    leyenda = f"Año de lanzamiento con más horas jugadas para Género {x}: {año_max_playtime}"

    return leyenda