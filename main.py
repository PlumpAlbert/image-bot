from __future__ import annotations
import logging
import os
from dotenv import load_dotenv
import pathlib
from yandex_cloud_ml_sdk import YCloudML
import telebot
from telebot.formatting import hcite

from prompts import get_picture_prompt

logging.basicConfig(level=logging.INFO)
load_dotenv()

yandex_folder_id = os.getenv('YA_FOLDER_ID') or ''
yandex_key = os.getenv('KEY_SECRET') or ''
telegram_key = os.getenv('KEY_TG') or ''
telegram_chat_id = os.getenv('TELEGRAM_CHAT') or ''

sdk = YCloudML(
    folder_id=yandex_folder_id,
    auth=yandex_key
)
bot = telebot.TeleBot(token=telegram_key)

def get_prompt(prompt: str) -> str | None:
    model = sdk.models.completions("yandexgpt")

    response = model.run(prompt)

    return response.alternatives[0].text

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

def main():
    text_prompt = get_picture_prompt()
    message = get_prompt(text_prompt) or ''
    logging.info(f'# Generating image with: "{message}"')

    result = generate_image(message)
    path = pathlib.Path('./image.jpeg')
    path.write_bytes(result.image_bytes)
    logging.info('# Picture saved')

    with open('./image.jpeg', 'rb') as photo:
        logging.info('# Sending picture to telegram')
        bot.send_photo(
            chat_id=telegram_chat_id,
            caption=hcite(message, True, True),
            parse_mode='html',
            photo=photo
        )

if __name__ == '__main__':
    main()
