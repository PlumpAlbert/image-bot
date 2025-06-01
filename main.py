from __future__ import annotations
import os
from dotenv import load_dotenv
import pathlib

load_dotenv()

from openwebui import get_prompt
from ya import generate_image

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
