
import config

from nandha import bot
from nandha.database.users import add_user
from nandha.database.chats import add_chat
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton



async def start_message(name, message):
    return await message.reply_photo(photo=config.START_IMAGE,
              caption="Welcome {name}! I'm Gojo Satoru, a quiz bot here to train you and boost your knowledge. Join our support channel. Thank you for using!".format(name=name),
       reply_markup=InlineKeyboardMarkup(
              [[InlineKeyboardButton(text='Support', url=config.SUPPORT_URL),
               InlineKeyboardButton(text='Channel', url=config.CHANNEL_URL)]]), quote=True)
              

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








  
