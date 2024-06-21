
import config

from nandha import bot
from nandha.database.users import add_user
from nandha.database.chats import add_chat
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from nandha.helpers.scripts import react, ask_start_pm
from nandha.helpers.func import change_font
from nandha.database.points import get_user_chat_points
from nandha.helpers.ranks import get_user_rank


async def start_message(name, message):
    await react(message)
    txt = "Welcome {name}! I'm Gojo Satoru, a quiz bot here to train you and boost your knowledge. Join our support channel. Thank you for using!".format(name=name)
    return await message.reply_photo(photo=config.START_IMAGE,
              caption=change_font(txt),
       reply_markup=InlineKeyboardMarkup(
              [[
               InlineKeyboardButton(text=change_font('Support'), url=f'{config.SUPPORT}.t.me'),
               InlineKeyboardButton(text=change_font('Channel'), url=f'{config.CHANNEL}.t.me')
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






@bot.on_message(filters.command("profile", prefixes=config.PREFIXES))
async def statics(bot, message):
     m = message
     if m.chat.type == enums.ChatType.PRIVATE or not m.from_user:
         return
     user_id = m.from_user.id
     chat_id = m.chat.id
     name = m.from_user.mention
     chat_name = m.chat.title
     
     m_rank, m_points = await get_user_rank(user_id, 'riddle', 'math')
     w_rank, w_points = await get_user_rank(user_id, 'riddle', 'words')
  
     if (await ask_start_pm(user_id, message)):
          rmath_points = await get_user_chat_points(
              chat_id, user_id, 'riddle', 'math'
          )
          rwords_points = await get_user_chat_points(
              chat_id, user_id, 'riddle', 'words'
          )
          text = (
f"""
⚡ **{name}'s Profile**:

🌐 **Global Ranks**:

Maths Score ➾ {m_rank}th -〚 {m_points} 〛
Words Score ➾ {w_rank}th -〚 {w_points} 〛

More amazing updates coming soon.
""")
          await m.reply_photo(
            photo=config.STATS_IMG,
            caption=change_font(text)
          )
  
