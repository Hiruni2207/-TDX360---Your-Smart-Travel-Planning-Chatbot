# ✈️ TDX360 Travel Chatbot

A travel-focused AI chatbot built using **Python**, **Streamlit**, and the **Groq API**.  
It helps travelers with destination recommendations, hotel suggestions, itinerary planning, and budget travel tips — all through an easy-to-use interactive chat interface.

---

## Features

-  **Plan Itineraries** – Create detailed travel plans instantly.
-  **Find Hotels** – Search for hotels within your budget.
-  **Best Time to Visit** – Get the optimal travel seasons for any destination.
-  **Budget Travel Tips** – Receive money-saving advice for your trip.
-  **Interactive Chat Interface** – Ask any travel-related question.
-  **Model Choice** – `llama-3.1-8b-instant`.

---

## Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Backend AI:** [Groq API](https://groq.com/)
- **Environment Variables:** [python-dotenv](https://pypi.org/project/python-dotenv/)
- **Language:** Python 3.x

---

## Project Structure

**Folder/Files Explanation:**
- **`app.py`** → Handles the Streamlit interface, quick option buttons, and chat display.  
- **`chatbot.py`** → Contains the function to send and receive messages from Groq API.  
- **`requirements.txt`** → All required Python packages for running the project.  
- **`.env`** → Stores sensitive API keys (never push this file to GitHub).  
- **`.gitignore`** → Ensures sensitive or unnecessary files are not tracked by Git.  
- **`README.md`** → Documentation for the project (this file).  

---
## How to Run the Code Locally

Follow these steps to set up and run the TDX360 Travel Chatbot on our machine:

### 1️. Clone the Repository
bash
git clone https://github.com/Hiruni2207/-TDX360---Your-Smart-Travel-Planning-Chatbot.git
cd tdx360-travel-chatbot

### 2️. Create a Virtual Environment 
bash
python -m venv venv

Activate the environment
- **Windows**:
venv\Scripts\activate
- **Mac/Linux**:
source venv/bin/activate

### 3️. Install Dependencies
pip install -r requirements.txt

### 4️. Set Up Environment Variables
GROQ_API_KEY=our_groq_api_key_here
(You can get an API key through this site- [Groq API](https://groq.com/))

### 5️. Run the Application
bash

streamlit run app.py

### 6️. Access the App
Once the app starts, Streamlit will display a local URL (e.g., http://localhost:8501) in the terminal.
Open it in your browser to start chatting.

---

## Model Deployment

The **TDX360 Travel Chatbot** is deployed using **Streamlit Community Cloud** and powered by **Groq API** for AI responses.

This project does not require hosting a separate AI model server — it uses the **Groq API** to run powerful LLMs in the cloud.  
The chatbot is deployed on **Streamlit Cloud**, which serves as both the **frontend** and the **backend**.

---

## Deployment Architecture

- **User**: Enters a travel-related query or selects a quick option.
- **Streamlit UI (Frontend + Backend)**: `app.py` manages the interface and passes messages to the backend.
- **Groq API**: Handles requests and sends them to the chosen AI model.
- **AI Model (Cloud)**: Processes the request using `llama-3.1-8b-instant`.
- **Response**: The generated answer is returned to the Streamlit app and displayed in the chat.


1. **Streamlit UI & Backend**  
   - `app.py` handles the chatbot interface, quick travel buttons, and chat history.
   - `chatbot.py` sends user messages to Groq API and retrieves AI-generated travel responses.

2. **Groq API Models**  
   - **llama-3.1-8b-instant** → Fast and cost-efficient, ideal for most queries.  

3. **Environment Variables**  
   - API key stored in `.env` file locally.
   - On Streamlit Cloud, the key is stored in **Secrets** for security.

---

## Live Application
You can access the chatbot here:  
🔗 **[TDX360 Travel Chatbot](https://4xkfeahyi9bzsmnfiex4bh.streamlit.app/)**

---


