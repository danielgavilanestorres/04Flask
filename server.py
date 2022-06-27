from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    pedido = [
        {'nombre': 'Strawberry', 'cantidad': request.form.get("strawberry")},
        {'nombre': 'Raspberry', 'cantidad': request.form.get("raspberry")},
        {'nombre': 'Apple', 'cantidad': request.form.get("apple")},
        {'nombre': 'Blackberry', 'cantidad': request.form.get("blackberry")}
    ]
    
    persona = {'nombre': request.form.get("first_name"), 'apellido': request.form.get("last_name"), 'id': request.form.get("student_id")}

    totalFrutas = int(request.form.get("strawberry")) + int(request.form.get("raspberry")) + int(request.form.get("apple")) + int(request.form.get("blackberry"))

    return render_template("checkout.html", pedidoFrutas = pedido, infoPersona = persona, totalFrutas = totalFrutas)

@app.route('/fruits')
def fruis():
    frutas = [
        {'nombre': 'Strawberry', 'imagen': '/img/strawberry.png'},
        {'nombre': 'Raspberry', 'imagen': '/img/raspberry.png'},
        {'nombre': 'Apple', 'imagen': '/img/apple.png'},
        {'nombre': 'Blackberry', 'imagen': '/img/blackberry.png'}
    ]
    return render_template("fruits.html", listaFrutas=frutas)


if __name__ == "__main__":
    app.run(debug=True)
