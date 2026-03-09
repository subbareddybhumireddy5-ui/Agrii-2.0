from db import connect_db

def send_message(sender,message):

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO chat(sender,message) VALUES(%s,%s)",
        (sender,message)
    )

    conn.commit()
    conn.close()