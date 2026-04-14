# 🤖 AI Semantic Search Chatbot using Endee

## 📌 Overview
This project is an AI-powered chatbot built using **Endee vector database**.  
It uses **semantic search with embeddings** to understand user queries and return the most relevant answers.

Instead of keyword matching, the chatbot understands the meaning of the query and retrieves the best result.

---

## 🎯 Objective
To demonstrate the use of:
- Vector Databases (Endee)
- Semantic Search
- Retrieval Augmented Generation (RAG)
- AI Chatbot systems

---

## 🚀 Features
- 🔍 Semantic search (meaning-based search)
- ⚡ Fast vector storage using Endee
- 🤖 AI chatbot responses
- 🧠 Embedding-based similarity matching
- 🌐 Simple web UI for interaction

---

## 🧠 How It Works
1. Dataset text is converted into vector embeddings  
2. Embeddings are stored in Endee  
3. User query is converted into embedding  
4. Endee performs similarity search  
5. Top matching result is returned as chatbot response  

---

## 🛠️ Tech Stack
- Python  
- Flask  
- Sentence Transformers  
- Endee (Vector Database)  
- HTML, CSS (UI)  

---

## 🪜 Steps to Build the Project

### 1️⃣ Endee Repository Setup
- Star the Endee repository ⭐  
- Fork the repository 🍴  
- Clone your fork:
```bash
git clone https://github.com/YOUR_USERNAME/endee.git
cd endee
Start Endee server:
npm install
npm start
2️⃣ Create Project Folder
endee/
└── ai-search/

Add files:

ai-search/
 ├── app.py
 ├── index.html
 ├── requirements.txt
 └── README.md
3️⃣ Install Dependencies
pip install sentence-transformers flask requests
4️⃣ Prepare Dataset

Example:

[
  {"id": 1, "text": "Gym helps to build muscles"},
  {"id": 2, "text": "Protein helps muscle growth"},
  {"id": 3, "text": "Sleep is important for recovery"}
]
5️⃣ Store Data in Endee
Convert text into embeddings
Store vectors using Endee API
6️⃣ Semantic Search
Convert user query into embedding
Search similar vectors in Endee
Return best match
7️⃣ Chatbot Functionality
User enters query
System retrieves relevant answer
Displays response
8️⃣ User Interface
Simple web-based chatbot UI
Input box + response display
9️⃣ Demo
📸 Screenshot

🎥 Demo GIF

🔟 Push to GitHub
git add .
git commit -m "Added AI chatbot using Endee"
git push
📂 Project Structure
ai-search/
 ├── app.py
 ├── index.html
 ├── requirements.txt
 ├── README.md
 ├── screenshot.png
 └── demo.gif
📌 Use Cases
AI Chatbots
FAQ systems
Document search
Recommendation systems
⭐ Why Endee?

Endee is used as a vector database to:

Store embeddings efficiently
Perform fast similarity search
Enable semantic retrieval
📌 Result

The chatbot successfully:

Understands user intent
Retrieves relevant answers
Demonstrates semantic search and RAG concept
🔮 Future Improvements
Add advanced UI
Integrate LLM (ChatGPT API)
Add large dataset
Voice-based chatbot
🙌 Conclusion

This project demonstrates how vector databases + embeddings can be used to build intelligent AI systems.
