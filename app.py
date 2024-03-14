from flask import Flask, render_template, request, url_for, redirect # para usar las paginas dinamicas
import sqlite3

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

@app.route("/dashboard/<string:username>") #<> para pasar los valores de otros definiciones
def dashboard(username):
    return f"Ya estas dentro! {username}"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else: #POST
        username = request.form["username"]
        password = request.form["password"]
        if username == "jan" and password == "666":
            return redirect(url_for('dashboard', username=username))
        else:
            return "contraseña incorrecta"
       # return f"submit resultados con POST {username} y {password}"

@app.route('/pelis')
def peliculas():
    conn = sqlite3.connect('pelis2.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM pelis;")
    rows = cur.fetchall()
    conn.close()
    return render_template("peliculas.html", rows = rows) #sin app.

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method=="GET":
        return render_template("add.html")
    else: #POST
        titulo = request.form["titulo"]
        duracion = request.form["duracion"]
        conn = sqlite3.connect('pelis2.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO pelis (nombre, duracion) VALUES (?,?);", (titulo, duracion))
        conn.commit()
        conn.close()           
        return redirect(url_for('peliculas'))


if __name__ == '__main__':  # siempre abajo de todo
    app.run(debug=True)