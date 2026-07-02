from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("crop_model.pkl")

crop_names = [
    'apple','banana','blackgram','chickpea','coconut','coffee',
    'cotton','grapes','jute','kidneybeans','lentil','maize',
    'mango','mothbeans','mungbean','muskmelon','orange',
    'papaya','pigeonpeas','pomegranate','rice','watermelon'
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    N = float(request.form["N"])
    P = float(request.form["P"])
    K = float(request.form["K"])
    temperature = float(request.form["temperature"])
    humidity = float(request.form["humidity"])
    ph = float(request.form["ph"])
    rainfall = float(request.form["rainfall"])

    data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

    prediction = model.predict(data)

    result = crop_names[int(prediction[0])]

    return render_template("result.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
