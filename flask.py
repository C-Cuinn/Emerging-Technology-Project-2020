import flask as fl

import numpy as np

app = fl.Flask(__name__)

@app.route("/")
def home(): # 
  return app.send_static_file('index.html')

@app.route('/api/power_gen_lin')
def power_gen_lin():
    return {}

@app.route('/api/power_gen_pol')
def power_gen_pol():
    return {}
    

