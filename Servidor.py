import socket
import json
import psutil

def enviar_informacion_sistema(ip_servidor, puerto_servidor):
    informacion_sistema = {
        "CPU": psutil.cpu_percent(interval=1, percpu=True),
        "RAM": psutil.virtual_memory().percent,
        "Disco": psutil.disk_usage('/').percent

        # Información del sistema
    }

    # Convertir a formato JSON
    informacion_json = json.dumps(informacion_sistema)

    # Crear un socket y conectar al servidor
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente.connect((ip_servidor, puerto_servidor))

        # Enviar datos al servidor
        cliente.sendall(informacion_json.encode())

if __name__ == "__main__":
    # IP y puerto del servidor (tu PC local)
    ip_servidor = '10.3.20.248'  # Cambia a la IP de tu PC local o 'localhost'
    puerto_servidor = 65432  # Puerto donde el servidor estará escuchando

    enviar_informacion_sistema(ip_servidor, puerto_servidor)
