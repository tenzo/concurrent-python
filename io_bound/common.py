import os
import requests
import time

BASE_URL = "https://http.cat/{code}"
DOWNLOAD_DIR = "/home/tenzo/http_cats"

CODES = tuple(requests.status_codes._codes.keys())


def save_cat_image(image: bytes, filename: str) -> None:
    path = os.path.join(DOWNLOAD_DIR, "{}.jpg".format(filename))
    with open(path, "wb") as cat_file:
        cat_file.write(image)


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print("{0}  {1:2.2f} ms".format(method.__name__, (te - ts) * 1000))

    return timed
