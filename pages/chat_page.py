import streamlit as st
from db import connect_db

def show():
    st.title("💬 Chat System")

    sender = st.text_input("Your Name")
    msg = st.text_input("Message")

    if st.button("Send Message"):
        if sender and msg:
            conn = connect_db()
            cur = conn.cursor()
            cur.execute("INSERT INTO chat(sender, message) VALUES(?,?)", (sender, msg))
            conn.commit()
            conn.close()
            st.success("Message Sent!")

    # Display chat messages in a nice card-style layout
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT sender, message FROM chat ORDER BY id DESC")
    messages = cur.fetchall()
    conn.close()

    if messages:
        for s, m in messages:
            st.markdown(f"**💬 {s}:** {m}")
            st.markdown("---")