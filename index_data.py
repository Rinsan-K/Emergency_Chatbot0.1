from sentence_transformers import SentenceTransformer
import faiss
import pandas as pd

# Load the dataset
data = pd.read_csv('emergency_preparedness.csv')  # Ensure file path is correct and 'Content' column exists

# Initialize the transformer model for embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

# Encode all content entries
embeddings = model.encode(data['Content'].tolist())

# Build the FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Save index and data
faiss.write_index(index, "faiss_index")
data.to_pickle("data.pkl")

print("Index and data files have been saved successfully.")
