from aiogram import types, F
from aiogram import Router

start_router = Router()


@start_router.message(F.text == "/start")
async def command_start_handler(message: types.Message) -> None:
    await message.answer(f"Привет, **{message.from_user.full_name}**! хай")