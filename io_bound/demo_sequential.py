# %%
import requests
from tqdm import tqdm

from io_bound.common_cats import get_http_cat, save_cat_image
from io_bound.common import timeit, CODES

#%%
@timeit
def download_cats_sequential() -> None:
    for code in tqdm(CODES):
        try:
            cat_img = get_http_cat(code)
            save_cat_image(cat_img, "cat_{}.jpg".format(code))
        except requests.HTTPError:
            pass


#%%
download_cats_sequential()

#%%
