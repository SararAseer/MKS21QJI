#Sarar Aseer
#SoftDev1 pd8
#25 REST
#2018-11-14

from flask import Flask, render_template, request
from flask import session, redirect, url_for
import os, urllib, json


app = Flask(__name__)

@app.route('/')
def index():
                     url="http://www.omdbapi.com/?i=tt3896198&apikey=100a2e2a"       
                     hr = urllib.request.urlopen(url)
                     rr = hr.read() 
                     dr = rr.decode() 
                     print(rr)
                     data = json.loads(dr)             
                     return render_template("test2.html", data=data)

if __name__ == '__main__':
                     app.debug = True
                     app.run()

