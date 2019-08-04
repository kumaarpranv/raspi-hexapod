from flask import Flask, jsonify, render_template, request
from main import *
import json

ct=0
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/get', methods=['GET'])
def post():
    mov=""
    if request.method == "GET":
        mov = request.args.get('mov')
        #print(mov)
        
        if mov == "f":
            frwd()
        if mov == "l":
            left()
        if mov == "r":
            right()
        
        return jsonify({"success" : "true"});

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True, threaded= True)
