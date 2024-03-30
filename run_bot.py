import logging
from aiogram import Bot, Dispatcher
import asyncio

from handlers import router

"""
Устанавливаем уровень логирования (просто в окне компиляции выдаст инфу о том,
что бот запущен и о тех изменениях, которые там происходят при общении с пользователем). 
"""
logging.basicConfig(level=logging.INFO)

bot = Bot(token="7055728613:AAHsj-Uufr_Qb7L-9OzddNfBzWHGY8DPhI8")
dp = Dispatcher()


#запуск бота
async def main() -> None:
    dp.include_router(router)
    await dp.start_polling(bot)

asyncio.run(main())
