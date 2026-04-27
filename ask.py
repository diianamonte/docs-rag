import sys
from dotenv import load_dotenv
from src.context_loader import load_context
from src.llm_client import ask_llm


def main():
    # Cargo variables de entorno (.env)
    load_dotenv()
    
    # Validación de argumentos
    if len(sys.argv) < 2:
        print("Uso: python ask.py \"<tu pregunta>\"")
        print("Ejemplo: python ask.py \"¿qué es BIN Sponsorship?\"")
        sys.exit(1)
    
    question = sys.argv[1]
    
    # Cargo el contexto
    try:
        context = load_context()
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
    
    print(f"\n📝 Pregunta: {question}\n")
    print("⏳ Consultando al modelo...\n")
    
    # Consulto al LLM
    result = ask_llm(question, context)
    response = result["response"]
    
    # Imprimo la respuesta
    print("=" * 60)
    print(f"💬 Respuesta:\n{response.answer}\n")
    
    if response.citations:
        print(f"📚 Citas: {', '.join(response.citations)}")
    else:
        print(f"📚 Citas: (ninguna)")
    
    print(f"🎯 Confianza: {response.confidence}")
    print(f"✅ En scope: {response.in_scope}")
    print("=" * 60)
    
    # Métricas
    print(f"\n📊 Métricas:")
    print(f"   Tokens input: {result['tokens_input']}")
    print(f"   Tokens output: {result['tokens_output']}")
    print(f"   Latencia: {result['latency_seconds']}s")
    print(f"   Intentos: {result['attempts']}")
    
    if "error" in result:
        print(f"   ⚠️  Error: {result['error']}")


if __name__ == "__main__":
    main()