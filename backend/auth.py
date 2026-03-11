from db import connect_db


def register_user(name, email, password, role):

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users(name,email,password,role) VALUES(?,?,?,?)",
        (name, email, password, role)
    )

    conn.commit()
    conn.close()


def login_user(email, password):

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "SELECT id, name, email, role FROM users WHERE email=? AND password=?",
        (email, password)
    )

    row = cur.fetchone()
    conn.close()

    if row:
        return {
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "role": row[3]
        }

    return None