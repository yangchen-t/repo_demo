#!/usr/bin/env python3 

from flask import Flask, request, jsonify
from flask import make_response, json
from flask import abort, make_response, render_template

import test_wh 


igv_tools = test_wh.IgvVehicleTools()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/')
def user():
    return render_template('login.html')

@app.route('/update')
def update():
    GET_input = request.values.get("methods")
    print(GET_input)
    return render_template('update.html')

if __name__ == "__main__":
    app.run()

