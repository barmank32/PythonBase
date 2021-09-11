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
from homework_04.jsonplaceholder_requests import get_posts, get_users
from homework_04.models import Base, Session, engine, User, Post


async def fetch_users_data():
    result = await get_users()
    return result


async def fetch_posts_data():
    result = await get_posts()
    return result


async def base_create():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def user_create(user_data):
    async with Session() as session:
        async with session.begin():
            for user in user_data:
                session.add(User(
                    name=user["name"],
                    username=user["username"],
                    email=user["email"]
                ))


async def post_create(post_data):
    async with Session() as session:
        async with session.begin():
            for post in post_data:
                session.add(Post(
                    user_id=post['userId'],
                    title=post['title'],
                    body=post['body']
                ))


async def async_main():
    users_data: List[dict]
    posts_data: List[dict]
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )
    await base_create()
    await user_create(users_data)
    await post_create(posts_data)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
