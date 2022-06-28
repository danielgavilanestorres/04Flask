import random
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = 'HolaHolaHolaHola'
aleatorio = random.randint(1, 100)
contador = 0

@app.route('/')
def Inicio():

    session['contador']
    session['aleatorio'] = aleatorio
    print(session['aleatorio'])

    return render_template("index.html")

@app.route('/numeroElegido', methods = ['POST'])
def numeroElegido():
    session['numero'] = request.form['adivinaText']
    return redirect ('/resultado')

@app.route('/resultado')
def resultado():
    if session['contador'] < 4:

        if int(session['aleatorio']) == int(session['numero']):
            session['resultado'] = "Ganaste"
        elif int(session['aleatorio'] > int(session['numero'])):
            session['resultado'] = "Muy Bajo"
            session['contador'] += 1
            print(session['contador'])
        elif int(session['aleatorio'] < int(session['numero'])):
            session['resultado'] = "Muy Alto"
            session['contador'] += 1
    else:
        session['resultado'] = "Nuevo"
        session['contador'] = 0

    return redirect('/')

@app.route('/nuevoJuego', methods = ['post'])
def nuevoJuego():
    session.pop('resultado')
    session['contador'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)