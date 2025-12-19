from aiogram import types, F
from aiogram import Router

from bot_dictionary.frontend.keyboards.keyboards import get_main_menu_kb

start_router = Router()


@start_router.message(F.text == "/start")
async def command_start_handler(message: types.Message) -> None:
    await message.answer(
        f"Привет! {message.from_user.full_name} \nВыбери нужное действие в меню:",
        reply_markup=get_main_menu_kb()
    )