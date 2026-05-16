from src.embedding import EmbeddingModel
from src.vector_db import VectorStore
from src.reteriver import Reteriver
from src.eval_reterover import MockRetriver

result = []


with open("./data/python_oops_complete_guide.txt","r",encoding="utf-8") as f:
    text = f.read()

text = [i for i in text.split(sep="\n") if i != ""]

embedding_model = EmbeddingModel()
embeddings_list = embedding_model.embed(text)

vector_store = VectorStore(dimension=384)
vector_store.add(embeddings_list,text)

mockretriver = MockRetriver()
retriver = Reteriver(embedding_model,vector_store)


while True:

    query = input("Ask Me.....")

    if query.lower() in ["exit","leave","stop"]:
        break

    retrived_ans = retriver.generate(query)

    mockretrived_ans = mockretriver.generate(query,retrived_ans)

    result.append(
        {"Query":query,
        "Reterived Answer":retrived_ans,
        "Evalved Retervied Answer":mockretrived_ans})
    

print(result)
