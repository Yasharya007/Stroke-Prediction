from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS # CORS for handling Cross-Origin Resource Sharing
import pickle 

# Create a Flask application instance
app = Flask(__name__)

# Enable CORS for all routes, allowing requests from any origin
CORS(app,resources={r"/*":{"origins":"*"}})
# try:
#     with open("model.pkl", "rb") as f:
#         est = pickle.load(f)
# except InconsistentVersionWarning as w:
#     print(w.original_sklearn_version)

model = pickle.load(open('RandomForest.pkl', 'rb'))

# Define a route for handling HTTP GET requests to the root URL
@app.route('/', methods=['GET'])
def get_data():
    data = {
        "message":"API is Running"
    }
    return jsonify(data)
  
# Define a route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()   
        print(data)  
        query_df = pd.DataFrame([data]) 
        # [[data['a'],51.0,0,0,1,2,0,166.29,25.600000,1]]
        prediction = model.predict(query_df) 
        print(prediction[0])    
        # {'Prediction': list(prediction)}
        return jsonify(int(prediction[0]))  
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
