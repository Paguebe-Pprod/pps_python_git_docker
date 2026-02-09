# pps_python_git_docker
Repositorio para realizar la tarea de P.Produccion

## Tecnologías
- Python
- Git
- Docker

## Cometido
Esta app tiene como función decir frases aleatorias de futuro como si fuera galleta de la fortuna.
Como referencia ver el capítulo de Rick y Morty "Desmitificación Final"

## Instalación y uso
Para ejecutar esta aplicación en local, sigue estos pasos:

1. **Crear el entorno virtual:** `python3 -m venv venv`
2. **Activar el entorno:** `source venv/bin/activate`
3. **Instalar dependencias:** `pip install -r requirements.txt`
4. **Ejecutar:** `python app.py`

# Momento actual
el programa ya da una sola respuesta de vaticionio por llamada


# Para correr el docker
1. Construir la imagen: usar el comando `docker build -t bayeta-app` .
2. Correr el contenedor `docker run -p 5000:5000 bayeta-app`
