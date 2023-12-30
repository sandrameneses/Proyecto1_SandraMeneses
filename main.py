
# le doy la primera funcion para API (PlayTimeGenre)

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import pandas as pd
import numpy as np
import Funciones as FU
import importlib
importlib.reload(FU)

app = FastAPI(title='PI1 - Sandra Meneses')

# 1

@app.get(path = "/play_time_genre")

def play_time_genre(x: str):

    return FU.play_time_genre(x)

# 2

@app.get(path = "/user_for_genre")

def user_for_genre(x: str):

    return FU.user_for_genre(x)

# 3 

@app.get(path = "/users_recommend")

def users_recommend(x: int):

    return FU.users_recommend(x)

# 4

@app.get(path = "/users_no_recommend")

def users_no_recommend(x: int):

    return FU.users_recommend(x)

# 5

@app.get(path = "/sentiment_analysis")

def sentiment_analysis(x: int):

    return FU.sentiment_analysis(x)

# Recomendacion 1

@app.get(path=("/users_recommend", "/users_no_recommend"))

def get_item_recommendations(game_name):

    return FU.recommended_games[1:] 
