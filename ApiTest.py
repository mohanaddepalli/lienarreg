import numpy as np
from flask import Flask, request, jsonify
import pickle
import logging
app = Flask(__name__)
# Load the model
model = pickle.load(open('model.pkl','rb'))
@app.route('/api',methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    logging.error(str(data))
    logging.error(str(model))
    # Make prediction using model loaded from disk as per the data.
    
    return jsonify(1)
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)
