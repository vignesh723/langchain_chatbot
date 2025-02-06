from flask import Flask, request, jsonify
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

app = Flask(__name__)

# Load FAISS index safely
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

@app.route("/query", methods=["POST"])
def query_vector_store():
    try:
        user_input = request.json.get("query")  
        if not user_input:
            return jsonify({"error": "Query is required"}), 400

        results = vector_store.similarity_search(user_input, k=3)
        response_texts = [doc.page_content for doc in results]

        return jsonify({"query": user_input, "results": response_texts})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
