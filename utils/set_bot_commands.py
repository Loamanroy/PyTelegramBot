from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Start Bot'),
        types.BotCommand('help', 'Help'),
        types.BotCommand('register', 'Registration'),
        types.BotCommand('profile', 'Посмотреть профиль'),
        types.BotCommand('question', 'Задать вопрос')
    ])
