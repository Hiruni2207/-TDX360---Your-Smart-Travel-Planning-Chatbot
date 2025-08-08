import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("❌ GROQ_API_KEY not found. Please set it in the .env file.")

# Initialize Groq client
client = Groq(api_key=groq_api_key)

def get_response_from_groq(user_input, chat_history, model="llama3-8b-8192"):
    """
    Send the conversation (chat_history + new message) to Groq API
    and return the assistant's reply.
    """
    messages = [
        {"role": "system", "content": "You are a friendly and creative travel assistant. Help users with destinations, hotels, itineraries, travel tips, and budget advice."}
    ]

    # Add past conversation
    for sender, msg in chat_history:
        role = "user" if sender == "You" else "assistant"
        messages.append({"role": role, "content": msg})

    # Add latest user input
    messages.append({"role": "user", "content": user_input})

    # Call Groq API
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=500,
        temperature=0.8
    )

    return response.choices[0].message.content


