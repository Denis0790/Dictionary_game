from aiogram import types, F
from aiogram import Router

from bot_dictionary.frontend.services.api_get_all_words import get_all_words_in_backend

get_all_words_router = Router()

@get_all_words_router.message(F.text == "📚 Мой словарь")
@get_all_words_router.message(F.text == "/get_all")
async def get_all_words(message: types.Message):
    result = await get_all_words_in_backend()
    all_words = []
    for words in result:
        for word in words:
            all_words.append(word)
    formatted_lines = []

    for i in range(0, len(all_words), 2):
        english_word = all_words[i]
        russian_word = all_words[i + 1]
        formatted_line = f'{english_word.capitalize()} - {russian_word.capitalize()}'
        formatted_lines.append(formatted_line)

    output_message = '\n'.join(formatted_lines)


    await message.answer(output_message, parse_mode='Markdown')
