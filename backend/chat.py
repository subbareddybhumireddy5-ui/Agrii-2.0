from db import connect_db

def send_message(sender, message):

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO chat(sender, message) VALUES(?, ?)",
        (sender, message)
    )

    conn.commit()
    conn.close()


def get_messages():

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT sender, message FROM chat ORDER BY id")

    messages = cur.fetchall()

    conn.close()

    return messages