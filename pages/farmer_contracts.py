import streamlit as st
from db import connect_db

st.title("📑 Contract Requests")

conn = connect_db()
cur = conn.cursor()

cur.execute("SELECT * FROM contracts")
contracts = cur.fetchall()

for contract in contracts:

    st.write("Farmer:", contract[1])
    st.write("Crop:", contract[2])
    st.write("Industry:", contract[3])
    st.write("Quantity:", contract[4])
    st.write("Price:", contract[5])
    st.write("Status:", contract[6])

    if contract[6] == "Pending":

        if st.button("Approve", key=f"a{contract[0]}"):
            cur.execute(
                "UPDATE contracts SET status='Approved' WHERE id=?",
                (contract[0],)
            )
            conn.commit()
            st.success("Contract Approved")

        if st.button("Reject", key=f"r{contract[0]}"):
            cur.execute(
                "UPDATE contracts SET status='Rejected' WHERE id=?",
                (contract[0],)
            )
            conn.commit()
            st.error("Contract Rejected")

    st.write("---")

conn.close()