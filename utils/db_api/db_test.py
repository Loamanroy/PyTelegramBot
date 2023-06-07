import asyncio

from data import config
from utils.db_api import quickcommands as commands
from utils.db_api.db_telegrambot import db


async def db_test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    await commands.add_user(1, 'gfdqwte', 'qwe')
    await commands.add_user(1, 'Timur', 'gfqwte')
    await commands.add_user(1, 'Timur', 'gfdqwdte')
    await commands.add_user(1, 'Timur', 'gffe')
    await commands.add_user(1, 'Timur', 'gfqwdte')
    await commands.add_user(1, 'Timur', 'gftwe')
    await commands.add_user(1, 'Timur', 'gftqwfe')

    users = await commands.select_all_users()
    print(users)

    count = await commands.count_users()
    print(count)


loop = asyncio.get_event_loop()
loop.run_until_complete(db_test())
