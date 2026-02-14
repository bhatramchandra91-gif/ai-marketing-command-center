import requests

# FREE AI API (no key needed for testing)
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

def generate_content(prompt):

    payload = {
        "inputs": f"Write marketing content for: {prompt}"
    }

    response = requests.post(API_URL, json=payload)

    try:
        return response.json()[0]["generated_text"]
    except:
        return "AI error. Try again."

