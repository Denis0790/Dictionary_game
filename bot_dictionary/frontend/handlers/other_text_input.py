import random

from aiogram import types, F
from aiogram import Router

other_text_router = Router()


@other_text_router.message(F.text)
async def get_other_text(message: types.Message):
    await message.answer(text_for_other_text())



def text_for_other_text() -> str:
    a = "Таких команд не знаю"
    b = "Что-то для меня на непонятном"
    c = "Чавой написал?"
    d = "Моя твоя не понимать"
    e = "Учи слова, а не буковки пиши)"
    f = "Драсьте, я банан!"
    g = "Бе бе бе 😂"
    result = random.choice([a, b, c, d, e, f, g])
    return result