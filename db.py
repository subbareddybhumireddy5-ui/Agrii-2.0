import sqlite3

DB_NAME = "agrilink.db"

def connect_db():
    conn = sqlite3.connect(DB_NAME)
    return conn


def create_tables():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS crops(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        farmer_id INTEGER,
        crop_name TEXT,
        quantity INTEGER,
        price INTEGER,
        location TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS contracts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        farmer_id INTEGER,
        industry_id INTEGER,
        crop TEXT,
        quantity INTEGER
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS chat(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT,
        message TEXT
    )
    """)

    conn.commit()
    conn.close()