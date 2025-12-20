import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv


from bot_dictionary.frontend.handlers.add_words_handler import add_words_router
from bot_dictionary.frontend.handlers.delete_word_handler import delete_router
from bot_dictionary.frontend.handlers.get_all_words import get_all_words_router
from bot_dictionary.frontend.handlers.get_random_word_handler import get_random_word_router
from bot_dictionary.frontend.handlers.new_victorina_handler import new_victorina_router
from bot_dictionary.frontend.handlers.other_text_input import other_text_router
from bot_dictionary.frontend.handlers.start_handler import start_router

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(storage=MemoryStorage())

dp.include_router(start_router)
dp.include_router(add_words_router)
dp.include_router(get_all_words_router)
#dp.include_router(get_random_word_router)
dp.include_router(delete_router)
dp.include_router(new_victorina_router)
dp.include_router(other_text_router)

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())