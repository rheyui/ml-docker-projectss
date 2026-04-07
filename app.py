from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return "ML Model is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    hours = data['hours']
    prediction = model.predict([[hours]])
    return jsonify({'prediction': prediction[0]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)