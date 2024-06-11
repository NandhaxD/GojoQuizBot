
import config

from nandha import bot
from nandha.database.users import add_user
from nandha.database.chats import add_chat
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from nandha.helpers.scripts import react, ask_start_pm
from nandha.database.points import get_user_chat_points


async def start_message(name, message):
    await react(message)
    return await message.reply_photo(photo=config.START_IMAGE,
              caption="Welcome {name}! I'm Gojo Satoru, a quiz bot here to train you and boost your knowledge. Join our support channel. Thank you for using!".format(name=name),
       reply_markup=InlineKeyboardMarkup(
              [[
               InlineKeyboardButton(text='Support', url=f'{config.SUPPORT}.t.me'),
               InlineKeyboardButton(text='Channel', url=f'{config.CHANNEL}.t.me')
              ]]), quote=True)
              

@bot.on_message(filters.command('start', prefixes=config.PREFIXES))
async def start(_, message):
       chat_id = message.chat.id
       user_id = message.from_user.id
       name = message.from_user.first_name
       
       if message.chat.type == enums.ChatType.PRIVATE:           
            await add_user(user_id)
            await start_message(name, message)               
       else:
           await add_chat(chat_id)
           await start_message(name, message)






@bot.on_message(filters.command("stats", prefixes=config.PREFIXES))
async def stats(bot, message):
     m = message
     if m.chat.type == enums.ChatType.PRIVATE or not m.from_user:
         return
     user_id = m.from_user.id
     chat_id = m.chat.id
     name = m.from_user.first_name
     chat_name = m.chat.title
     
     if (await ask_start_pm(user_id, message)):
          rmath_points = await get_user_chat_points(
              chat_id, user_id, 'riddle', 'math'
          )
          rwords_points = await get_user_chat_points(
              chat_id, user_id, 'riddle', 'words'
          )
          text = config.STATS_STRING.format(
               name=name,
               chat_name=chat_name,
               rmath_points=rmath_points,
               rwords_points=rwords_points
          )
          await m.reply_text(text)
  
