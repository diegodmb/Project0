from flask import Flask, flash, jsonify, redirect, render_template, request
import random
import os
from os import scandir


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.testing = True
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True


if __name__ == "__main__":
    app.run(debug=True)


@app.route("/")
def home():
    rands = random.sample(range(19), 4)
    return render_template("index.html", rands=rands)


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/galeria", methods=["GET", "POST"])
def galeria():
    path = request.form.get("name")
    path2 = "static/img/" + path
    imgs = ls2(path2)
    return render_template("galeria.html", imgs=imgs, path=path2)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")


def ls2(path):
    obj = os.scandir()
    return [obj.name for obj in scandir(path) if obj.is_file()]
