import requests

# 1. Probar la Landing Page (GET)
url_landing = "http://127.0.0.1:8000/"
print("Probando Landing:", requests.get(url_landing).json())

# 2. Probar la Predicción (POST)
url_predict = "http://127.0.0.1:8000/predict"
# Aquí ponemos una lista de números (features) que el modelo entienda
datos = {
    "features": [
        150.1, 152.5, 149.0, 151.2, 151.2, 1000000, # Open, High, Low, Close, Adj, Vol
        0.005, 0.004,                               # Returns
        150.5, 149.8, 148.5,                        # Lags de Close
        0.002, 0.001, -0.001,                       # Lags de Return
        150.2, 149.5, 147.0,                        # SMAs (5, 10, 20)
        1.5, 1.8, 2.1,                              # Volatilidad
        2.5, 3.0,                                   # Momentum
        55.0,                                       # RSI (valor normal entre 0 y 100)
        150.8, 149.2,                               # EMAs
        1.5, 1.2                                    # MACD y Signal
    ]
}
respuesta = requests.post(url_predict, json=datos)

print("Resultado de la predicción:", respuesta.json())