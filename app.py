import pandas as pd
from flask import Flask, jsonify, request
import joblib

app = Flask(__name__) #all instances pointed to app.py file

@app.route('/predict', methods = ['POST'])
def predict():
    req = request.get_json()
    input_data = req['data']
    input_data_df = pd.DataFrame.from_dict(input_data)

    #model = joblib.load('model.pkl')
    model = joblib.load('model.pkl')

    prediction = model.predict(input_data_df)

    if prediction[0] == 1:
        transaction_type = 'Fraudulent'
    else:
        transaction_type = 'Non-fraudulent'
    
    return jsonify({'output':{'transaction_type': transaction_type}}) #convert to json

@app.route('/')
def home():
    return "Credit Card Fraud Detection System"

if __name__ == '__main__':
    app.run(host='localhost', port='3000')