from db import connect_db


def get_price_recommendation(crop):

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "SELECT AVG(price) FROM crops WHERE crop_name=?",
        (crop,)
    )

    result = cur.fetchone()

    conn.close()

    if result and result[0]:
        return round(result[0], 2)
    else:
        return None