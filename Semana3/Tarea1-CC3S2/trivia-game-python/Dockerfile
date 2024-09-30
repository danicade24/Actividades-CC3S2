FROM python:3.9-slim

# Establecemos el directorio de trabajo dentro del contenedor como /app.
WORKDIR /app

# Copiamos el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Ejecutamos pip para instalar las dependencias listadas en requirements.txt.
# La opción --no-cache-dir evita que pip guarde archivos innecesarios
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todo el contenido del directorio actual en el directorio /app del contenedor
COPY . .

EXPOSE 8000

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]