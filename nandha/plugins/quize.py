import config


from nandha import bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from nandha.database.chats import add_chat
from nandha.helpers.decorator import admin_only




@bot.on_message(filters.command('quize', prefixes=config.PREFIXES))
@admin_only
async def quize_cmd(_, message):
      chat_id = message.chat.id
      user_id = message.from_user.id
      
      button = [[
      InlineKeyboardButton(text='Customize', callback_data=f'cb_quize:{user_id}')
            
]]
      
      await message.reply(
            "Before setting up a quiz in your group, you need to establish a timeline for sending the quiz periodically, with breaks in between. Click the button below to set up the quiz time."
      , reply_markup=InlineKeyboardMarkup(button), quote=True)
                        
      
        
                                  
@bot.on_callback_query(filters.regex('^cb_quize'))
async def customize_quize(_, query):
      user_id = query.from_user.id
      admin_id = int(query.data.split(':')[1])
      if user_id != admin_id:
            return await query.answer("🔐 Sorry this not for you. try you're own to customize.", show_alert=True)
      else:  
        button = [[
              InlineKeyboardButton(text='Math Quize', callback_data=f'math:{user_id}'),
              InlineKeyboardButton(text='Physics Quize', callback_data=f'physics:{user_id}'),
        ],[
              InlineKeyboardButton(text='Chemistry Quize', callback_data=f'chemistry:{user_id}'),
              InlineKeyboardButton(text='Zoolagy Quize', callback_data=f'zoolagy:{user_id}')
        ] , [
                    InlineKeyboardButton(text='Back ⬅️', callback_data='back')
              
              
        
]]
        return await query.message.edit(
              "Here is a list of quizzes for your chat ✨. You can set up a maximum of two quizzes in one chat group. Click on the quize type button for quick setup."
        , reply_markup=InlineKeyboardMarkup(button))
       


  
     
