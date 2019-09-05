#!/usr/bin/env python3

import json
from flask import (Flask, render_template, redirect, url_for,
                   request, make_response, flash)
from options import DEFAULTS

app = Flask(__name__)
app.secret_key = 'esauhou>UO>au.sh35@<Uouo52%@#ouo.42!@#42'

def get_saved_data():
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:
        data = {}
    return data

@app.route('/')
def index():
    return render_template('index.html', saves=get_saved_data())

@app.route('/builder')
def builder():
    return render_template(
        'builder.html',
        saves=get_saved_data(),
        options=DEFAULTS)

@app.route('/save', methods=['POST'])
def save():
    flash("Alright! That looks awesome!")
    # Make a redirect response
    response = make_response(redirect(url_for('builder')))
    # load data from cookie
    data = get_saved_data()
    # Update data with values from POST request
    data.update(dict(request.form.items()))
    # Save data to cookie for the response
    response.set_cookie('character', json.dumps(data))
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
