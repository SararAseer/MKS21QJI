#Sarar Aseer
#SoftDev1 pd8
#24 REST
#2018-11-14

from flask import Flask, render_template, request
from flask import session, redirect, url_for
import os, urllib, json


app = Flask(__name__)

@app.route('/')
def index():
                     url="https://api.nasa.gov/planetary/apod?api_key=L3V7lEeBNB3NqbKW8ptOg7VBq3jABSBFD7Lkv9wI&date=2018-11-12&hd=True"       
                     hr = urllib.request.urlopen(url)
                     rr = hr.read() 
                     dr = rr.decode() 
                     print(rr)
                     data = json.loads(dr)             
                     return render_template("test2.html", data=data)

if __name__ == '__main__':
                     app.debug = True
                     app.run()

