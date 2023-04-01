# %%
import requests
from tqdm import tqdm
from concurrent import futures

from io_bound.common_cats import get_http_cat, save_cat_image
from io_bound.common import timeit, CODES

# %%
def download_a_cat(code: int) -> None:
    try:
        cat_img = get_http_cat(code)
        save_cat_image(cat_img, "cat_{}".format(code))
        return {code: True}
    except requests.HTTPError:
        return {code: False}


# %%
@timeit
def download_cats_with_map() -> None:
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        result = executor.map(download_a_cat, tqdm(CODES))


# %%
@timeit
def download_cats_with_submit() -> None:
    results = []
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        tasks = [executor.submit(download_a_cat, code) for code in CODES]

        for future in tqdm(futures.as_completed(tasks), total=len(CODES)):
            results.append(future.result())


#%%
download_cats_with_map()

#%%
download_cats_with_submit()
