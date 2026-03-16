import streamlit as st
import requests

st.title("Domain Adapted AI Assistant")

question = st.text_input("Ask a question")

if st.button("Submit"):

    r = requests.get(
        "http://localhost:8000/ask",
        params={"question": question}
    )

    st.write(r.json()["response"])
