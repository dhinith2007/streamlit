import streamlit as st

st.title("My First Streamlit App on Vertex 🚀")
st.write("Hello! This app is running on Google Cloud Vertex AI.")

name = st.text_input("Enter your name:")
if st.button("Greet Me"):
    st.success(f"Hello {name}, welcome to my Vertex-hosted app! 🎉")

