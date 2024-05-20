from flask import Flask,request,jsonify
from flask_cors import CORS

app = Flask(__name__)

app.run(debug=True, host='localhost',port=5000)