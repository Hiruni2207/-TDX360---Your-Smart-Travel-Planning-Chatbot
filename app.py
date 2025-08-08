import streamlit as st
from chatbot import get_response_from_groq

# ---------------- UI CONFIG ----------------
st.set_page_config(page_title="TDX360 Travel Chatbot", page_icon="✈️", layout="centered")
st.markdown("<h1 style='text-align:center;'>✈️ TDX360 Travel Chatbot</h1>", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "model_choice" not in st.session_state:
    st.session_state.model_choice = "llama3-8b-8192"

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("⚙️ Settings")
    st.session_state.model_choice = st.selectbox("Choose AI Model", ["llama3-8b-8192", "mixtral-8x7b-32768"])
    if st.button("🗑 Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

# ---------------- QUICK BUTTONS ----------------
st.subheader("Quick Travel Options")
cols = st.columns(4)
with cols[0]:
    if st.button("🗺 Plan Itinerary"):
        st.session_state.chat_history.append(("You", "Plan a 5-day itinerary for Paris."))
        st.session_state.chat_history.append(("Bot", get_response_from_groq("Plan a 5-day itinerary for Paris.", st.session_state.chat_history, st.session_state.model_choice)))
        st.rerun()
with cols[1]:
    if st.button("🏨 Find Hotels"):
        st.session_state.chat_history.append(("You", "Find good hotels in Tokyo under $100/night."))
        st.session_state.chat_history.append(("Bot", get_response_from_groq("Find good hotels in Tokyo under $100/night.", st.session_state.chat_history, st.session_state.model_choice)))
        st.rerun()
with cols[2]:
    if st.button("☀️ Best Time to Visit"):
        st.session_state.chat_history.append(("You", "What is the best time to visit Bali?"))
        st.session_state.chat_history.append(("Bot", get_response_from_groq("What is the best time to visit Bali?", st.session_state.chat_history, st.session_state.model_choice)))
        st.rerun()
with cols[3]:
    if st.button("💰 Budget Tips"):
        st.session_state.chat_history.append(("You", "Give me budget travel tips for Europe."))
        st.session_state.chat_history.append(("Bot", get_response_from_groq("Give me budget travel tips for Europe.", st.session_state.chat_history, st.session_state.model_choice)))
        st.rerun()

# ---------------- USER INPUT ----------------
user_input = st.text_input("Ask me anything about travel:")

if st.button("Send"):
    if user_input:
        with st.spinner("Thinking..."):
            response = get_response_from_groq(user_input, st.session_state.chat_history, st.session_state.model_choice)
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("Bot", response))
        st.rerun()

# ---------------- DISPLAY CHAT ----------------
st.markdown("<hr>", unsafe_allow_html=True)
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(
            f"""
            <div style='background-color:#4A90E2; color:white; padding:10px; 
            border-radius:12px; margin-bottom:8px; max-width:80%;'>
                <b>{sender}:</b> {message}
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style='background-color:#FFFFFF; color:#000000; padding:10px; 
            border:1px solid #ccc; border-radius:12px; margin-bottom:8px; max-width:80%;'>
                <b>{sender}:</b> {message}
            </div>
            """,
            unsafe_allow_html=True
        )



