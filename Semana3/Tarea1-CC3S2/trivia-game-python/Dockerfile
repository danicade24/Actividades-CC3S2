FROM python:3.9-slim

WORKDIR /app

# Instala netcat-openbsd y actualiza los paquetes
RUN apt-get update && apt-get install -y netcat-openbsd

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Cambia el WORKDIR solo para `init_db`
RUN export PYTHONPATH=/app/src

CMD ["uvicorn","src.main:app","--host","0.0.0.0","--port","8000"]

# Ajustar la linea de main:app por ejemplo si main esta en una
# carpeta src deberia decir src.main:app