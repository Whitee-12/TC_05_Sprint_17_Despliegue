from fastapi import FastAPI
import pickle
import numpy as np
from pydantic import BaseModel

app = FastAPI()

# -------------------------
# Cargar modelo
# -------------------------
with open("model/finished_model.model", "rb") as f:
    model = pickle.load(f)

# -------------------------
# Validación de inputs
# -------------------------
class InputData(BaseModel):
    features: list

# -------------------------
# Landing page
# -------------------------
@app.get("/")
def landing():
    return {
        "message": "Bienvenido a la API del modelo",
        "endpoints": {
            "/predict": "Devuelve una predicción. POST con JSON {'features': [...]}",
            "/extra": "Endpoint extra para redeploy (comentado por defecto)"
        }
    }

# -------------------------
# Endpoint de predicción
# -------------------------
@app.post("/predict")
def predict(data: InputData):
    X = np.array(data.features).reshape(1, -1)
    pred = model.predict(X)[0]
    return {"prediction": float(pred)}

# -------------------------
# Endpoint extra (comentado)
# -------------------------
# @app.get("/extra")
# def extra():
#     return {"message": "Este endpoint se activa para demostrar redeploy"}
