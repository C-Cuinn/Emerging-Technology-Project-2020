import flask as fl

import numpy as np

app = fl.Flask(__name__)

@app.route("/")
def home(): # 
  return app.send_static_file('index.html')

@app.route('/api/power_gen_lin', methods=['GET', 'POST'])
def power_gen_lin():
        form = PowerForm(request.form)

    if request.method == 'POST' and form.validate():
        lin = request.form['lin']
        return render_template('poly.html', power_gen=model_predict(power)[0])
    # Send template information to index.html
    return render_template('index.html', form=form)

@app.route('/api/power_gen_pol', methods=['GET', 'POST'])
def power_gen_pol():
    return {}