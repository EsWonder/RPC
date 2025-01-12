# server.py
import xmlrpc.server

def say_hello(name):
    return f"Hola, {name}!"

with xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000)) as server:
    print("Servidor RPC iniciado y escuchando en puerto 8000...")
    server.register_function(say_hello, "say_hello")
    server.serve_forever()
