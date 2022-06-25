from flask import Flask, render_template

app = Flask(__name__)

@app.errorhandler(404)
def paginaNoEncontrada(e):
    return '¡Lo siento! No hay respuesta. Inténtalo otra vez.'

@app.route('/')
def Hola():
    return '¡Hola Mundo!'

@app.route('/dojo')
def dojo():
    return '¡Dojo!'

@app.route('/say/<string:nombre>')
def say(nombre):
    return f'¡Hola, {nombre.capitalize()}!' 

@app.route('/repeat/<int:num>/<string:palabra>')
def repeat(num, palabra):
    return f' {num * palabra}'

if __name__ == "__main__":
    app.run(debug = True)

