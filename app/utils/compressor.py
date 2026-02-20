COMPRESSED_QUESTIONS = [
    {"id": 1, "q": "How satisfied are you with our service?"},
    {"id": 2, "q": "What can we improve?"},
    {"id": 3, "q": "Would you recommend us to others? Why?"}
]

def get_question(index: int):
    if index < len(COMPRESSED_QUESTIONS):
        return COMPRESSED_QUESTIONS[index]["q"]
    return None

def total_questions():
    return len(COMPRESSED_QUESTIONS)
