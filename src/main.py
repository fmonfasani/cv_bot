import os
from dotenv import load_dotenv

from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

# 🧪 Cargar variables de entorno
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("❌ No se encontró la API KEY. Agregala al archivo .env como OPENAI_API_KEY")

# 📄 Cargar el CV desde archivo
def cargar_documento(ruta):
    loader = TextLoader(ruta)
    documentos = loader.load()
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.split_documents(documentos)

# 🧠 Crear base de conocimiento vectorial
def crear_vectorstore(documentos):
    embeddings = OpenAIEmbeddings()
    return Chroma.from_documents(documentos, embeddings, persist_directory="./chroma_db")

# 🔍 Crear cadena de recuperación y respuesta
def crear_cadena_retrieval(vectorstore):
    return RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model="gpt-4", temperature=0),
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )

# 🚀 Loop interactivo
def ejecutar_chat(cadena):
    print("🧠 ¡Preguntale a tu CV! (escribí 'salir' para terminar)")
    while True:
        query = input("\n> Tu pregunta: ")
        if query.lower() in ["salir", "exit", "quit"]:
            print("👋 ¡Hasta la próxima!")
            break
        respuesta = cadena.run(query)
        print(f"\n🤖 Respuesta:\n{respuesta}")

# 🔁 Ejecución principal
if __name__ == "__main__":
    docs = cargar_documento("data/cv_prompt_eng.txt")
    db = crear_vectorstore(docs)
    qa = crear_cadena_retrieval(db)
    ejecutar_chat(qa)
