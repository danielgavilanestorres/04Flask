
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/', methods = ['GET'])
def Inicio():
    session['contador']
    if 'contador' in session:
        session['contador'] = session['contador'] + 1
    else:
        print("La llave no existe")
    
    return render_template("index.html")

@app.route('/destroy')
def BorrarSesion():
    session.clear()
    session['contador'] = 0
    return redirect('/')

@app.route('/sumarDos')
def sumarDos():
    print("Hola")
    session['contador'] = session['contador'] + 1
    return redirect('/')

@app.route('/reset')
def BorrarSesionBoton():
    session.clear()
    session['contador'] = 0
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)