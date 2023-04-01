# %%
import aiohttp
import asyncio

from io_bound.common_cats import BASE_URL, DOWNLOAD_DIR, CODES, save_cat_image


async def async_get_http_cat(code: int) -> bytes:
    async with aiohttp.ClientSession(raise_for_status=True) as session:
        async with session.get(BASE_URL.format(code=code)) as response:
            cat_image = await response.read()
            return cat_image


async def async_download_cat(code: int) -> None:
    try:
        cat_image = await async_get_http_cat(code)
        blocking_task = asyncio.get_event_loop().run_in_executor(
            None, save_cat_image, cat_image, "cat_{}".format(code)
        )
        completed, pending = await asyncio.wait([blocking_task])
        return {code: True}
    except aiohttp.client_exceptions.ClientResponseError:
        return {code: False}
