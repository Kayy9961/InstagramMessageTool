import logging
from instagrapi import Client
import os
from datetime import datetime

logging.getLogger("instagrapi").setLevel(logging.CRITICAL)

def silent_public_request(self, url, data=None, params=None, headers=None):
    try:
        return self.private_request(url, data=data, params=params, headers=headers)
    except Exception:
        return None

Client.public_request = silent_public_request

cl = Client()

SESSION_ID = "TU_SESSIONID_AQUÍ"

try:
    cl.login_by_sessionid(SESSION_ID)
    print("Inicio de sesión exitoso mediante token.")
except Exception as e:
    print(f"Error al iniciar sesión: {e}")
    exit()

try:
    threads = cl.direct_threads()
except Exception as e:
    print(f"Error al obtener los hilos de mensajes: {e}")
    exit()

ultimas_5_personas = []

for thread in threads[:5]:
    if len(thread.users) == 1:
        usuario = thread.users[0].username
    else:
        usuario = ", ".join([user.username for user in thread.users])
    ultimas_5_personas.append(usuario)

print("\nÚltimas 5 personas con las que has hablado:")
for idx, usuario in enumerate(ultimas_5_personas, start=1):
    print(f"{idx}. {usuario}")

nombre_buscado = input("\nIngresa el nombre de usuario para ver los últimos mensajes: ").strip()

def encontrar_thread(threads, nombre):
    for thread in threads:
        if len(thread.users) == 1 and thread.users[0].username.lower() == nombre.lower():
            return thread
        elif len(thread.users) > 1:
            usernames = [user.username.lower() for user in thread.users]
            if nombre.lower() in usernames:
                return thread
    return None

thread_encontrado = encontrar_thread(threads, nombre_buscado)

if thread_encontrado:
    messages = thread_encontrado.messages
    total_mensajes = len(messages)
    print(f"\nÚltimos mensajes con {nombre_buscado} (Total de mensajes: {total_mensajes}):\n")
    
    num_mensajes_a_mostrar = 10
    mensajes_a_mostrar = (
        messages[-num_mensajes_a_mostrar:] if total_mensajes >= num_mensajes_a_mostrar else messages
    )
    
    mensajes_a_mostrar = sorted(mensajes_a_mostrar, key=lambda msg: msg.timestamp)
    
    for msg in mensajes_a_mostrar:
        try:
            sender_username = cl.user_info(msg.user_id).username if msg.user_id else 'Desconocido'
        except Exception:
            sender_username = "Desconocido"
        timestamp = msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        if hasattr(msg, "text") and msg.text:
            text = msg.text
        elif hasattr(msg, "media"):
            text = "[Archivo multimedia: Foto, Video o Audio]"
        else:
            text = "[Mensaje sin texto]"

        print(f"[{timestamp}] {sender_username}: {text}")
else:
    print(f"\nNo se encontró una conversación con '{nombre_buscado}'.")

input("\nPresiona cualquier tecla para salir...")
