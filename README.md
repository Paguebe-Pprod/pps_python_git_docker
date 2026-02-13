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

## Momento actual
el programa ya da una sola respuesta de vaticionio por llamada


## Para correr el docker
1. Construir la imagen: usar el comando `docker build -t bayeta-app` .
2. Correr el contenedor `docker run -p 5000:5000 bayeta-app`

# Olvida lo anterior, ahora para correr el docker con mongo-db
docker network create bayeta-red
docker stop mongo-db && docker rm mongo-db
docker run -d --name mongo-db --network bayeta-red mongo
docker build -t bayeta-app:v2 .
docker run -d -p 5000:5000 --name bayeta-web \
  --network bayeta-red \
  -e MONGO_HOST=mongo-db \
  bayeta-app:v2

## Requisitos: 
MongoDB en el puerto 27017 . Aunque esto en principio lo hace la función inicialiar del script `persistencia.py`


## Olvida lo anterior de lo anterior, ahora con compose es 
1. estar en el directorio donde se encuentre el fichero
2. comando `docker-compose up -d`
3. para ver si todo está bien `docker-compose ps`
4. para parar el compose `docker-compose down`
