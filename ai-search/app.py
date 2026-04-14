from sentence_transformers import SentenceTransformer
import requests

model = SentenceTransformer('all-MiniLM-L6-v2')

data = [
    {"id": 1, "text": "Gym helps to build muscles"},
    {"id": 2, "text": "Protein helps muscle growth"},
    {"id": 3, "text": "Sleep is important for recovery"}
]

for item in data:
    vector = model.encode(item["text"]).tolist()

    requests.post("http://localhost:8000/add", json={
        "id": item["id"],
        "vector": vector,
        "metadata": {"text": item["text"]}
    })

print("Data stored!")

while True:
    query = input("You: ")

    q_vector = model.encode(query).tolist()

    response = requests.post("http://localhost:8000/search", json={
        "vector": q_vector,
        "top_k": 1
    }).json()

    print("Bot:", response[0]["metadata"]["text"])
