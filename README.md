# ✈️ TDX360 Travel Chatbot

A travel-focused AI chatbot built using **Python**, **Streamlit**, and the **Groq API**.  
It helps travelers with destination recommendations, hotel suggestions, itinerary planning, and budget travel tips — all through an easy-to-use interactive chat interface.

---

## 📌 Features

- 🗺 **Plan Itineraries** – Create detailed travel plans instantly.
- 🏨 **Find Hotels** – Search for hotels within your budget.
- ☀️ **Best Time to Visit** – Get the optimal travel seasons for any destination.
- 💰 **Budget Travel Tips** – Receive money-saving advice for your trip.
- 💬 **Interactive Chat Interface** – Ask any travel-related question.
- ⚙️ **Model Choice** – Switch between `llama3-8b-8192` and `mixtral-8x7b-32768`.

---

## 🛠 Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Backend AI:** [Groq API](https://groq.com/)
- **Environment Variables:** [python-dotenv](https://pypi.org/project/python-dotenv/)
- **Language:** Python 3.x

---

## 📂 Project Structure

**Folder/Files Explanation:**
- **`app.py`** → Handles the Streamlit interface, quick option buttons, and chat display.  
- **`chatbot.py`** → Contains the function to send and receive messages from Groq API.  
- **`requirements.txt`** → All required Python packages for running the project.  
- **`.env`** → Stores sensitive API keys (never push this file to GitHub).  
- **`.gitignore`** → Ensures sensitive or unnecessary files are not tracked by Git.  
- **`README.md`** → Documentation for the project (this file).  

---

## 🚀 Model Deployment

The **TDX360 Travel Chatbot** is deployed using **Streamlit Community Cloud** and powered by **Groq API** for AI responses.

This project does not require hosting a separate AI model server — it uses the **Groq API** to run powerful LLMs in the cloud.  
The chatbot is deployed on **Streamlit Cloud**, which serves as both the **frontend** and the **backend**.

---

### 📦 Deployment Architecture

- **User**: Enters a travel-related query or selects a quick option.
- **Streamlit UI (Frontend + Backend)**: `app.py` manages the interface and passes messages to the backend.
- **Groq API**: Handles requests and sends them to the chosen AI model.
- **AI Model (Cloud)**: Processes the request using `llama3-8b-8192` or `mixtral-8x7b-32768`.
- **Response**: The generated answer is returned to the Streamlit app and displayed in the chat.


1. **Streamlit UI & Backend**  
   - `app.py` handles the chatbot interface, quick travel buttons, and chat history.
   - `chatbot.py` sends user messages to Groq API and retrieves AI-generated travel responses.

2. **Groq API Models**  
   - **llama3-8b-8192** → Fast and cost-efficient, ideal for most queries.  
   - **mixtral-8x7b-32768** → Handles larger context windows for long conversations.  

3. **Environment Variables**  
   - API key stored in `.env` file locally.
   - On Streamlit Cloud, the key is stored in **Secrets** for security.

---

### 🌍 Live Application
You can access the chatbot here:  
🔗 **[TDX360 Travel Chatbot](https://4xkfeahyi9bzsmnfiex4bh.streamlit.app/)**



