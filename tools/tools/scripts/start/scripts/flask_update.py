#!/usr/bin/env python3 

from flask import Flask, request, jsonify,url_for
from flask import make_response, json, redirect
from flask import abort, make_response, render_template

import test_wh 


igv_tools = test_wh.IgvVehicleTools()

app = Flask(__name__)

@app.route("/error")
def error():
    return render_template('error.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html"),404

@app.route('/')
def index():
    return redirect(url_for('page_not_found'))

@app.route('/login')
def user():
    abort(401)
    return render_template('login.html')

@app.route('/update', methods=["POST","GET"])
def update():
    GET_VERSION = request.values.get("version")
    print(GET_VERSION)
    if GET_VERSION == 1 :
        print("version:{0}".format(GET_VERSION))
    return render_template('update.html', url_for('static', filename='css/update.css'))

if __name__ == "__main__":
    app.run()

