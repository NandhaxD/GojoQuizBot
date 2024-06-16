

from pyrogram import filters, types, enums, errors
from nandha.database.users import get_users
from nandha import bot
from nandha.helpers.func import time_diffrence

import random
import config


async def ask_start_pm(user_id: int, message):
    users = await get_users()    
    if not user_id in users:
         button = [[
           types.InlineKeyboardButton(text='✨ Start ✨', url=f'{config.NAME}.t.me?start=True')]]
         await message.reply(
             f'**⛔ Hello, {message.from_user.mention} start the bot in private and then start answering in {message.chat.title} 💫**',
             reply_markup=types.InlineKeyboardMarkup(button))
         return False
    else:
         return True





async def send_errors(m, e):
    text = (
      f"**Chat title**: {m.chat.title}\n"
      f"**Chat id**: `{m.chat.id}`\n"
      f"**Prompt**: `{m.text}`\n"
      f"**Link**: {m.link}\n"
      f"**Error**: {str(e)}\n"
    )
    chat_id = config.LOGS_CHANNEL 
    await bot.send_message(
        chat_id=chat_id, text=text
    )
  

async def react(message):
    try:
      await message.react(
         emoji=random.choice(config.EMOJI),
         big=True
       )
    except:
       pass




