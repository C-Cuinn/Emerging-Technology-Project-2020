from flask import *
import json
import numpy as np
import pickle as p

app = Flask(__name__)

@app.route('/') 
def predict():
  return app.send_static_file('index.html')  

@app.route('/api/poly',methods = ['POST', 'GET']) 
def render_datafunction(): 

  if request.method == 'POST': 
    result = request.form 
  
  return app.send_static_file("poly.html",result = result) 
  
if __name__ == '__main__': 
  app.run(debug = True)  
