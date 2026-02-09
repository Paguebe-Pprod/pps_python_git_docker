from flask import Flask, jsonify
from bayeta import frotar

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>¡Hola, mundo! Bienvenido a La Bayeta de la Fortuna</h1>"

@app.route('/frotar/<int:n_frases>')
def get_frases(n_frases):
    lista_frases = frotar(n_frases)
    return jsonify({"frases": lista_frases, "cantidad": n_frases})

if __name__ == '__main__':
    # Ejecutamos en el puerto 5000
    app.run(host='0.0.0.0', port=5000)
