import streamlit as st
from backend.chat import send_message

st.title("Chat")

sender = st.text_input("Your Name")
msg = st.text_input("Message")

if st.button("Send"):

    send_message(sender,msg)

    st.success("Message Sent")