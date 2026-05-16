import numpy as np

class Reteriver:
    def __init__(self, embedding_model,vector_store):
        self.embedding_model = embedding_model
        self.vector_store = vector_store

    
    def generate(self,query):

        query_emb = self.embedding_model.embed(query)

        if len(query_emb.shape) == 1:
            query_emb = np.expand_dims(query_emb,0)
        
        return self.vector_store.search(query_emb)
        