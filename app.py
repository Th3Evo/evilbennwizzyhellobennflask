from flask import Flask, render_template, session, request, redirect
import sqlite3

app = Flask(__name__)
app.secret_key = "DiddyBlud67"

def get_db():
    db = app.config.get("DATABASE", "rosla_database.db")
    return sqlite3.connect(db, check_same_thread = False)


def init_db():
    conn = get_db()
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        description TEXT,
        conslength INTEGER
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/information")
def information():
    return render_template("information.html")

@app.route("/my-bookings")
def bookings():
    return render_template("my-bookings.html")

if __name__ == "__main__":
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)