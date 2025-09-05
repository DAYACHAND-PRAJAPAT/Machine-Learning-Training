# app.py
from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
import pickle
import numpy as np
import os
from datetime import datetime

app = Flask(__name__)

# # MySQL Configuration - Replace with your actual credentials
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Daya%40123@localhost/breast_cancer_db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# # Create tables on app start
# with app.app_context():
#     db.create_all()

# # Define DB model
# class Prediction(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     timestamp = db.Column(db.DateTime, default=datetime.utcnow)
#     features = db.Column(db.String(500))
#     result = db.Column(db.String(20))

# Load the model
MODEL_PATH = os.path.join("model", "Breast_Cancer_Prediction.lb")
with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form[key]) for key in request.form]
        input_data = np.array([features])
        prediction = model.predict(input_data)[0]
        result = "Benign" if prediction == 1 else "Malignant"

        # # Save to DB
        # pred = Prediction(features=str(features), result=result)
        # db.session.add(pred)
        # db.session.commit()

        return render_template('result.html', result=result)
    except Exception as e:
        return f"Error occurred: {e}"

@app.route('/about')
def about():
    return render_template('about.html')

# @app.route('/history')
# def history():
#     records = Prediction.query.order_by(Prediction.timestamp.desc()).all()
#     return render_template('history.html', records=records)

if __name__ == '__main__':
    app.run(debug=True)
