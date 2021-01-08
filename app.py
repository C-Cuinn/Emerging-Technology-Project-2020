from flask import *
import flask as fl
import json
import numpy as np
import pickle as p
import joblib

app = Flask(__name__)

INDEX = "index.j2"

@app.route('/',methods = ['GET','POST']) 
def home():
  if request.method == "POST":
    try:

      speedInput = request.form["speed"]
      # speed = np.array(speedInput).reshape(1, -1)
      model = joblib.load("model")
      speed = model.fit_transform(np.array(speedInput).reshape(1,-1))
      print(speed)
      model_prediction = model.predict(speed)
      print(model_prediction)
      # type (model_prediction)
      # return render_template(INDEX, output=model_prediction[0])
      return render_template(INDEX, output="")
    except Exception as ex:
      print(ex)

  if request.method == "GET":
    return render_template(INDEX, output="")

if __name__ == '__main__':
  app.run(debug = True)