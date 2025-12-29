from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="📩 Múrájatıńızdı jiberiń")]],
        resize_keyboard=True
    )

def confirm_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="✅ Tastıyıqlaw")],
            [KeyboardButton(text="❌ Biykar etiw")]
        ],
        resize_keyboard=True
    )

def phone_kb():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="📞 Telefon nomerdi jiberiw", request_contact=True)]],
        resize_keyboard=True
    )
