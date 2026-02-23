from flask import Flask, render_template, request, redirect # i want these two modules from "flask"


app = Flask(__name__)
messages = []

@app.route("/")
def home():
    return render_template("index.html", messages=messages)

@app.post("/")
def accept_message():
    message = request.form['message']
    messages.append(message)
    return redirect("/") # sends the browser to the GET route

"""
Add a delete button next to each list item,
The button should be in a form next to a hidden input that has the message to remove,
The delete button should go to a python route that removes that 
message from the list and redirects to /
"""



"""
Make a website that takes messages from users using a text input 
and submit button. The website should show all messages people 
have submitted. You can use a list to store messages received, 
then send the list to the HTML to show each message. 
Here is a quick tutorial: 
https://github.com/ShuchirJ/flask-lesson/blob/main/templating.md
"""