import asyncio
import time

from aiogram import types, F
from aiogram import Router
from aiogram.fsm.context import FSMContext

from bot_dictionary.frontend.services.api_get_word_for_test import get_random_word_in_db
from bot_dictionary.frontend.states.states import CheckStates

get_random_word_router = Router()

@get_random_word_router.message(F.text == "📝 Начать тест")
@get_random_word_router.message(F.text == "/get_random")
async def get_random_word(message: types.Message, state: FSMContext):
    result = await get_random_word_in_db()
    try_word = result[0]
    result = result[1]

    await state.set_state(CheckStates.try_word)
    await state.update_data(try_word=try_word)
    await state.set_state(CheckStates.words_test)
    if result:
        answer_text = f"Жду перевод на слово: '{result}'"
        await message.answer(answer_text, parse_mode="Markdown")
    else:
        await message.answer("Произошла ошибка при получении слова.")


@get_random_word_router.message(F.text == "🛑 Остановить тест")
@get_random_word_router.message(F.text == "/stop_test")
async def stop_test(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.clear()
    await message.answer("Тестирование остановлено!")


@get_random_word_router.message(CheckStates.words_test)
async def get_answer_for_check(message: types.Message, state: FSMContext):
    await state.update_data(words_test=message.text)

    data = await state.get_data()
    try_word = data.get("try_word")
    try_word = try_word.lower()
    words_test = data.get("words_test")
    words_test = words_test.lower()

    if try_word == words_test:
        await message.answer(f"Верно!")
        await asyncio.sleep(1)
        await get_random_word(message, state)
    else:
        await message.answer(f"Неверно! Попробуй еще раз: ")