import requests

def ask_query(query):
    url = "http://localhost:8000/ask/"
    payload = {"query": query}
    response = requests.post(url, json=payload)
    print("Query:", query)
    print("Answer:", response.json()["answer"])

if __name__ == "__main__":
    ask_query("অনুপমের ভাষায় সুপুরুষ কাকে বলা হয়েছে?")
    ask_query("Who is referred to as the deity of fortune by Anupam?")
