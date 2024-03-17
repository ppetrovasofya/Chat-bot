import logging
from aiogram import Bot, Dispatcher
import asyncio

from handlers import router

"""
Устанавливаем уровень логирования (просто в окне компиляции выдаст инфу о том,
что бот запущен и о тех изменениях, которые там происходят при общении с пользователем). 
"""
logging.basicConfig(level=logging.INFO)

bot = Bot(token="[Токен на тест-бота]")
dp = Dispatcher()


#запуск бота
async def main() -> None:
    dp.include_router(router)
    await dp.start_polling(bot)

asyncio.run(main())
