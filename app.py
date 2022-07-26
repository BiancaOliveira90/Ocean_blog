from flask import Flask, render_template

app = Flask("hello")

@app.route("/")
@app.route("/hello")
def hello():
    return "Hello World"

@app.route("/meucontato")
def meuContato():
    return render_template("index.html")


@app.route("/Dylan")
def Dylan():
    return """<html>
    <head>
         <title> Dylan </title>
    </head>
    <body>
    <h1>Te amo bem grandão!</h1>
    </body>
    </html>"""
      
  

     
    