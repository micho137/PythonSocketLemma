# Utiliza una imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY requirements.txt .
COPY src/ src/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que tu aplicación Flask estará escuchando
EXPOSE 4890

# Comando de inicio para Gunicorn
CMD ["gunicorn", "-k", "eventlet", "app:app", "--bind", "0.0.0.0:4890"]
