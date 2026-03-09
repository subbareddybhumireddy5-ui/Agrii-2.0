from db import connect_db


def find_matches():

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
    SELECT c.farmer_name, c.crop_name, c.quantity, c.price,
           ct.industry_name, ct.quantity, ct.price
    FROM crops c
    JOIN contracts ct
    ON c.crop_name = ct.crop_name
    WHERE ct.price >= c.price
    """)

    matches = cur.fetchall()

    conn.close()

    return matches