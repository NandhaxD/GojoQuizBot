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
async def select_quize(_, message):
      chat_id = message.chat.id
      user_id = message.from_user.id
      await message.reply(
            "Before setting up a quiz in your group, you need to establish a timeline for sending the quiz periodically, with breaks in between. Click the button below to set up the quiz timeline."
      , reply_markup=InlineKeyboardMarkup(button), quote=True)
                        
      
        
                                  
                                


  
     
