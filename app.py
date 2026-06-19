from flask import Flask
import os

app = Flask(__name__)

ENVIRONMENT = os.getenv("ENVIRONMENT", "DEV")

@app.route("/")
def home():
    return {
    "environment": os.getenv("APP_ENV"),
    "message": os.getenv("WELCOME_MESSAGE"),
    "debug": os.getenv("DEBUG"),
    "deployment_test": "DEV Deployment Test"
}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)