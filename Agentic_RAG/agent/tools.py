# from rag.rag import load_vector_db

# db = load_vector_db()



# def pdf_search(query):
#     docs = db.similarity_search(query, k=3)
#     return "\n".join([doc.page_content for doc in docs])

from rag.rag import load_vector_db

def pdf_search(query):
    db = load_vector_db()   # load only when needed
    docs = db.similarity_search(query, k=3)
    return "\n".join([doc.page_content for doc in docs])