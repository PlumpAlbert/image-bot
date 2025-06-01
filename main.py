from __future__ import annotations
import os
from dotenv import load_dotenv
import pathlib
from ollama import Client
from yandex_cloud_ml_sdk import YCloudML

load_dotenv()

ollama_host = os.getenv('OLLAMA_HOST') or ''
ollama_key = os.getenv('KEY_OLLAMA') or ''
yandex_key = os.getenv('KEY_SECRET') or ''

client = Client(
    host=ollama_host,
    headers={
        'Authorization': 'Bearer ' + ollama_key
    }
)
sdk = YCloudML(
    folder_id='b1g911dgehfvr5va5erg',
    auth=yandex_key
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

def generate_image(prompt: str):
    """
    Generates an image based on the provided prompt using Yandex Cloud ML.

    Args:
        prompt (str): The text-based description of the desired image.

    Returns:
        ImageResult: An object containing details about the generated image, including image bytes.
    """

    model = sdk.models.image_generation('yandex-art')

    model = model.configure(width_ratio=9, height_ratio=16, seed=1863)

    operation = model.run_deferred(prompt)
    result = operation.wait()

    return result

prompt = """
Write prompt that will be used for generative LLM which will generate image
based on your text. Respond with only the prompt text and nothing else.
The prompt should not contain any placeholders.
"""

def main():
    message = get_prompt(prompt) or ''
    print('Generating image with: "' + message + '"')

    # commented out for development
    # result = generate_image(message)
    # path = pathlib.Path('./image.jpeg')
    # path.write_bytes(result.image_bytes)

if __name__ == '__main__':
    main()
