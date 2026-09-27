from flask import Flask, render_template, request, jsonify
import sqlite3
import os
from create_database import DB_PATH, DB_DIR, init_db

app = Flask(__name__)

if not os.path.exists(DB_PATH):
    init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    usn = request.form["usn"]
    dept = request.form["dept"]
    conn = sqlite3.connect(DB_PATH)
    conn.cursor().execute(
        "INSERT INTO students(name, usn, dept) VALUES (?, ?, ?)",
        (name, usn, dept),
    )
    conn.commit()
    conn.close()
    return f'<h2>Registered: {name} | {usn} | {dept}</h2><a href="/">Back</a>'


@app.route("/api/students")
def api_students():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.cursor().execute(
        "SELECT id, name, usn, dept FROM students ORDER BY id DESC"
    ).fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])


@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "registration-service"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
