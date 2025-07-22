import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_answer(query, retrieved_chunks):
    context = "\n".join(retrieved_chunks)
    prompt = f"Context:\n{context}\n\nQuestion:\n{query}\n\nAnswer:"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()
