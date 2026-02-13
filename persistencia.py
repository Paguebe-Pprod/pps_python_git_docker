from pymongo import MongoClient
import os

# Si estamos en Docker, usamos el nombre del contenedor 'mongo-db', 
# si no, usaremos 'localhost'
MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')

def instanciar():
    cliente = MongoClient(f'mongodb://{MONGO_HOST}:27017/')
    bd = cliente['bayeta']
    coleccion = bd['frases_auspiciosas']
    return cliente, coleccion

def inicializar(fichero_texto="frases.txt"):
    cliente, coleccion = instanciar()
    
    if coleccion.count_documents({}) == 0:
        if os.path.exists(fichero_texto):
            with open(fichero_texto, "r", encoding="utf-8") as f:
                frases = [{"frase": linea.strip()} for linea in f if linea.strip()]
            if frases:
                coleccion.insert_many(frases)
                print(f"Base de datos inicializada con {len(frases)} frases.")
    cliente.close()

def consultar(n_frases=1):
    cliente, coleccion = instanciar()
    frases_cursor = coleccion.aggregate([{'$sample': {'size': n_frases}}])
    resultado = [f['frase'] for f in frases_cursor]
    cliente.close()
    return resultado

def annadir_frases(lista_frases):
    cliente, coleccion = instanciar()
    documentos = [{"frase": f} for f in lista_frases]
    resultado = coleccion.insert_many(documentos)
    cliente.close()
    return len(resultado.inserted_ids)
