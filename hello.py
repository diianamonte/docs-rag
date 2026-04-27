import os
from dotenv import load_dotenv
from groq import Groq

# Cargo la API key desde .env
load_dotenv()

# Inicializo el cliente
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Hago una pregunta simple
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": "Hola Groq, ¿estás funcionando?"}
    ],
)

print(response.choices[0].message.content)