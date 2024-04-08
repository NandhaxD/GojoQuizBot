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




@bot.on_message(filters.command('riddle', prefixes=config.PREFIXES))
@admin_only
async def riddle(_, message):
      chat_id = message.chat.id
      user_id = message.from_user.id
      
      button = [[
      InlineKeyboardButton(text='Customize', callback_data=f'cb_riddle:{user_id}')      
]]
      
      await message.reply(
            "Before setting up a riddle in your group, you need to establish a timeline for sending the riddle periodically, with breaks in between. Click the button below to set up the riddle timeline."
      , reply_markup=InlineKeyboardMarkup(button), quote=True)
                        
      
        
                                  
@bot.on_callback_query(filters.regex('^cb_riddle'))
async def customize(_, query):
      user_id = query.from_user.id
      admin_id = int(query.data.split(':')[1])
      if user_id != admin_id:
            return await query.answer("🔐 Sorry this not for you. try you're own to customize.", show_alert=True)
      else:  
        button = [[
              InlineKeyboardButton(text='Math Riddle', callback_data=f'rmath:{user_id}'),
              InlineKeyboardButton(text='Comming Soon', callback_data=f'cs:{user_id}'),
        ],[
              InlineKeyboardButton(text='Comming Soon', callback_data=f'cs:{user_id}'),
              InlineKeyboardButton(text='Comming Soon', callback_data=f'cs:{user_id}')
        ] , [
                    InlineKeyboardButton(text='Back ⬅️', callback_data='back')
              
              
        
]]
        return await query.message.edit(
              "Here is a list of riddles for your chat ✨. You can set up a maximum of three riddles in one chat group. Click on the riddle type button for quick setup."
        , reply_markup=InlineKeyboardMarkup(button))
       

@bot.on_callback_query(filters.regex('^cs'))
async def commingsoon(_, query):
      return await query.answer('I have no idea about what i next add for riddle so please if you have some idea kindly share to @Nandha', show_alert=True)

