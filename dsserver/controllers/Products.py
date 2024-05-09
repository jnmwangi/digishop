from flask_restful import Resource
from flask import jsonify

class Products(Resource):
    catelog = [
        {
            "name":"HP Laptop",
            "description":"Corei 5, RAM 16GB, SDR 500GB"
        },
        {
            "name":"Lenovo",
            "description":"Corei 7, RAM 32GB, SDR 500GB"
        }
    ]
    
    def get(self):
        return jsonify(self.catelog)