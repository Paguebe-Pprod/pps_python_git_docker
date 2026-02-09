import random
from flask import Flask, jsonify
from bayeta import frotar

app = Flask(__name__)

@app.route('/')
def home():
    # Llamamos a la función para obtener 1 sola frase
    resultado = frotar(1)
    
    # Extraemos el texto de la lista (o mensaje de error)
    frase_del_dia = resultado[0] if resultado else "La bayeta está seca hoy..."
    
    # Retornamos el HTML básico con la frase única
    return f"<html><body><h1>Tu fortuna de hoy:</h1><p>{frase_del_dia}</p></body></html>"

@app.route('/frotar/<int:n_frases>')
def get_frases(n_frases):
    # Endpoint para devolver JSON si se piden varias frases
    lista_frases = frotar(n_frases)
    return jsonify({"frases": lista_frases, "cantidad": n_frases})

if __name__ == '__main__':
    # El host 0.0.0.0 es clave para que funcione luego en Docker
    app.run(host='0.0.0.0', port=5000)
