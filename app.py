from flask import Flask, request, jsonify, render_template
import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

# Load data and model
try:
    data = pd.read_pickle("data.pkl")
    index = faiss.read_index("faiss_index")
    model = SentenceTransformer('all-MiniLM-L6-v2')
except Exception as e:
    print("Error loading model or data:", e)
    data, index, model = None, None, None

def search(query):
    try:
        query_embedding = model.encode([query])
        _, indices = index.search(query_embedding, 5)
        results = data.iloc[indices[0]]
        return results
    except Exception as e:
        print("Error in search function:", e)
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    results = search(user_input)
    if results is not None:
        response = " ".join(results['Content'].tolist())
        return jsonify({"response": response})
    else:
        return jsonify({"response": "I'm sorry, I couldn't find relevant information."})

if __name__ == "__main__":
    app.run(debug=True)
