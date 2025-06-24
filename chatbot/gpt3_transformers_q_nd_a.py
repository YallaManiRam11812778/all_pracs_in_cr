# # gpt3_transformers_q_nd_a.py
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.settings import Settings
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import SimilarityPostprocessor

Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
Settings.llm = None
Settings.chunk_size = 256
Settings.chunk_overlap = 25

documents = SimpleDirectoryReader("reading_deposit_ledger", recursive=True).load_data()

# store docs into vector DB
index = VectorStoreIndex.from_documents(documents)
# set number of docs to retreive
top_k = 1
# configure retriever
retriever = VectorIndexRetriever(
    index=index,
    similarity_top_k=top_k,
)

# assemble query engine
query_engine = RetrieverQueryEngine(
    retriever=retriever,
    node_postprocessors=[SimilarityPostprocessor(similarity_cutoff=0.5)],
)
     
# query documents
query = "Conference and Meeting Hall details?"
response = query_engine.query(query)
print("\n\n","["*10,"\n",response,"\n","]"*10,"\n\n")
# import sys
# sys.exit()
from transformers import pipeline

# Load the Q&A pipeline
qa_pipeline = pipeline("question-answering")

# for question in questions:
result = qa_pipeline(question=query, context=str(response))
print("\n\n",result,"#"*100,"\n\n")
print(f"Question: {query}")
print(f"Answer: {result['answer']},MMMMMMMMMMMMMMMMMMMMMM\n")