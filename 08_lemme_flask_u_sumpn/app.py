# Sarar Aseer
# SoftDev1 pd8
# K08 -- Fill Yer Flask
# 2018-09-19

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
 return 'hi'

@app.route('/eg')
def english():
 return 'cat'

@app.route('/eb')
def german():
 return 'dog'

app.debug = True
app.run()
