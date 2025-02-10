from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Forex API is running!"})

@app.route("/latest-rates")
def get_latest_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"  # Use a forex API provider
    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch forex data"}), 500

if __name__ == "__main__":
    app.run(debug=True)
