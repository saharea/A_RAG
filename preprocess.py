import fitz  # PyMuPDF
import os
import pickle
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    return "\n".join([page.get_text() for page in doc])

def clean_text(text):
    return text.replace('\u200c', '').strip()

def chunk_text(text, chunk_size=500, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_text(text)

def generate_embeddings(chunks, model_name='paraphrase-multilingual-MiniLM-L12-v2'):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(chunks, show_progress_bar=True)
    return embeddings, model

def save_index_and_chunks(chunks, embeddings, index_path, chunks_path):
    faiss_index = faiss.IndexFlatL2(embeddings.shape[1])
    faiss_index.add(embeddings)
    faiss.write_index(faiss_index, index_path)
    with open(chunks_path, 'wb') as f:
        pickle.dump(chunks, f)

if __name__ == "__main__":
    file_path = "data/hsc26_bangla.pdf"
    raw_text = extract_text_from_pdf(file_path)
    cleaned_text = clean_text(raw_text)
    chunks = chunk_text(cleaned_text)
    embeddings, _ = generate_embeddings(chunks)
    save_index_and_chunks(chunks, np.array(embeddings), "data/index.faiss", "data/chunks.pkl")
    print("Preprocessing complete. Index and chunks saved.")
