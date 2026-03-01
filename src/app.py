
import streamlit as st
from google import genai
from google.genai import types
from dotenv import load_dotenv
from config import GEMINI_API_KEY

load_dotenv()
client = genai.Client(api_key=GEMINI_API_KEY)

st.title("🤖 GeminiBot")

st.write("Hello! I'm GeminiBot, your personal assistant. How can I help you today?")

chat = client.chats.create(model="gemini-2.5-flash")

if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = chat.send_message(prompt)
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})