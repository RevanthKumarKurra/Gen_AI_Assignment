**Similarity Metric Choice**

* For this project, I used cosine similarity instead of Euclidean distance because the objective was to retrieve documents based on semantic meaning. The embeddings generated from transformer models represent meaning through vector direction more than magnitude, so cosine similarity is more effective in identifying semantically related text. Even when two embeddings have different magnitudes, cosine similarity can still recognize them as similar if their directions are close.

* I also found cosine similarity to be more reliable for NLP tasks such as semantic search and question answering. Euclidean distance is more sensitive to vector magnitude, which may not accurately represent semantic relationships in high-dimensional embeddings. Since cosine similarity is widely adopted in modern vector search systems and performs well for text retrieval, it was the most suitable choice for this implementation.

**Migrating to Vertex AI Vector Search (Matching Engine)**

* To move this project into production, I would migrate the current FAISS-based vector search system to Google Vertex AI Vector Search (Matching Engine). While FAISS works well for local development and smaller datasets, Vertex AI provides better scalability, low-latency retrieval, monitoring, and managed infrastructure for large-scale applications.

* The migration process would involve generating embeddings using the same embedding model, storing them in Google Cloud Storage, and creating a Vertex AI index configured with cosine similarity. The index would then be deployed through a Vertex AI endpoint for real-time similarity search. This setup would improve reliability, scalability, and operational management while also making it easier to extend the system in the future with features like hybrid search, metadata filtering, and RAG integration with large language models.