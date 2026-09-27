from flask import Flask, render_template, jsonify
import requests
import os

app = Flask(__name__)

REGISTRATION_SERVICE_URL = os.environ.get(
    "REGISTRATION_SERVICE_URL", "http://registration-service:5000"
)


@app.route("/")
def home():
    students = []
    error = None
    try:
        resp = requests.get(f"{REGISTRATION_SERVICE_URL}/api/students", timeout=3)
        resp.raise_for_status()
        students = resp.json()
    except requests.exceptions.RequestException:
        error = "Could not reach the Registration Service right now. Please try again shortly."
    return render_template("records.html", students=students, error=error)


@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "records-service"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
