from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from states import AppealState
from keyboards import main_menu, confirm_kb, phone_kb
from db import save_appeal
from config import GROUP_ID
from aiogram import Bot

router = Router()

@router.message(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        "Assalawma aleykum!\nMúrájat jiberiw ushın túymeni basıń",
        reply_markup=main_menu()
    )

@router.message(text="📩 Múrájat jiberiw")
async def start_appeal(message: types.Message, state: FSMContext):
    await state.set_state(AppealState.full_name)
    await message.answer("Tolıq atıńızdı kiritiń:")

@router.message(AppealState.full_name)
async def get_name(message, state):
    await state.update_data(full_name=message.text)
    await state.set_state(AppealState.subject)
    await message.answer("Pánińizdi kiritiń:")

@router.message(AppealState.subject)
async def get_subject(message, state):
    await state.update_data(subject=message.text)
    await state.set_state(AppealState.workplace)
    await message.answer("Jumıs orınıńızdı kiritiń:")

@router.message(AppealState.workplace)
async def get_workplace(message, state):
    await state.update_data(workplace=message.text)
    await state.set_state(AppealState.phone)
    await message.answer("Telefon nomerińizdi jiberiń:", reply_markup=phone_kb())

@router.message(AppealState.phone)
async def get_phone(message, state):
    await state.update_data(phone=message.contact.phone_number)
    await state.set_state(AppealState.text)
    await message.answer("Múrajatıńızdı jazıń:")

@router.message(AppealState.text)
async def get_text(message, state):
    await state.update_data(text=message.text)
    data = await state.get_data()

    preview = f"""
🔍 Tekserip kóriń:

👤 {data['full_name']}
📚 {data['subject']}
🏫 {data['workplace']}
📞 {data['phone']}
📝 {data['text']}
"""
    await state.set_state(AppealState.confirm)
    await message.answer(preview, reply_markup=confirm_kb())

@router.message(AppealState.confirm)
async def confirm(message, state, bot: Bot):
    if message.text == "❌ Biykar etiw":
        await state.clear()
        await message.answer("Biykar etildi", reply_markup=main_menu())
        return

    data = await state.get_data()
    appeal_id = await save_appeal(data, message.from_user.id)

    group_text = f"""
🆕 JAŃA MÚRÁJAT

🆔 ID: {appeal_id}
👤 {data['full_name']}
📚 {data['subject']}
🏫 {data['workplace']}
📞 {data['phone']}
📝 {data['text']}
"""
    await bot.send_message(GROUP_ID, group_text)

    await message.answer(
        f"✅ Múrajatıńız qabıl etildi!\nID: {appeal_id}",
        reply_markup=main_menu()
    )
    await state.clear()
