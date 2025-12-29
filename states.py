from aiogram.fsm.state import StatesGroup, State

class AppealState(StatesGroup):
    full_name = State()
    subject = State()
    workplace = State()
    phone = State()
    text = State()
    confirm = State()
