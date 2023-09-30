import asyncio

from config import TOKEN
from aiogram import Bot, Dispatcher, Router, types, F

from handlers import questions


# Запуск бота
async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()

    dp.include_router(questions.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

