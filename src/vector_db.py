import faiss
import numpy as np

class VectorStore:
    def __init__(self, dimension):
        self.index = faiss.IndexFlatIP(dimension)
        self.documents = []

    def add(self, embeddings, docs):
        faiss.normalize_L2(embeddings)
        self.index.add(np.array(embeddings, dtype=np.float32))
        self.documents.extend(docs)

    def search(self, query_embedding, top_k=3):
        faiss.normalize_L2(query_embedding)
        scores, indices = self.index.search(
            np.array(query_embedding, dtype=np.float32),
            top_k
        )

        results = []
        for idx, score in zip(indices[0], scores[0]):
            results.append({
                "document": self.documents[idx],
                "score": float(score)
            })

        return results