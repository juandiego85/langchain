from agenticaicourse.rag.data_loader import load_all_documents
from agenticaicourse.rag.vectorstore import FaissVectorStore
from agenticaicourse.rag.search import RAGSearch

#Example usage

if __name__ == "__main__":
    #docs = load_all_documents("rag/data")
    store = FaissVectorStore("rag/data/faiss_store")
    #store.build_from_documents(docs)
    store.load()
    
    rag_search = RAGSearch()
    query= "HOW TO SURVIVE MEMORY POISONING and PROMPT INJECTION for ai agents"
    summary = rag_search.search_and_summarize(query,top_k=3)
    print("Summary",summary)
    

