import streamlit as st
import google.generativeai as genai
API_KEY = "AIzaSyAF9LD3YkUwPX9ZvxLNJNacNknDCzU-fAs"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
if "chat" not in st.session_state:
  st.session_state.chat=model.start_chat(history=[])
st.title("Chatbot - your  ai assistant ")
st.write("Welcome to the my chatbot! How can i help you?")
if "messages" not in st.session_state:
  st.session_state.messages=[]
for messages in st.session_state.messages:
  with st.chat_messages(messages["role"]):
    st.markdown(message["content"])
if prompt := st.chat_input("Say something..."):
  st.session_state.messages.append({"role": "user","content" : prompt})
  with st.chat_message("user"):
    st.markdown(prompt)
  response = st.session_state.chat.send_message(prompt)
  st.session_state.messages.append({"role": "assistant","content" : response.text})
  with st.chat_message("assistant"):
    st.markdown(response.text)
