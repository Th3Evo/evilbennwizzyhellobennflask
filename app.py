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
        slug TEXT UNIQUE NOT NULL,
        name TEXT UNIQUE NOT NULL,
        description TEXT,
        conslength INTEGER
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)    
    conn.commit()
    conn.close()

def initProducts():
    conn = get_db()
    c = conn.cursor()

    products = [
        {
            "slug": "solar",
            "name": "Solar Panels",
        }
    ]





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

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)