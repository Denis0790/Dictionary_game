from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext

from bot_dictionary.frontend.services.api_get_all_words import get_all_words_in_backend
from bot_dictionary.frontend.states.states import QuizState

new_victorina_router = Router()

@new_victorina_router.message(F.text == "📝 Начать тест")
@new_victorina_router.message(F.text == "/victorina")
async def victorina_start(message: types.Message, state: FSMContext):
    result = await get_all_words_in_backend()

    if not result:
        await message.answer("Словарь пуст!")
        return

    await state.update_data(
        words=result,
        current_index=0,
        correct=0,
        incorrect=0,
        total=len(result)
    )

    await message.answer(
        f"В тесте {len(result)} слов. Поехали!\n"
        f"Я пишу на русском — ты на английском: \n"
        f"Если хочешь остановить тест - жми остановить тест"
    )

    first_word_ru = result[0][1].upper()
    await message.answer(f"Первое слово: {first_word_ru}", parse_mode="Markdown")

    await state.set_state(QuizState.waiting_for_answer)

@new_victorina_router.message(F.text == "🛑 Остановить тест")
@new_victorina_router.message(F.text == "/stop it", QuizState.waiting_for_answer)
async def stop_quiz(message: types.Message, state: FSMContext):
    data = await state.get_data()
    correct = data.get('correct', 0)
    incorrect = data.get('incorrect', 0)
    total_answered = correct + incorrect
    percent = round((correct / total_answered) * 100, 1) if total_answered > 0 else 0

    await message.answer(
        f"Тест остановлен. 🛑\nВаш результат: ✅ {correct} | ❌ {incorrect}\n"
        f"Точность: {percent}%"
    )
    await state.clear()


@new_victorina_router.message(QuizState.waiting_for_answer)
async def process_quiz_answer(message: types.Message, state: FSMContext):
    data = await state.get_data()

    words = data['words']
    idx = data['current_index']
    correct = data['correct']
    incorrect = data['incorrect']
    total = data['total']

    english_word = words[idx][0].strip().lower()
    user_answer = message.text.strip().lower()

    if user_answer == english_word:
        correct += 1
        res_msg = "Верно! ✅"
    else:
        incorrect += 1
        res_msg = f"Неверно! ❌\nПравильно: {(words[idx][0]).upper()}"

    idx += 1
    total_answered = correct + incorrect
    percent = round((correct / total_answered) * 100, 1)

    if idx < total:
        await state.update_data(current_index=idx, correct=correct, incorrect=incorrect)

        next_word_ru = words[idx][1].upper()
        await message.answer(
            f"{res_msg}\n"
            f"Статистика: ✅ {correct} | ❌ {incorrect}\n\n"
            f"Следующее слово ({idx + 1}/{total}): {next_word_ru}",
            parse_mode="Markdown"
        )
    else:
        await message.answer(
            f"{res_msg}\n\n"
            f"Поздравляю! Весь тест пройден. 🎉\n"
            f"Итоговый результат: ✅ {correct} из {total}\n"
            f"Точность: {percent}%"
        )
        await state.clear()