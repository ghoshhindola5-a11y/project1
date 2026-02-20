import requests
from app.config import SCALEDOWN_API_KEY

SCALEDOWN_URL = "https://api.scaledown.ai/v1/chat"

def generate_followup(question, history):

    if not SCALEDOWN_API_KEY:
        return question

    headers = {
        "Authorization": f"Bearer {SCALEDOWN_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": f"""
        You are a smart survey chatbot.
        Ask this question conversationally.

        Question: {question}
        User History: {history}
        """,
        "temperature": 0.7
    }

    try:
        response = requests.post(SCALEDOWN_URL, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json().get("response", question)
    except:
        pass

    return question
