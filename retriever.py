from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

# Load model and data
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

# Load pre-encoded chunks and FAISS index
with open('data/chunks.pkl', 'rb') as f:
    chunks = pickle.load(f)
faiss_index = faiss.read_index('data/index.faiss')

def retrieve_relevant_chunks(query, k=3):
    query_vector = model.encode([query])
    D, I = faiss_index.search(np.array(query_vector), k)
    return [chunks[i] for i in I[0]]
