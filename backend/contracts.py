from db import connect_db

def create_contract(farmer_id,industry_id,crop,quantity):

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO contracts(farmer_id,industry_id,crop,quantity) VALUES(%s,%s,%s,%s)",
        (farmer_id,industry_id,crop,quantity)
    )

    conn.commit()
    conn.close()