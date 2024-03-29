import asyncio
import logging
from aiogram import Bot, Dispatcher
from project import handlers


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token="os.getenv(“TOKEN”)")
    dp = Dispatcher()

    dp.include_router(handlers.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
