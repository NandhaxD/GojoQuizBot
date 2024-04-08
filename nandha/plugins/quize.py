import io
import os
import config
import requests
import asyncio
import random 


from nandha import bot
from pyrogram import filters, enums
from nandha.database.chats import add_chat
from nandha.helpers.decorator import admin_only

@bot.on_message(filters.command('quize', prefixes=config.PREFIXES))
@admin_only
async def select_quize(_, message):
      chat_id = message.chat.id
      user_id = message.from_user.id

      
        
                                  
                                


  
     
