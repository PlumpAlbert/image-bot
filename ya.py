from __future__ import annotations
from yandex_cloud_ml_sdk import YCloudML
import os

yandex_key = os.getenv('KEY_SECRET') or ''

def generate_image(prompt: str):
    """
    Generates an image based on the provided prompt using Yandex Cloud ML.

    Args:
        prompt (str): The text-based description of the desired image.

    Returns:
        ImageResult: An object containing details about the generated image, including image bytes.
    """
    sdk = YCloudML(
        folder_id='b1g911dgehfvr5va5erg',
        auth=yandex_key
    )

    model = sdk.models.image_generation('yandex-art')

    model = model.configure(width_ratio=9, height_ratio=16, seed=1863)

    operation = model.run_deferred(prompt)
    result = operation.wait()

    return result
