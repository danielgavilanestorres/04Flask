from flask import Flask

app = Flask(__name__)

@app.route('/')
def Hola():
    return '¡Hola Mundo!'

@app.route('/dojo')
def dojo():
    return '¡Dojo!'

@app.route('/say/<nombre>')
def say(nombre):
    return f'¡Hola, {nombre.capitalize()}!' 

@app.route('/repeat/<int:num>/<string:palabra>')
def repeat(num, palabra):
    return f' {num * palabra}'

if __name__ == "__main__":
    app.run(debug = True)

