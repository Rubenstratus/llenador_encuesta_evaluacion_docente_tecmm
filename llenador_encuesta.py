import requests
import random
import time

url_formulario = "https://docs.google.com/forms/d/e/1FAIpQLSfDkzU092EqPbm0dfVk3VnC9J4nZTprLn4AoW4wxWJK14BJ4Q/formResponse"

# Disfrazamos a Python para que parezca Google Chrome y no te corten la conexión
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

for i in range(15):
    # Tus opciones exactas
    opciones_p1 = ["si", "No", "tal vez", "no se que es eso"]  
    opciones_p2 = ["si", "no", "no se que es eso"]
    opciones_p3 = ["Solamente privada", "Solamente publica", "a veces ambas", "no se que es eso"]
    opciones_p4 = ["si, todo original", "no, son piratas", "algunos", "no uso prorgamas asi"]
    opciones_p5 = ["Sí", "No"]
    opciones_p6 = ["Sí", "No", "Tal vez", "realmente no sabia que se podia"]
    
    # Tus IDs reales que ya sacaste
    datos = {
        "entry.134956587": random.choice(opciones_p1),  
        "entry.117589874": random.choice(opciones_p2),  
        "entry.686684728": random.choice(opciones_p3),
        "entry.1558617282": random.choice(opciones_p4),
        "entry.2093124253": random.choice(opciones_p5),
        "entry.1275273558": random.choice(opciones_p6)
    }

    # Bloque try-except para que el script no truene si Google se pone rudo
    try:
        respuesta = requests.post(url_formulario, data=datos, headers=headers)

        if respuesta.status_code == 200:
            print(f"Respuesta {i+1} enviada al tiro.")
        else:
            print(f"Chale, falló la {i+1}. Código: {respuesta.status_code}")
            
    except requests.exceptions.ConnectionError:
        print(f"Google cortó la conexión en la {i+1}, pero seguimos vivos. Pasando a la siguiente...")

    # Pausa aleatoria entre 4 y 8 segundos para parecer humano
    tiempo_espera = random.randint(4, 8)
    time.sleep(tiempo_espera)

print("¡Listo el pollo! 15 enviadas.")
