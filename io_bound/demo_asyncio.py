import asyncio
from tqdm import tqdm

from io_bound.common import CODES, timeit
from io_bound.common_async_cats import async_get_http_cat, async_download_cat


async def async_download_cats():
    results = []
    tasks = [async_download_cat(code) for code in CODES]
    for future in tqdm(asyncio.as_completed(tasks), total=len(CODES)):
        result = await future
        results.append(result)
    return results


@timeit
def async_wrapper():
    return asyncio.run(async_download_cats())


async_wrapper()
