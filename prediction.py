from flask import Flask, request, redirect, url_for, flash, jsonify
import json
import numpy as np
import pickle as p

app = Flask(__name__)

@app.route("/", methods=['POST'])
def home():
    data = request.get_json()
    prediction = np.array2string(model_lin(data))

    return jsonify(prediction)

if __name__ == '__main__':
    modelfile = 'model_lin.pickle'
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True, host='0.0.0.0')

@app.route('/api/power_gen_lin', methods=['GET', 'POST'])
def power_gen_lin():
        return {}

@app.route('/api/power_gen_pol', methods=['GET', 'POST'])
def power_gen_pol():
      return {}

