import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import log_in


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token="")
    dp = Dispatcher()

    dp.include_router(log_in.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
