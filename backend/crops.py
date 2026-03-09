from db import connect_db

def add_crop(farmer_id,crop,quantity,price,location):

    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO crops(farmer_id,crop_name,quantity,price,location) VALUES(%s,%s,%s,%s,%s)",
        (farmer_id,crop,quantity,price,location)
    )

    conn.commit()
    conn.close()