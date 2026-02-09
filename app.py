import random
from flask import Flask, jsonify
from bayeta import frotar

app = Flask(__name__)

@app.route('/')
def home():
    # Generamos un número aleatorio entre 1 y 10
    repeticiones = random.randint(1, 10)
    
    # Creamos el texto base
    frase = "¡Hola, mundo! Bienvenido a La Bayeta de la Fortuna.<br>"
    
    # Lo repetimos en bucle
    contenido = ""
    for i in range(repeticiones):
        contenido += f"{i+1}. {frase}"
    
    return f"<html><body><h1>Sesión de hoy ({repeticiones} veces):</h1>{contenido}</body></html>"

@app.route('/frotar/<int:n_frases>')
def get_frases(n_frases):
    lista_frases = frotar(n_frases)
    return jsonify({"frases": lista_frases, "cantidad": n_frases})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
