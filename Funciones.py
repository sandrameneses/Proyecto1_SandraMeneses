
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


# Segunda funcion UserForGenre

def user_for_genre(x: str):

    # Leer el DataFrame desde el archivo CSV
    dataframe = pd.read_csv("DATA FUNCIONES/UserForGenre.csv")

    # Filtrar el DataFrame por el género dado
    genre_df = dataframe.loc[dataframe['Genero'] == x]

    if genre_df.empty:
        return {"error": "No hay datos para el género proporcionado"}

    # Encontrar el usuario con más horas jugadas
    max_hours_user = genre_df.loc[genre_df['Horas_Jugadas'].idxmax()]['Id_user']

    # Agrupar por año y sumar las horas jugadas
    hours_by_year = genre_df.groupby('Año_Lanzamiento')['Horas_Jugadas'].sum().reset_index()

    # Convertir el resultado a un formato de lista de diccionarios
    hours_list = [{'Año': int(row['Año_Lanzamiento']), 'Horas': int(row['Horas_Jugadas'])} for index, row in hours_by_year.iterrows()]

    # Crear el resultado final en el formato deseado
    result = {"Usuario con más horas jugadas para Género {}".format(x): max_hours_user, "Horas jugadas": hours_list}

    return result


# Tercera Funcion Users_Recommend

def users_recommend(x: int):
    # Leer el DataFrame desde el archivo CSV
    dataframe = pd.read_csv("DATA FUNCIONES/UsersRecommend.csv")
    
    # Filtrar el DataFrame por el año dado
    year_df = dataframe.loc[dataframe['Año'] == x ]

    if year_df.empty:
        return {"error": "No hay datos para el año proporcionado"}

    # Ordenar el DataFrame por la cantidad de recomendaciones en orden descendente
    sorted_df = year_df.sort_values(by='Recomendaciones', ascending=False)

    # Tomar los tres juegos más recomendados
    top3_games = sorted_df.head(3)['Juego'].tolist()

    # Convertir el resultado a un formato de lista de diccionarios con los puestos correctos
    result = [{"Puesto {}".format(i + 1): juego} for i, juego in enumerate(top3_games)]

    return result


# Cuarta funcion UsersNotRecommend

def users_not_recommend(x: int):
    # Leer el DataFrame desde el archivo CSV
    dataframe = pd.read_csv("DATA FUNCIONES/UsersNotRecommend.csv")

    # Filtrar el DataFrame por el año dado
    year_df = dataframe.loc[dataframe['Año'] == x]

    if year_df.empty:
        return {"error": "No hay datos para el año proporcionado"}

    # Ordenar el DataFrame por la cantidad de recomendaciones en orden ascendente
    sorted_df = year_df.sort_values(by='Recomendaciones')

    # Tomar los tres juegos menos recomendados
    bottom3_games = sorted_df.head(3)['Juego'].tolist()

    # Convertir el resultado a un formato de lista de diccionarios con los puestos correctos
    result = [{"Puesto {}".format(i + 1): juego} for i, juego in enumerate(bottom3_games)]

    return result

# Quinta Funcion Sentiment_Analysis

def sentiment_analysis(x: int):
    # Leer el DataFrame desde el archivo CSV
    dataframe = pd.read_csv("DATA FUNCIONES/Sentiment_Analysis.csv")

    # Filtrar el DataFrame por el año dado
    year_df = dataframe.loc[dataframe['Año_Lanzamiento'] == x]

    if year_df.empty:
        return {"error": "No hay datos para el año proporcionado"}

    # Obtener la cantidad de registros para cada categoría de análisis de sentimiento
    negativo = year_df[year_df['sentiment_analysis'] == 0]['Registros'].sum()
    neutral = year_df[year_df['sentiment_analysis'] == 1]['Registros'].sum()
    positivo = year_df[year_df['sentiment_analysis'] == 2]['Registros'].sum()

    # Crear el resultado en el formato deseado
    resultado = {"Negativo": negativo,
              "Neutral": neutral,
              "Positiv0": positivo}

    return resultado

