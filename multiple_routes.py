from flask import Flask, render_template, request # i want these two modules from "flask"


app = Flask(__name__)

@app.route("/") # app.route is a GET request by default
def home_page():
    name = request.args.get("name")
    return render_template("index.html", name=name)

@app.post("/") # now we have GET and POST on the "/" route
def post_home():
    print(request.form)
    return render_template("page2.html", name=request.form["name"])

@app.route("/hello/<name>")
def page2(name):
    # name = whatever you type in after the slash
    print(name)
    return render_template("page2.html", name=name)
    # in name1=name2, name1 = the var in the html
    # name2 is the var in python


"""
Make a website that takes messages from users using a text input 
and submit button. The website should show all messages people 
have submitted. You can use a list to store messages received, 
then send the list to the HTML to show each message. 
Here is a quick tutorial: 
https://github.com/ShuchirJ/flask-lesson/blob/main/templating.md
"""