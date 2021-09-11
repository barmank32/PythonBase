"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
from aiohttp import ClientSession

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def get_users() -> dict:
    async with ClientSession() as session:
        result = await fetch_json(session, USERS_DATA_URL)
    return result


async def get_posts() -> dict:
    async with ClientSession() as session:
        result = await fetch_json(session, POSTS_DATA_URL)
    return result
