from datetime import datetime
import random
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = 'sdfsdfser234swdfesfsdf'

listaAct = []

@app.route('/')
def Inicio():
    if 'scoreGold' not in session:
        session['scoreGold'] = 0

    if 'actividades' not in session:
        session['actividades'] = {}

    if 'act' not in session:
        session['act'] = []

    return render_template("index.html")


@app.route('/process_money', methods=['POST'])
def process_money():
    opcion = request.form['building']
    fechaHora = datetime.now()
    if opcion == 'Farm':
        numero = random.randint(10, 20)
        session['scoreGold'] += numero
    elif opcion == 'Cave':
        numero = random.randint(5, 10)
        session['scoreGold'] += numero
    elif opcion == 'House':
        numero = random.randint(2, 5)
        session['scoreGold'] += numero
    elif opcion == 'Casino':
        numero = random.randint(0, 50)
        session['scoreGold'] -= numero

    listaAct.append([numero, opcion, str(fechaHora.day) + "/" + str(fechaHora.month) + "/" + str(fechaHora.year) + " " + str(fechaHora.hour) + ":" + str(fechaHora.minute)])
    session['act'] = listaAct

    return redirect('/')


@app.route('/nuevoJuego')
def nuevoJuego():
    session.clear()
    listaAct.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
