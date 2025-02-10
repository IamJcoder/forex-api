from flask import Flask, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Forex API is running!"})

if __name__ == '__main__':
    app.run(debug=True)
