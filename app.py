from flask import Flask, request
import os
from datetime import datetime
from flask.templating import render_template
from werkzeug.utils import redirect

app = Flask(__name__)

def fecha():
    now = datetime.now()
    year = now.year
    return f"{year}"

@app.route("/")
def principal():
    y = fecha()
    return render_template("index.html",yr = y)

@app.route("/mensaje", methods=['POST'])
def mensaje():
    nombre = request.form['nombres']
    telefono = request.form['telefono']
    texto = request.form['comment']
    return  redirect(f"https://wa.me/573153495460?text=*De:*%20_{nombre}_%0A%0A*Teléfono:*%20_{telefono}_%0A%0A*Mensaje:*%20_{texto}_")

if __name__ == '__main__':
    app.run(debug=True,port=3000)