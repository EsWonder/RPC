from xmlrpc.client import ServerProxy

# Crear el objeto proxy para conectarse al servidor RPC
proxy = ServerProxy("http://127.0.0.1:8000")

# Hacer una solicitud al servidor
response = proxy.say_hello("Mundo")

# Imprimir la respuesta del servidor
print(response)
