"""
Домашнее задание №3
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from typing import List
from homework_04.jsonplaceholder_requests import get_json, USERS_DATA_URL, POSTS_DATA_URL
from homework_04.models import Base, Session, engine, User, Post


async def fetch_data(url: str):
    result = await get_json(url)
    return result


async def base_create():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def base_insert(query: Base):
    async with Session() as session:
        async with session.begin():
            session.add_all(query)


async def user_create(user_data):
    query: List[Base] = []
    for user in user_data:
        query.append(User(
            name=user["name"],
            username=user["username"],
            email=user["email"]
        ))
    await base_insert(query)


async def post_create(post_data):
    query: List[Base] = []
    for post in post_data:
        query.append(Post(
            user_id=post['userId'],
            title=post['title'],
            body=post['body']
        ))
    await base_insert(query)


async def async_main():
    users_data: List[dict]
    posts_data: List[dict]
    users_data, posts_data = await asyncio.gather(
        fetch_data(USERS_DATA_URL),
        fetch_data(POSTS_DATA_URL),
    )
    await base_create()
    await user_create(users_data)
    await post_create(posts_data)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
