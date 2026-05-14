import aiohttp, random

WALL_API = "https://techz-wallpaper-bot-3.onrender.com/wall?query="
UNSPLASH_API = "https://techz-wallpaper-bot-3.onrender.com/unsplash?query="

async def get_wallpapers(query: str):
    try:
        url = WALL_API + query

        async with aiohttp.ClientSession() as session:
            resp = await session.get(url)
            data = await resp.json()

        images = data["results"]

        if len(images) == 0:
            return "nonee Can't find the wallpaper you are trying to search..."

        return images

    except Exception as e:
        return f"error {e}"


async def get_unsplash(query: str):
    try:
        url = UNSPLASH_API + query

        async with aiohttp.ClientSession() as session:
            resp = await session.get(url)
            data = await resp.json()

        images = data["results"]

        if len(images) == 0:
            return "nonee Can't find the wallpaper you are trying to search..."

        return images

    except Exception as e:
        return f"error {e}"
