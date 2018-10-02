#Sarar Aseer
#SoftDev1 pd8
#13: Echo Echo Echo
#2018-09-27
from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.secret_key =os.random(32)

@app.route('/')
def index():
    return render_template("test2.html")

@app.route("/auth")
def authenticate():
    return render_template("next.html", user = request.args["username"], method = request.method)

app.debug = True
app.run()
