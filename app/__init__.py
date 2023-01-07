from flask import Flask, request, render_template
from predict.predict.run import TextPredictionModel
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/", methods=['POST'])
def predict_input():
    # Load the TextPredictionModel object from the specified artefacts file
    model = TextPredictionModel.from_artefacts("train/data/artefacts/2023-01-04-23-23-57")
    
    # Retrieve the text from the request form data
    text = request.form['text']
    
    # Use the model to make a prediction on the text, with a top-k value of 1
    predictions = model.predict([text], top_k=1)
    
    # Return the predictions as a string
    return str(predictions)

@app.route("/predict", methods=['POST'])
def predict_post():
    # Load the request data as a JSON object
    request_data = json.loads(request.get_data())
    
    # Retrieve the text list and top-k value from the request data
    text = request_data['text']
    top_k = request_data['top_k']
    
    # Load the TextPredictionModel object from the specified artefacts file
    model = TextPredictionModel.from_artefacts("train/data/artefacts/2023-01-04-23-23-57")
    
    # Use the model to make predictions on the text list, with the specified top-k value
    predictions = model.predict(text, top_k=top_k)
    
    # Return the predictions as a string
    return str(predictions)


if __name__ == '__main__':
    app.run()