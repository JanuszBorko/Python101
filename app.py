from flask import Flask, render_template # para usar las paginas dinamicas
app = Flask (__name__)

from productos import *

@app.route('/')
def homepage():
    return 'Home Page AQUI. <a href="/agur"> pincha aqui </a> para volver'

@app.route('/lambda')
def sign():

    sign = lambda x: "negat" if x<0 else "posit"   
    return sign(-10)
   
    # resultado = lambda x: "negat" if x<0 else "positivo"
    # return resultado(10)

@app.route('/agur')
def agur():
    return "<h1>agur</h1>"


@app.route('/pagina1')
def pagina1():
    return app.send_static_file("pagina1.html")

@app.route('/pagina2')
def pagina2():
    return app.send_dynamic_file("pagina2.html")

@app.route('/dinamica1')
def dinamica1():
    nombre = "Jon"
    edad = 25
    frutas = ["kiwi","PLATANO", "fresa", "manzana", "mango", "PIÑA"]
    return render_template("pagina1.html", nombre=nombre, edad=edad, frutas=frutas) #sin app.


@app.route('/productos')
def productos():
    pr1= Producto(1, "raqueta", 5.00, "images/raqueta.jpeg")
    pr2= Producto(2, "palo", 3.49, "images/palo.avif")
    pr3= Producto(3, "pelota", 1.99, "images/pelota.jpeg")
    listaProductos = [pr1, pr2, pr3]
    return render_template("productos.html", listaProductos=listaProductos) #sin app.

if __name__ == '__main__':  # siempre abajo de todo
    app.run(debug=True)