# --- Fase 1: Resolución de dependencias (Builder) ---
FROM python:3.12-slim as builder

# Evitamos que Python genere archivos .pyc y buffer de salida
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copiamos los requisitos
COPY requirements.txt .

# Instalamos las dependencias en una ruta local de usuario
RUN pip install --user --no-cache-dir -r requirements.txt


# --- Fase 2: Ejecución (Runner) ---
FROM python:3.12-slim as runner

WORKDIR /app

# Copiamos solo las librerías instaladas desde la fase anterior (builder)
COPY --from=builder /root/.local /root/.local

# Actualizamos el PATH para que encuentre las librerías
ENV PATH=/root/.local/bin:$PATH

# Copiamos el código fuente de la aplicación
COPY . .

# Exponemos el puerto
EXPOSE 5000

# Comando de arranque
CMD ["python", "app.py"]
