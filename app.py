from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🌾 OptiCrop</h1>
    <h2>Smart Agricultural Production Optimization Engine</h2>
    <p>Welcome to the OptiCrop Crop Recommendation System.</p>
    <p>This application recommends the most suitable crop based on soil and environmental conditions.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
