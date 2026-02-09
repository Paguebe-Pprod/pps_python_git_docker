import random
from flask import Flask, jsonify
from bayeta import frotar

app = Flask(__name__)

@app.route('/')
def home():
    resultado = frotar(1)
    frase_del_dia = resultado[0] if resultado else "La bayeta está seca..."
    return f"<h1>Frase de la fortuna:</h1><p>{frase_del_dia}</p>"

@app.route('/frotar/<int:n_frases>')
def get_frases(n_frases):
    lista_frases = frotar(n_frases)
    return jsonify({"frases": lista_frases, "cantidad": n_frases})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
