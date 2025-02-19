#!/usr/bin/env python3 

from flask import Flask, request, jsonify,url_for
from flask import make_response, json, redirect
from flask import abort, make_response, render_template

import test_wh 


igv_tools = test_wh.IgvVehicleTools()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def user():
    abort(401)
    # return render_template('login.html')

@app.route('/update', methods=["POST","GET"])
def update():
    if (request.values.get("packages") == 
        request.values.get("package")):
        VERSION = request.values.get("version")
        if request.values.get("version") == None:
            pass
        else:    
            print("需要升级的版本为: {0}={1}" .format(request.values.get("packages"),VERSION))
            update_cmd = request.values.get("packages") + "=" + VERSION
            print(update_cmd)
            igv_tools.qpilot_config(update_cmd)
            
    else:
        print("选择的版本不匹配")
        return render_template('error.html')
    return render_template('update.html')

if __name__ == "__main__":
    app.run()

