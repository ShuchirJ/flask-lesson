from flask import Flask, render_template, request # i want these two modules from "flask"


app = Flask(__name__)

@app.route("/") # app.route is a GET request by default
def home_page():
    return render_template("index.html")

@app.post("/") # now we have GET and POST on the "/" route
def post_home():
    print(request.form["name"])
    return render_template("page2.html", name=request.form["name"])

@app.route("/hello/<name>")
def page2(name):
    # name = whatever you type in after the slash
    print(name)
    return render_template("page2.html", name=name)
    # in name1=name2, name1 = the var in the html
    # name2 is the var in python