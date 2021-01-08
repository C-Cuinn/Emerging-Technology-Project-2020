from flask import *
import flask as fl
import json
import numpy as np
import pickle as p

app = Flask(__name__)

INDEX = "index.html"

@app.route('/') 
def home():
  return app.send_static_file('index.html')  

@app.route('/predict',methods = ['POST', 'GET']) 
def predict():
  if request.method == "POST":
    speed = request.form["speed"]
    speed = [float(speed)]
    model = p.load(open('./model_pol.pkl', 'rb'))
    model_prediction = model.predict(speed)
  return render_template(INDEX, prediction=model_prediction[0])
  return render_template(INDEX)