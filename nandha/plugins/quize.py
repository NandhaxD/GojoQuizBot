import io
import os
import config
import requests
import asyncio
import random 


from nandha import bot
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from nandha.database.chats import add_chat
from nandha.helpers.decorator import admin_only


button = [[
      InlineKeyboardButton(text='Customize', callback_data='customize'),
      InlineKeyboardButton(text='Skip', callback_data='skip')      
]]

@bot.on_message(filters.command('quize', prefixes=config.PREFIXES))
@admin_only
async def quize(_, message):
      chat_id = message.chat.id
      user_id = message.from_user.id
      
      button = [[
      InlineKeyboardButton(text='Customize', callback_data=f'customize:{user_id}'),
      InlineKeyboardButton(text='Skip', callback_data='skip')      
]]
      
      await message.reply(
            "Before setting up a quiz in your group, you need to establish a timeline for sending the quiz periodically, with breaks in between. Click the button below to set up the quiz timeline."
      , reply_markup=InlineKeyboardMarkup(button), quote=True)
                        
      
        
                                  
@bot.on_callback_query(filters.regex('^customize'))
async def customize(_, query):
      user_id = query.from_user.id
      admin_id = int(query.data.split(':')[1])
      if user_id != admin_id:
            return await query.answer("🔐 Sorry this not for you. try you're own to customize.", show_alert=True)
      else:  
        button = [[
              Inlinekeyboardbutton(text='Math Quize', callback_data=f'math:{user_id}'),
              Inlinekeyboardbutton(text='Math Quize', callback_data=f'physics:{user_id}'),
              Inlinekeyboardbutton(text='Math Quize', callback_data=f'chemistry:{user_id}'),
              Inlinekeyboardbutton(text='Math Quize', callback_data=f'zoolagy:{user_id}')
        ] , [
                    Inlinekeyboardbutton(text='Back ⬅️', callback_data='back')
              
              
        
]]
        return await query.message.edit(
              "Here is a list of quizzes for your chat ✨. You can set up a maximum of three quizzes in one chat group. Click on the quiz for quick setup."
        , reply_markup=InlineKeyboardMarkup(button))
       


  
     
