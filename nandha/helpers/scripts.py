

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





class S_STRING:
    @staticmethod
    def legend(name, multiplier):
        return f"**Hey {name}, that's really awesome 🎉! You're doing great 🥳. I will {multiplier}x your points ✨!**"
    @staticmethod
    def pro(name, multiplier):
        return f"**Hey {name}, great job! I will {multiplier}x your points ✨!**"
    @staticmethod
    def player(name, multiplier):
        return f"**Hey {name}, well done 😊! Try to be a bit faster next time to claim more points. For now, I'm {multiplier}x your points 🎉!**"


async def get_special_points(start_time: str, end_time: str, name: str, message):
    time_diff = await time_diffrence(start_time, end_time)  # Assuming time_difference is defined elsewhere
  
    if int(time_diff) <= 8:
        points = random.randint(5, 10)
        await message.reply_sticker(sticker=config.S_STICKER, quote=True)
        await message.reply_text(S_STRING.legend(name, points))
    elif int(time_diff) <= 60:
        points = random.randint(1, 5)
        await message.reply_sticker(sticker=config.S_STICKER, quote=True)
        await message.reply_text(S_STRING.pro(name, points))
    else:
        points = 1
        await message.reply_sticker(sticker=config.S_STICKER, quote=True)
        await message.reply_text(S_STRING.player(name, points))
    
    return points







