#Sarar Aseer
#SoftDev1 pd8
#26_rrreeesssttt
#2018-11-15

from flask import Flask, render_template  
import urllib.request
import json
import ssl



app = Flask(__name__)

@app.route('/')
def index():
                     url="https://www.boredapi.com/api/activity"
                     context = ssl._create_unverified_context()
                     q = urllib.request.Request(url)
                     q.add_header('User-Agent','Mozilla/5.0')
                     f =  urllib.request.urlopen(q,context=context)                     
                     rr = f.read() 
                     dr = rr.decode() 
                     print(rr)
                     data = json.loads(dr)             
                     return render_template("test2.html", activity=data['activity'], price=data['price'])
if __name__ == '__main__':
                     app.debug = True
                     app.run()

