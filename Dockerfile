# Usa una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto en el contenedor
COPY . /app

# Instala las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto que usará el servidor (8000)
EXPOSE 8000

# Comando para ejecutar el servidor RPC cuando el contenedor se inicie
CMD ["python", "server.py"]
