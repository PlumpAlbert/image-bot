from __future__ import annotations
import logging
import os
from dotenv import load_dotenv
import pathlib
from ollama import Client
from yandex_cloud_ml_sdk import YCloudML
import telebot

from prompts import get_picture_prompt

logging.basicConfig(level=logging.INFO)
load_dotenv()

ollama_host = os.getenv('OLLAMA_HOST') or ''
ollama_key = os.getenv('KEY_OLLAMA') or ''
yandex_key = os.getenv('KEY_SECRET') or ''
telegram_key = os.getenv('KEY_TG') or ''
telegram_chat_id = os.getenv('TELEGRAM_CHAT') or ''

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
bot = telebot.TeleBot(token=telegram_key)

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
    message = get_prompt(get_picture_prompt()) or ''
    logging.info(f'# Generating image with: "{message}"')

    result = generate_image(message)
    path = pathlib.Path('./image.jpeg')
    path.write_bytes(result.image_bytes)
    logging.info('# Picture saved')

    with open('./image.jpeg', 'rb') as photo:
        logging.info('# Sending picture to telegram')
        bot.send_photo(
            chat_id=telegram_chat_id,
            caption=message,
            photo=photo
        )

if __name__ == '__main__':
    main()
