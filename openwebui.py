import os
from dotenv import load_dotenv
from ollama import Client

load_dotenv()

ollama_host = os.getenv('OLLAMA_HOST') or ''
ollama_key = os.getenv('KEY_OLLAMA') or ''

client = Client(
    host=ollama_host,
    headers={
        'Authorization': 'Bearer ' + ollama_key
    }
)

response = client.chat(
    model='llama3.2',
    messages=[
        {
            'role': 'user',
            'content': 'Write a prompt for LLM that will generate picture of the day'
        }
    ]
)

print(response.message.content)
