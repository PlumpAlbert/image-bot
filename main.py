from __future__ import annotations
import os
from dotenv import load_dotenv
import pathlib
from yandex_cloud_ml_sdk import YCloudML

load_dotenv()

message = """
Милое животное держит в руках чашечку горячего чая, смотрит на нас, на фоне
красивый пейзаж, full hd, добавь красивую надпись 'Добрый вечер!'
"""

def main():
    sdk = YCloudML(
        folder_id='b1g911dgehfvr5va5erg',
        auth=os.getenv('KEY_SECRET') or ''
    )

    model = sdk.models.image_generation('yandex-art')

    model = model.configure(width_ratio=2, height_ratio=1, seed=1863)

    path = pathlib.Path('./image.jpeg')
    operation = model.run_deferred(message)
    result = operation.wait()
    path.write_bytes(result.image_bytes)

if __name__ == '__main__':
    main()
