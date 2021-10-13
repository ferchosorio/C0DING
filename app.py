from flask import Flask
import os
from datetime import datetime
from flask.templating import render_template

app = Flask(__name__)

#@app.context_processor
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
    return "a"
if __name__ == '__main__':
    app.run(debug=True,port=3000)