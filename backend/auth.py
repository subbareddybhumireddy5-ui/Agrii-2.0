from db import connect_db

def register_user(name,email,password,role):

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users(name,email,password,role) VALUES(%s,%s,%s,%s)",
        (name,email,password,role)
    )

    conn.commit()
    conn.close()


def login_user(email,password):

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE email=%s AND password=%s",
        (email,password)
    )

    user = cur.fetchone()
    conn.close()

    return user