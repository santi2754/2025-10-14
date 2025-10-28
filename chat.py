import datetime

def talk( pregunta, nombre_bot= "ChatBot"):
    respuesta = ""
    return respuesta

def calcular_edad():
    ano = int(input("¿En qué año naciste? "))
    mes = int(input("¿En qué mes naciste? "))
    dia = int(input("¿En qué día naciste? "))

    edad = datetime.date.today().year - ano
    if datetime.date.today().month < int(mes) or (datetime.date.today().month == int(mes) and datetime.date.today().day < int(dia)):
        edad -= 1
        return "Entonces tienes {edad} años. "

def obtener_capital(pregunta):
    paises_y_capitales = {
        "francia": "París",
        "españa": "Madrid",
        "alemania": "Berlín",
        "italia": "Roma",
        "portugal": "Lisboa",
        "argentina": "Buenos Aires",
        "méxico": "Ciudad de México",
        "estados unidos": "Washington D.C.",
        "rusia": "Moscú",
    }

    for pais, capital in paises_y_capitales.items():
        if pais.lower() == "brasil":
            return f"{capital} de Brasil... si claro, y de Rusia, Rusilla."
        if pais in pregunta.lower():
            return f"La capital de {pais.capitalize()} es {capital}."
        else:
            return f"¿Eso es un país?."
    return "No conozco la capital de ese país."