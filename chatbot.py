import streamlit as st
import google.generativeai as genai

# Configure Gemini with your API key
genai.configure(api_key="AIzaSyAirGKFXwyaMurrXF1K8ZAFcUwoUN7LqyE")

# Load the Gemini model
model = genai.GenerativeModel('gemini-2.0-flash-exp')

# Streamlit UI
st.title("💬 Gemini AI Chatbot")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", key="user_input")

if st.button("Send"):
    if user_input:
        # Show user message
        st.session_state.chat_history.append(("You", user_input))

        # Generate response from Gemini
        response = model.generate_content(user_input)
        bot_reply = response.text

        # Show bot reply
        st.session_state.chat_history.append(("Gemini", bot_reply))

# Display chat history
for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
