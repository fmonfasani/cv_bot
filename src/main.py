from utils import cargar_api_key
from chat import crear_cadena_qa, preguntar

def run():
    cargar_api_key()  # Carga y valida la clave
    cadena = crear_cadena_qa()

    print("\n🧠 Preguntale a tu CV — Escribí 'salir' para terminar")
    while True:
        query = input("\n👉 Tu pregunta: ")
        if query.lower() in ["salir", "exit", "quit"]:
            print("👋 ¡Hasta la próxima!")
            break
        respuesta = preguntar(cadena, query)
        print(f"\n🤖 Respuesta: {respuesta}")

if __name__ == "__main__":
    run()
