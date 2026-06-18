from flask import Flask
import os

app = Flask(__name__)

ENVIRONMENT = os.getenv("ENVIRONMENT", "DEV")

@app.route("/")
def home():
    return f"Hello from {ENVIRONMENT} Environment"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)