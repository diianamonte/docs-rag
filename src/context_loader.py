from pathlib import Path


def load_context(source: str = "context/pomelo_docs.md") -> str:
    """
    Carga el contexto desde un archivo.
    
    Más adelante esta función va a ser reemplazada por una que consulta
    un vector store, pero el resto del código no se va a enterar.
    
    Args:
        source: ruta al archivo de contexto
    
    Returns:
        Contenido del archivo como string
    
    Raises:
        FileNotFoundError: si el archivo no existe
    """
    path = Path(source)
    if not path.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo de contexto: {source}"
        )
    
    return path.read_text(encoding="utf-8")