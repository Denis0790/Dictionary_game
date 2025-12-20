from aiogram import types, F
from aiogram import Router
from aiogram.fsm.context import FSMContext

from bot_dictionary.frontend.services.api_add_word import add_words_in_backend
from bot_dictionary.frontend.states.states import AddStates
add_words_router = Router()

@add_words_router.message(F.text == "➕ Добавить слово")
@add_words_router.message(F.text == "/add")
async def command_start_add_handler(message: types.Message, state: FSMContext):
    await message.answer(f"Для того, что бы запомнить слова, впиши сначала на английском и отправь мне:")
    await state.set_state(AddStates.waiting_en)

@add_words_router.message(AddStates.waiting_en)
async def command_add_en(message: types.Message, state: FSMContext) -> None:
    await state.update_data(en_word=message.text)
    await message.answer("Прекрасно, теперь введи перевод этого слова на русском и пришли мне:")
    await state.set_state(AddStates.waiting_ru)

@add_words_router.message(AddStates.waiting_ru)
async def command_add_ru(message: types.Message, state: FSMContext) -> None:
    await state.update_data(ru_word=message.text)

    data = await state.get_data()
    english_word = data.get("en_word").lower()
    russian_word = data.get("ru_word").lower()
    answer_add = await add_words_in_backend(english_word, russian_word)
    await message.answer(f'{answer_add}')

    await state.clear()