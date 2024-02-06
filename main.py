import asyncio
import webserver

import command_handlers
from config import TOKEN
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode


bot = Bot(TOKEN, parse_mode=ParseMode.HTML)

# Запуск бота
async def main():
    # bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    #dp.include_router(questions.router)
    dp.include_router(command_handlers.router)

    # start web-server
    await webserver.start_server()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
