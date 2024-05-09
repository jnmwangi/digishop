from flask import Flask, send_file, send_from_directory
from flask_restful import Api
from controllers.Products import Products
from flask_cors import CORS
import os

BASEPATH = os.path.abspath(os.path.dirname(__file__))
print(BASEPATH)

app = Flask(__name__)
CORS(app)
api = Api(app)

@app.route('/')
def root():
    return send_file(os.path.join(BASEPATH, 'static/index.html'))

@app.route('/<path:path>')
def staticfiles(path):
    if os.path.exists(os.path.join(BASEPATH, "static", path)):
        return send_from_directory(os.path.join(BASEPATH, "static"), path)
    else:
        return send_file(os.path.join(BASEPATH, 'static/index.html'))
    
api.add_resource(Products, '/api/products')

if __name__ == "__main__":
    app.run(debug=True, port=5003)