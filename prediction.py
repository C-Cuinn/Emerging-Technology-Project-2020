from flask import *
import flask as fl
import json
import numpy as np
import pickle as p
import joblib
import sys

app = Flask(__name__)

INDEX = "/index.j2"

@app.route('/',methods = ['GET','POST']) 
def home():
  if request.method == "POST":
    try:
      speed = request.form["speed"]
      speed = [float(speed)]
      model = joblib.load("model")
      model_prediction = model.predict([speed])
      type (model_prediction)
      return render_template(INDEX, output=model_prediction[0])
    except:
      print(sys.exc_info()[0])
  return render_template(INDEX)

  if request.method == "GET":
    return render_template(INDEX,output=" weinus")

if __name__ == '__main__':
  app.run(debug = True)