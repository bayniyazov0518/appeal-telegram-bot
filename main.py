import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers_user import router as user_router
from handlers_group import router as group_router
from db import init_db

async def main():
    await init_db()
    bot = Bot(token=8165993981:AAF1EWRHKdENWga54MHI1vvbfv5rz3AIXqM)
    dp = Dispatcher()
    dp.include_router(user_router)
    dp.include_router(group_router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
