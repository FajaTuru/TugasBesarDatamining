from flask import Flask, request, render_template
import pickle
from sklearn.preprocessing import OrdinalEncoder
import numpy as np

app = Flask(__name__)

model_file = open('bankmodel.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', insurance_cost=0)

@app.route('/predict', methods=['POST'])
def predict():
    prediction=int(request.form['prediction'])
    age=int(request.form['age'])
    income=int(request.form['income'])
    children=int(request.form['children'])

    return render_template('index.html', prediction=prediction, age=age, income=income, children=children)


if __name__ == '__main__':
    app.run(debug=True)