import os
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

def cargar_y_dividir_documento(path_txt: str, chunk_size: int = 500, chunk_overlap: int = 100):
    loader = TextLoader(path_txt)
    documentos = loader.load()
    splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(documentos)

def generar_vectorstore(documentos, persist_path: str = "vectorstore"):
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(documentos, embeddings)
    db.save_local(persist_path)
    print(f"✅ Vectorstore guardado en '{persist_path}'")

def cargar_vectorstore(persist_path: str = "vectorstore"):
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local(persist_path, embeddings, allow_dangerous_deserialization=True)

if __name__ == "__main__":
    documentos = cargar_y_dividir_documento("data/cv_prompt_eng.txt")
    generar_vectorstore(documentos)
