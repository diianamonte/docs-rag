from pydantic import BaseModel, Field
from typing import List


class RAGResponse(BaseModel):
    """
    Estructura esperada de respuesta del LLM.
    Si el modelo no cumple este schema, retry o fallback.
    """
    answer: str = Field(
        ...,
        min_length=10,
        max_length=2000,
        description="Respuesta a la pregunta del usuario"
    )
    citations: List[str] = Field(
        default_factory=list,
        description="Secciones de la documentación que respaldan la respuesta"
    )
    in_scope: bool = Field(
        ...,
        description="True si la pregunta está cubierta por la documentación"
    )
    confidence: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Nivel de confianza del modelo en su respuesta"
    )