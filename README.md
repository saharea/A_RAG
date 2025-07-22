# A_RAG# RAG Bangla Bot

A bilingual Retrieval-Augmented Generation (RAG) system for Bangla and English queries on HSC Bangla 1st Paper.

## 🧰 Features
- Bangla + English query understanding
- Contextual document retrieval
- GPT-based answer generation
- REST API with FastAPI

## 🛠 Setup

```bash
git clone https://github.com/yourname/rag-bangla-bot.git
cd rag-bangla-bot
pip install -r requirements.txt
export OPENAI_API_KEY=your_openai_key
uvicorn main:app --reload
```

## 🧪 Sample Queries

```bash
curl -X POST "http://localhost:8000/ask/" \
     -H "Content-Type: application/json" \
     -d '{"query":"অনুপমের ভাষায় সুপুরুষ কাকে বলা হয়েছে?"}'
```

## 📁 Folder Structure

```
rag-bangla-bot/
├── main.py
├── retriever.py
├── generator.py
├── data/
│   └── hsc26_bangla.pdf
├── requirements.txt
└── README.md
```

## 📌 Evaluation
- Groundedness: Answer supported by context
- Relevance: Cosine similarity match score


## ⚙️ Preprocessing

Run this once to prepare the FAISS index and chunks.

```bash
python preprocess.py
```

## 🧪 API Testing

You can test the API using the provided script:

```bash
python client.py
```
