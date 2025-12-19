from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_main_menu_kb():
    builder = ReplyKeyboardBuilder()

    builder.button(text="➕ Добавить слово")
    builder.button(text="📝 Начать тест")
    builder.button(text="📚 Мой словарь")
    builder.button(text="🛑 Остановить тест")

    builder.adjust(2)

    return builder.as_markup(
        resize_keyboard=True,
        is_persistent=True
    )


