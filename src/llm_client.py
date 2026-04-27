import os
import json
import time
from typing import Optional
from groq import Groq
from pydantic import ValidationError
from src.schemas import RAGResponse
from src.prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE


# Cliente global de Groq
_client: Optional[Groq] = None


def get_client() -> Groq:
    """Lazy initialization del cliente Groq."""
    global _client
    if _client is None:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY no encontrada en variables de entorno")
        _client = Groq(api_key=api_key)
    return _client


def ask_llm(
    question: str,
    context: str,
    model: str = "llama-3.3-70b-versatile",
    max_retries: int = 2
) -> dict:
    """
    Consulta el LLM con la pregunta y contexto, valida la respuesta con Pydantic.
    
    Args:
        question: pregunta del usuario
        context: documentación a usar como base
        model: modelo a usar
        max_retries: cuántas veces reintentar si la validación falla
    
    Returns:
        dict con: response (RAGResponse), tokens, latency_seconds
    """
    client = get_client()
    user_prompt = USER_PROMPT_TEMPLATE.format(
        context=context,
        question=question
    )
    
    last_error = None
    
    for attempt in range(max_retries + 1):
        start_time = time.time()
        
        try:
            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.1,
                response_format={"type": "json_object"},
            )
            
            latency = time.time() - start_time
            raw_response = completion.choices[0].message.content
            
            # Parseamos el JSON
            parsed = json.loads(raw_response)
            
            # Validamos con Pydantic
            validated = RAGResponse(**parsed)
            
            return {
                "response": validated,
                "tokens_input": completion.usage.prompt_tokens,
                "tokens_output": completion.usage.completion_tokens,
                "latency_seconds": round(latency, 2),
                "attempts": attempt + 1,
            }
            
        except (json.JSONDecodeError, ValidationError) as e:
            last_error = e
            print(f"⚠️  Intento {attempt + 1} falló: {type(e).__name__}")
            if attempt < max_retries:
                print(f"   Reintentando...")
                continue
        
        except Exception as e:
            # Cualquier otro error (network, API, etc.) → no reintenta
            raise
    
    # Si llegamos acá, todos los reintentos fallaron → fallback
    return {
        "response": RAGResponse(
            answer="Hubo un error procesando tu pregunta. El modelo no devolvió una respuesta válida después de varios intentos. Por favor reformulá la pregunta o contactá soporte.",
            citations=[],
            in_scope=False,
            confidence=0.0,
        ),
        "tokens_input": 0,
        "tokens_output": 0,
        "latency_seconds": 0,
        "attempts": max_retries + 1,
        "error": str(last_error),
    }