


from pyrogram import filters 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from nandha.database.riddle.math_riddle import is_chat_riddle, get_chat_time, set_chat_time
from nandha.database.chats import add_chat
from nandha import bot



@bot.on_callback_query(filters.regex('^rmath'))
async def riddle_math(_, query):
      user_id = query.from_user.id
      chat_id = query.message.chat.id
      
      admin_id = int(query.data.split(':')[1])
      if user_id != admin_id:
            return await query.answer("🔐 Sorry this not for you. try you're own to customize.", show_alert=True)
      else:
         riddle = await is_chat_riddle(chat_id)
         time = await get_chat_time(chat_id)
         button = [[
           InlineKeyboardButton(text='60 seconds', callback_data=f'rmtime:{user_id}:60'),
           InlineKeyboardButton(text='1 hour ', callback_data=f'rmtime:{user_id}:3600'),],
                   [InlineKeyboardButton(text='3 hours', callback_data=f'rmtime:{user_id}:10800'),
                    InlineKeyboardButton(text='6 hours', callback_data=f'rmtime:{user_id}:21600'), ],
                   [ InlineKeyboardButton(text='back ⬅️', callback_data=f'cb_riddle:{user_id}')
           
]]
         return await query.message.edit(
           f"Hello! Now you can set up a time for your chat. Click the button below to do so.\n\n<b>You're chat riddle is</b>: {riddle}\n<b>You're chat riddle time</b>: {time}",
           reply_markup=InlineKeyboardMarkup(button))


@bot.on_callback_query(filters.regex('^rmtime'))
async def set_riddle_chat_time(_, query):
       user_id = query.from_user.id
       chat_id = query.message.chat.id
      
       admin_id = int(query.data.split(':')[1])
       if user_id != admin_id:
             return await query.answer("🔐 Sorry this not for you. try you're own to customize.", show_alert=True)
       else:
           time = int(query.data.split(':')[2])
           await set_chat_time(chat_id, time)
           riddle = await is_chat_riddle(chat_id)
           time = await get_chat_time(chat_id)   
           return await query.message.edit(
                 f"Successfully set-up you're chat riddle 😉!\n\n<b>You're chat riddle is</b>: {riddle}\n<b>You're chat riddle time</b>: {time}"
           )
                                
