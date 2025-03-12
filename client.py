import streamlit as st
import requests

st.title("GenieMind - Research & Writing Assistant")

# Sidebar navigation
option = st.sidebar.radio("Choose a feature", ["Essay", "Poem", "Chatbot", "Amazon Search", "Image Analysis"])

# Essay Generator
if option == "Essay":
    topic = st.text_input("Enter your essay topic:")
    if topic:
        response = requests.post("http://localhost:8000/essay", json={"topic": topic})
        result = response.json()
        if "output" in result:
            st.write(result["output"]["content"])
        else:
            st.write("Error: No output found in the response.")

# Poem Generator
elif option == "Poem":
    topic = st.text_input("Enter your poem topic:")
    if topic:
        response = requests.post("http://localhost:8000/poem", json={"topic": topic})
        result = response.json()
        if "output" in result:
            st.write(result["output"]["content"])
        else:
            st.write("Error: No output found in the response.")

# Personality Chatbot
elif option == "Chatbot":
    question = st.text_input("Ask a question to Donald Trump:")
    if question:
        response = requests.post("http://localhost:8000/chat", json={"question": question})
        result = response.json()
        if "output" in result:
            st.write(result["output"]["content"])
        else:
            st.write("Error: No output found in the response.")

# Amazon Search
elif option == "Amazon Search":
    query = st.text_input("Ask about Amazon products:")
    if query:
        response = requests.post("http://localhost:8000/search", json={"question": query})
        result = response.json()
        if "output" in result:
            st.write(result["output"])
        else:
            st.write("Error: No output found in the response.")

# Image Analysis
elif option == "Image Analysis":
    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpeg", "jpg"])
    prompt = st.text_input("Describe what you want to know about the image:")
    if uploaded_file and prompt:
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://localhost:8000/analyze-image", files=files, params={"prompt": prompt})
        result = response.json()
        if "output" in result:
            st.write(result["output"])
        else:
            st.write("Error: No output found in the response.")