from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    exp = float(request.form["experience"])
    
    prediction = model.predict(np.array([[exp]]))[0]
    
    return render_template("index.html", prediction_text=f"Estimated Salary: ₹{round(prediction,2)}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)