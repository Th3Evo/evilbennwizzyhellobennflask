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
        ("solar", "Solar Panels", "High-efficiency solar panels for residential and commercial use.", 12),
        ("EV", "EV Charging Stations", "Durable EV charging stations for sustainable energy generation.", 6),
        ("EMS", "Energy Management Systems", "Advanced energy management systems for optimizing power consumption.", 3),
    ]

    c.executemany("""
        INSERT OR IGNORE INTO products (slug, name, description, conslength)
        VALUES (?, ?, ?, ?)
    """, products)

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/products")
def products():
    conn = get_db()
    c = conn.cursor()

    c.execute("SELECT slug, name, description FROM products")
    products = c.fetchall()

    conn.close()
    return render_template("products.html", products=products)


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
    initProducts()
    app.run(debug=True)