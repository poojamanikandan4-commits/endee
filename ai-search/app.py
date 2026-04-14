from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer
import requests

app = Flask(__name__)

model = SentenceTransformer('all-MiniLM-L6-v2')

data = [
    {"id": 1, "text": "Gym helps to build muscles"},
    {"id": 2, "text": "Protein helps muscle growth"},
    {"id": 3, "text": "Sleep is important for recovery"}
]

# Store data
for item in data:
    vector = model.encode(item["text"]).tolist()

    requests.post("http://localhost:8000/add", json={
        "id": item["id"],
        "vector": vector,
        "metadata": {"text": item["text"]}
    })

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    q_vector = model.encode(user_input).tolist()

    response = requests.post("http://localhost:8000/search", json={
        "vector": q_vector,
        "top_k": 1
    }).json()

    return jsonify({"response": response[0]["metadata"]["text"]})

app.run(port=5000)
