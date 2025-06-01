import os
from dotenv import load_dotenv
from ollama import Client

ollama_host = os.getenv('OLLAMA_HOST') or ''
ollama_key = os.getenv('KEY_OLLAMA') or ''

client = Client(
    host=ollama_host,
    headers={
        'Authorization': 'Bearer ' + ollama_key
    }
)

def get_prompt(prompt: str) -> str | None:
    response = client.chat(
        model='llama3.2',
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    return response.message.content
