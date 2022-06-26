import re
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Inicio():
    usuarios = [
        {'nombre': 'Daniel', 'apellido': 'Gavilanes'},
        {'nombre': 'Michael', 'apellido': 'Choi'},
        {'nombre': 'Jhon', 'apellido': 'Supsupin'},
        {'nombre': 'Mark', 'apellido': 'Guillen'},
        {'nombre': 'KB', 'apellido': 'Tonel'},
        {'nombre': 'Angie', 'apellido': 'Carrillo'}
    ]
    return render_template("index.html", listaUsuarios = usuarios)

if __name__ == "__main__":
    app.run(debug = True)