from flask import Flask, request, render_template
from predict.predict.run import TextPredictionModel

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')



@app.route("/", methods=['POST'])
def get_prediction():
    model = TextPredictionModel.from_artefacts("train/data/artefacts/2023-01-04-23-23-57")
    text = request.form['text']
    predictions = model.predict([text],top_k=1)
    
    return str(predictions)

@app.route("/predict",methods=["GET"])
def request_prediction():
    model = TextPredictionModel.from_artefacts("train/data/artefacts/2023-01-04-23-23-57")
    text = request.args.get('text')
    predictions = model.predict([text],top_k=1)
    return str(predictions)

if __name__ == '__main__':
    app.run()