import sqlite3

DB_NAME = "agrilink.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = connect_db()
    cur = conn.cursor()

    # Users table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    # Crops table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS crops(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        farmer_name TEXT,
        crop_name TEXT,
        quantity INTEGER,
        price REAL,
        location TEXT
    )
    """)
    # Add 'image' column if missing
    try:
        cur.execute("ALTER TABLE crops ADD COLUMN image TEXT")
    except sqlite3.OperationalError:
        pass  # Column already exists

    # Contracts table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS contracts(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        farmer_name TEXT,
        crop_name TEXT,
        industry_name TEXT,
        quantity INTEGER,
        price REAL,
        status TEXT
    )
    """)

    # Chat table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS chat(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT,
        message TEXT
    )
    """)

    conn.commit()
    conn.close()