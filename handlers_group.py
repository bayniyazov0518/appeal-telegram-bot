import re
from aiogram import Router, types, F
from db import get_appeal
from config import GROUP_ID
from aiogram import Bot

router = Router()

@router.message(F.chat.id == GROUP_ID, F.reply_to_message)
async def reply_from_group(message: types.Message, bot: Bot):
    text = message.reply_to_message.text
    match = re.search(r"ID:\s*(\d+)", text)

    if not match:
        return

    appeal_id = int(match.group(1))
    appeal = await get_appeal(appeal_id)

    if not appeal:
        return

    user_id = appeal[1]

    await bot.send_message(
        user_id,
        f"📩 Metodist juwabı\n🆔 ID: {appeal_id}\n\n{message.text}"
    )

    await message.reply("✅ Juwap paydalanıwshıǵa jiberildi")
