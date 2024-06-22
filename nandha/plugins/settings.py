import config


from nandha import bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from nandha.database.chats import add_chat
from nandha.helpers.decorator import admin_only

 
@bot.on_message(filters.command('settings', prefixes=config.PREFIXES))
@admin_only
async def send_settings(_, message):
       chat_id = message.chat.id
       user_id = message.from_user.id
       await add_chat(chat_id)

       button = [[
      InlineKeyboardButton(text='Riddle', callback_data=f'cb_riddle:{user_id}')
       ],[
      InlineKeyboardButton(text='Quiz', callback_data=f'cb_quize:{user_id}')
              
]]
       return await message.reply(
              'Click the below button for change settings ⚙️.', reply_markup=InlineKeyboardMarkup(button)
       )
                                

@bot.on_callback_query(filters.regex('^settings'))
async def cb_settings(_, query):
      user_id = query.from_user.id
      admin_id = int(query.data.split(':')[1])
      if user_id != admin_id:
            return await query.answer("🔐 Sorry this not for you. try you're own to customize.", show_alert=True)
      else:  
        button = [[
      InlineKeyboardButton(text='Riddle', callback_data=f'cb_riddle:{user_id}')
       ],[
      InlineKeyboardButton(text='Quiz', callback_data=f'cb_quize:{user_id}')
              
]]
        return await query.message.edit(
              "Click the below button for change settings ⚙️."
        , reply_markup=InlineKeyboardMarkup(button))
       



################################################################################################################################


# Quiz Codes
                                  
@bot.on_callback_query(filters.regex('^cb_quiz'))
async def customize_quize(_, query):
      user_id = query.from_user.id
      admin_id = int(query.data.split(':')[1])
      if user_id != admin_id:
            return await query.answer("🔐 Sorry this not for you. try you're own to customize.", show_alert=True)
      else:  
        button = [[
              InlineKeyboardButton(text='Math Quiz', callback_data=f'math:{user_id}'),
              InlineKeyboardButton(text='Physics Quiz', callback_data=f'physics:{user_id}'),
        ],[
              InlineKeyboardButton(text='Chemistry Quiz', callback_data=f'chemistry:{user_id}'),
              InlineKeyboardButton(text='Zoology Quiz', callback_data=f'zoolagy:{user_id}')
        ] , [
                    InlineKeyboardButton(text='𝗕𝗔𝗖𝗞 ⬅️', callback_data=f'settings:{user_id}')
              
              
        
]]
        return await query.message.edit(
              "Here Is A List Of Quizzes For Your Chat ✨. You Can Set Up A Maximum Of Two Quizzes In One Chat Group. CLick On The Quize Type Button For Quick Setup."
        , reply_markup=InlineKeyboardMarkup(button))
       





################################################################################################################################

# CODES RELATED TO RIDDLE 


        
                                  
@bot.on_callback_query(filters.regex('^cb_riddle'))
async def customize_riddle(_, query):
      user_id = query.from_user.id
      admin_id = int(query.data.split(':')[1])
      if user_id != admin_id:
            return await query.answer("🔐 Sorry this not for you. try you're own to customize.", show_alert=True)
      else:  
        button = [[
              InlineKeyboardButton(text='Maths', callback_data=f'rmath:{user_id}'),
              InlineKeyboardButton(text='Words', callback_data=f'rwords:{user_id}'),
        ],[
              InlineKeyboardButton(text='Emoji', callback_data=f'remoji:{user_id}'),
              InlineKeyboardButton(text='Comming Soon', callback_data=f'cs:{user_id}')
        ] , [
                    InlineKeyboardButton(text='𝗕𝗔𝗖𝗞 ⬅️', callback_data=f'settings:{user_id}')
              
              
        
]]
        return await query.message.edit(
              "Here is a list of riddles for your chat ✨. You can set up a maximum of two riddles in one chat group. Click on the riddle type button for quick setup."
        , reply_markup=InlineKeyboardMarkup(button)
        )
       


@bot.on_callback_query(filters.regex('^cs'))
async def comming_soon(_, query):
      return await query.answer('I have no idea about what i next add for riddle so please if you have some idea kindly share to @Nandha', show_alert=True)

################################################################################################################################

     
