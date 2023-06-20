# from asyncpg import UniqueViolationError
#
# from utils.db_api.db_telegrambot import db
#
#
# async def add_user(user_id: int, name: str):
#     try:
#         user = User(user_id=user_id, name=name)
#         await user.create()
#     except UniqueViolationError:
#         print('User not registered')
#
#
# async def select_all_users():
#     users = await User.query.gino.all()
#     return users
#
#
# async def count_users():
#     count = await db.func.count(User.user_id).gino.scalar()
#     return count
#
#
# async def select_user(user_id):
#     user = await User.query.where(User.user_id == user_id.gino.first())
#     return user
#
#
# async def update_username(user_id, new_name):
#     user = await select_user(user_id)
#     await user.update(update_name=new_name).apply()
