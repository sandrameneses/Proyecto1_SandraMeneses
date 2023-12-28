
# le doy la primera funcion para API (PlayTimeGenre)

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import pandas as pd
import numpy as np
import Funciones as FU
import importlib
importlib.reload(FU)

app = FastAPI(title='PI1 - Sandra Meneses')

@app.get(path = "/play_time_genre")

def play_time_genre(x: str):

    return FU.play_time_genre(x)