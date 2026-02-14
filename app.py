from fastapi import FastAPI
from ai.content_ai import generate_content
from ai.strategy_ai import generate_strategy
from ai.proposal_ai import create_proposal
from crm.crm_store import add_client, get_clients

app = FastAPI(title="AI Marketing Command Center")

@app.get("/")
def home():
    return {"status": "AI Marketing Command Center Running"}

# content generator
@app.get("/generate_content")
def content(prompt: str):
    return {"result": generate_content(prompt, "social media")}

# strategy generator
@app.get("/strategy")
def strategy(business: str, city: str, budget: str):
    return {"strategy": generate_strategy(business, city, budget)}

# proposal generator
@app.get("/proposal")
def proposal(client: str, service: str, price: str):
    file = create_proposal(client, service, price)
    return {"proposal_created": file}

# add client
@app.get("/add_client")
def add(name: str, business: str):
    return add_client(name, business)

# view clients
@app.get("/clients")
def clients_list():
    return get_clients()
