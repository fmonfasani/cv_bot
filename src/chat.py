from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from ingest import cargar_vectorstore

def crear_cadena_qa(vectorstore_dir: str = "vectorstore"):
    vectorstore = cargar_vectorstore(vectorstore_dir)
    return RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model="gpt-4", temperature=0),
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )

def preguntar(cadena_qa, pregunta: str):
    return cadena_qa.invoke(pregunta)["result"]


if __name__ == "__main__":
    qa = crear_cadena_qa()
    while True:
        q = input("\n🤔 Pregunta: ")
        if q.lower() in ["salir", "exit", "quit"]:
            break
        print("\n🤖 Respuesta:", preguntar(qa, q))
