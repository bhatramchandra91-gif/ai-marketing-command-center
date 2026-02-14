import requests

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

def generate_strategy(business, city, budget):

    prompt = f"""
    Create marketing strategy for {business} in {city} with budget {budget}.
    Include ads, reels, and lead generation.
    """

    response = requests.post(API_URL, json={"inputs": prompt})

    try:
        return response.json()[0]["generated_text"]
    except:
        return "Strategy generation failed"

