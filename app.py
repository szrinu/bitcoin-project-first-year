# app.py

from flask import Flask, render_template, request
import data_analysis
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route(action="/predict", methods=["POST"])
def predict():
    if request.method == 'POST':
        # Get data from form
        input_data = request.form['input_data']
    
        # Read CSV file 

        
          # Corrected

        
        
        # Call the prediction function from data_analysis.py
        prediction_result = data_analysis # Assuming there's a function named predict
        
        # Pass the prediction result to the template
        return render_template('predict.html', prediction_result=prediction_result)

if __name__ == '__main__':
    app.run(debug=True)
