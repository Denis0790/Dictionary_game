from aiogram.fsm.context import FSMContext
from aiogram import types, F
from aiogram import Router

from bot_dictionary.frontend.services.api_delete_word import delete_word_api
from bot_dictionary.frontend.states.states import DeleteWord

delete_router = Router()

@delete_router.message(F.text == "❌ Удалить")
@delete_router.message(F.text == "/delete")
async def delete_word(message: types.Message, state: FSMContext):
    await message.answer("Напиши слово на английском языке, которое хочешь удалить: ")
    await state.set_state(DeleteWord.word_en)

@delete_router.message(DeleteWord.word_en)
async def delete_word_en(message: types.Message, state: FSMContext):
    await state.update_data(word_en=message.text)

    data = await state.get_data()

    result = data.get("word_en").lower()
    answer = await delete_word_api(result)
    await message.answer(f"{answer}")

    await state.clear()