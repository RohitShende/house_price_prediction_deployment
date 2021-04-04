from flask import Flask, request, jsonify
import joblib
import json
from marshmallow import Schema, fields, ValidationError


app = Flask(__name__)
model = joblib.load('house_price_prediction_trained_model.pkl')

class ParameterSchema(Schema):
    location = fields.Integer(required=True)
    bhk = fields.Integer(required=True)
    area = fields.Integer(required=True)
    old = fields.Integer(required=True)
    floor = fields.Integer(required=True)


@app.route('/')
def index():
    return 'Hello world'



@app.route('/predict',methods = ['POST'])
def predict():

    # Get Request body from JSON
    request_data = request.json
    schema = ParameterSchema()

    try:
        # Validate request body against schema data types
        reqParam = schema.load(request_data)
    except ValidationError as err:
        # Return a nice message if validation fails
        return jsonify(err.messages), 400

    # Convert request body back to JSON str
    location = reqParam['location']
    bhk = reqParam['bhk']
    area = reqParam['area']
    old = reqParam['old']
    floor = reqParam['floor']
    
    returnJson = {}
    # predicting from model
    returnJson['price'] = model.predict(
        [[
            location,
            bhk,
            area,
            old,
            floor,
        ]]
    )[0]
    
    return jsonify(returnJson)

if __name__ == '__main__':
   app.run(threaded=True, port=5000)