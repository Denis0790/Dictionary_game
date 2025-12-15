from aiogram.fsm.state import StatesGroup, State

class AddStates(StatesGroup):
    waiting_en = State()
    waiting_ru = State()