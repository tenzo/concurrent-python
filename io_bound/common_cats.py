import os
import requests

from io_bound.common import BASE_URL, DOWNLOAD_DIR, CODES, save_cat_image


def get_http_cat(code: int) -> bytes:
    response = requests.get(BASE_URL.format(code=code))
    if response.status_code == 200:
        return response.content
    else:
        response.raise_for_status()
