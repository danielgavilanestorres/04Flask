from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hola():
    return render_template("index.html")

@app.route('/play')
def play():
    return render_template("index.html", numero = 3, color = "rgb(143, 201, 252)")

@app.route('/play/<int:numero>')
def playNumero(numero):
    return render_template("index.html", numero = numero, color = "rgb(143, 201, 252)")

@app.route('/play/<int:numero>/<string:color>')
def playNumeroColor(numero, color):
    return render_template("index.html", numero = numero, color = color)

if __name__ == "__main__":
    app.run(debug=True)