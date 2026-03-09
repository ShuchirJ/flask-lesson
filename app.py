from flask import Flask, render_template, request, redirect # i want these two modules from "flask"


app = Flask(__name__)
messages = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/images")
def images():
    return render_template("images.html")