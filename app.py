from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("CKD.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        bp = float(request.form['blood_pressure'])
        urea = float(request.form['blood_urea'])
        hypertension = int(request.form['hypertension'])

        features = np.array([[bp, urea, hypertension]])
        prediction = model.predict(features)[0]

        result = "Chronic Kidney Disease Detected." if prediction == 1 else "Chronic Kidney Disease Not Detected"
        return render_template('index.html', prediction_text=result)
    except Exception as e:
        return render_template('index.html', prediction_text="Invalid input.")

if __name__ == '__main__':
    app.run(debug=True)
