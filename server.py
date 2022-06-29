from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = 'hoasdfosdn234ksdlkfj'

@app.route('/')
def Inicio():
    return render_template("index.html")

@app.route('/registroUsuario', methods = ['POST'])
def registroUsuario():
    session['nombre'] = request.form['nombreTxt']
    print(session['nombre'])
    session['locacion'] = request.form['location']
    print(session['locacion'])
    session['lenguaje'] = request.form['lenguage']
    print(session['lenguaje'])
    session['comentarios'] = request.form['comentario']
    print(session['comentarios'])
    return redirect('/resultado')

@app.route('/resultado')
def resultado():
    return render_template("resultado.html")

if __name__ == "__main__":
    app.run(debug = True)