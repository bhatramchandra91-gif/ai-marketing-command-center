clients = []

def add_client(name, business):
    clients.append({"name": name, "business": business})
    return {"message": "Client added"}

def get_clients():
    return clients
