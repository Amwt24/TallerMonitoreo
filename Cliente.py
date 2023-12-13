import socket
import json

def iniciar_servidor(puerto):
    # Crear un socket de tipo servidor
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.bind(('10.119.252.102', puerto))
        print(f"Escuchando en el puerto {puerto}...")

        # Esperar por conexiones entrantes (máximo 1 conexión a la vez)
        servidor.listen(1)

        # Aceptar la conexión entrante
        conexion, direccion = servidor.accept()
        print(f"Conexión establecida desde: {direccion}")

        # Recibir datos del cliente
        datos_recibidos = conexion.recv(1024).decode()
        informacion = json.loads(datos_recibidos)

        # Mostrar la información del sistema recibida
        print("Información del sistema recibida:")
        print(json.dumps(informacion, indent=4))

if __name__ == "__main__":
    # Puerto en el que el servidor estará escuchando
    puerto_local = 65432

    iniciar_servidor(puerto_local)
