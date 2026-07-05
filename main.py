import os
import requests
from dotenv import load_dotenv

def buscar_coordenadas(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    respuesta = requests.get(url)
    json_de_cords = respuesta.json()
    cords = {
        "lat": json_de_cords["results"][0]["latitude"],
        "lon": json_de_cords["results"][0]["longitude"]
    }
    return cords

def obtener_clima(diccionario):
    respuesta = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={diccionario["lat"]}&longitude={diccionario["lon"]}&current=temperature_2m&current=weather_code")
    json_de_temp = respuesta.json()
    clima = {
        "estado": json_de_temp["current"]["weather_code"],
        "temperatura": json_de_temp["current"]["temperature_2m"]
    }
    return clima

def filtrar_estado(codigo):
    if codigo == 0:
        filtro = {"estado":"Despejado","recom":"Sentite libre de salir, es un dia muy bueno!!!"}
    elif 1 <= codigo <= 3:
        filtro = {"estado":"Nublado","recom":"El clima esta un poco inestable, lleva un paraguas!!"}
    elif 45 <= codigo <= 48:
        filtro = {"estado":"Con niebla","recom":"Podes salir pero con cuidado, no se ve mucho allá afuera."}
    elif 51 <= codigo <= 67 or (80<= codigo <= 86):
        filtro = {"estado":"Lluvioso","recom":"No te recomiendo salir, pero si sales sal con un paraguas si o si."}
    elif 71 <= codigo <= 77:
        filtro = {"estado":"Nevando","recom":"Esta nevando!!!, te recomiendo abrigarte bien, hacae mucho frio."}
    else:
        filtro = {"estado":"Temporal muy malo","recom":"NO SALGAS!!!Es muy peligroso ahi afuera, quedate en tu casa."}
    return filtro


while True:
    print("----BIENVENIDO AL PROGRAMA DEL CLIMA----")
    ciudad = input("Introduce una ciudad valida: ")
    coordenadas = buscar_coordenadas(ciudad)
    clima_real = obtener_clima(coordenadas)
    estado_actual = filtrar_estado(clima_real["estado"])
    reporte = {
        "ciudad": ciudad,
        "temp": clima_real["temperatura"],
        "estado": estado_actual["estado"],
        "recom": estado_actual["recom"]
    }

    load_dotenv()
    url_discord = os.getenv("URL_C")
    if url_discord is not None:
        datos = {
            "content":
            f"""
            ========================
            Reporte del Clima |
            ------------------
            *Ciudad: {reporte["ciudad"]}
            *Temperatura: {reporte["temp"]}°C
            *Estado: {reporte["estado"]}
            ----------------------------
            |-Recomendación: {reporte["recom"]}-|
            ========================
            """
        }
        respuesta_discord = requests.post(url_discord,json=datos)
    else:
        print("Error no se encontro la variable en .env")








