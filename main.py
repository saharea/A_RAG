from fastapi import FastAPI, Request
from retriever import retrieve_relevant_chunks
from generator import generate_answer

app = FastAPI()

@app.post("/ask/")
async def ask_question(request: Request):
    data = await request.json()
    query = data['query']
    chunks = retrieve_relevant_chunks(query)
    answer = generate_answer(query, chunks)
    return {"answer": answer}
