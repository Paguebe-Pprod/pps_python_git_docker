import random
from flask import Flask, jsonify, request
from bayeta import frotar, annadir

app = Flask(__name__)

@app.route('/')
def home():
    resultado = frotar(1)
    frase_del_dia = resultado[0] if resultado else "La bayeta está seca hoy..."
    return f"<html><body><h1>Tu fortuna de hoy:</h1><p>{frase_del_dia}</p></body></html>"

@app.route('/frotar/<int:n_frases>')
def get_frases(n_frases):
    lista_frases = frotar(n_frases)
    return jsonify({"frases": lista_frases, "cantidad": n_frases})

@app.route('/frotar/add', methods=['POST'])
def add_frases():
    datos = request.get_json()
    if not datos or 'frases' not in datos:
        return jsonify({"error": "Formato incorrecto"}), 400
    
    cantidad = annadir(datos['frases']) 
    return jsonify({"mensaje": f"Se han añadido {cantidad} frases"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
