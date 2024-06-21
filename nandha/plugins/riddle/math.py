
import os
import config
import asyncio
import random

from pyrogram import filters 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from nandha.database.db import is_chat, get_chat_sleep, off_chat, on_chat, save_chat_data, clear_chat_data, get_chat_data
from nandha.database.points import add_user_chat_points, get_user_chat_points
from nandha.database.users import update_name
from nandha.database.chats import add_chat
from nandha.helpers.func import get_question, make_math_riddle, taken_time, change_font
from nandha.helpers.scripts import ask_start_pm, react, send_errors
from nandha import bot



mode = 'riddle'
type = 'math'



chats_id = {} # temp chat ids

@bot.on_message(filters.text & ~filters.private & ~filters.bot, group=-2 )
async def check_user_rmath_ans(_, message):
        chat_id = message.chat.id
        chat_name = message.chat.title
        
        if not chat_id in chats_id:
               return
        else:
            riddle = list(await get_chat_data(chat_id, mode, type))
            if riddle == False:
                    return
            else:
                 answer = int(riddle[1])
                 start_time = str(riddle[2])
                    
                 if message.sender_chat:
                         return
                                  
                 try:
                    text = message.text
                    if not text.isdigit():
                       return
                    elif int(text) == answer:
                      
                         await clear_chat_data(chat_id, mode, type)
                         mention = message.from_user.mention
                         user_id = message.from_user.id
                         first_name = message.from_user.first_name
                         msg_id = message.id
                            
                         if (await ask_start_pm(user_id, message)) == False:
                                return 
                           
                         await update_name(user_id, first_name) # update name of user
                         await react(message)
                      
                         end_time = str(message.date).split()[1]
                         a_time = await taken_time(
                                start_time=start_time, 
                                 end_time=end_time
                        ) 
                                    
                         await add_user_chat_points(chat_id, user_id, mode, type)
                         points = await get_user_chat_points(chat_id, user_id, mode, type)

                         txt = text=config.RIDDLE_WINNER_STRING.format(first_name, type.upper(), points, a_time)
                         await message.reply_text(
                            text=change_font(txt)
                         )
                 except Exception as e:
                       return await send_errors(message, e)
                 


@bot.on_callback_query(filters.regex('^rmath'))
async def riddle_math(_, query):
      user_id = query.from_user.id
      chat_id = query.message.chat.id
        
      admin_id = int(query.data.split(':')[1])
      if user_id != admin_id:
            return await query.answer(
              text=change_font("🔐 Sorry this not for you. try you're own to customize.")
              , show_alert=True)
      else:
         riddle = await is_chat(chat_id, mode, type)
         time = await get_chat_sleep(chat_id, mode, type)
         button = [[
           InlineKeyboardButton(text=change_font('60 Sec'), callback_data=f'rmtime:{user_id}:60'),
           InlineKeyboardButton(text=change_font('3 Min'), callback_data=f'rmtime:{user_id}:90'),],
                   [InlineKeyboardButton(text=change_font('10 Min'), callback_data=f'rmtime:{user_id}:600'),
                    InlineKeyboardButton(text=change_font('30 Min'), callback_data=f'rmtime:{user_id}:1800'), ],
                   [ InlineKeyboardButton(text=change_font('Back ⬅️'), callback_data=f'cb_riddle:{user_id}')
           
]]
            
         off_button = [[
               InlineKeyboardButton(text=change_font('OFF 🛑'), callback_data=f'rmoff:{user_id}'),
               InlineKeyboardButton(text=change_font('BACK ⬅️'), callback_data=f'cb_riddle:{user_id}')
 ]]
         if riddle:
               txt = "This chat has already set up the timing for sending math riddles. To change the settings, turn them off and try again."
               return await query.message.edit(
                     change_font(txt),
                     reply_markup=InlineKeyboardMarkup(off_button))
                     
         else:
             txt = f"Hello! You can now set up a time for your chat. Click the button below to do so.\n\nChat Riddle: `Disabled` 🛑\nChat Riddle Time: `{time}` ⏰"
             return await query.message.edit(
                       text=change_font(txt),
                       reply_markup=InlineKeyboardMarkup(button)
             )


@bot.on_callback_query(filters.regex('^rmtime'))
async def set_riddle_chat_time(_, query):
       user_id = query.from_user.id
       chat_id = query.message.chat.id
       
        
       admin_id = int(query.data.split(':')[1])
       if user_id != admin_id:
             return await query.answer(
               text=change_font("🔐 Sorry this not for you. try your own to customize.")
               , show_alert=True)
       else:
           time = int(query.data.split(':')[2])
           await on_chat(chat_id, mode, type, time)
           riddle = await is_chat(chat_id, mode, type) 
           time = await get_chat_sleep(chat_id, mode, type) 
           button = [[
                   InlineKeyboardButton(
                     change_font('Back ⬅️'), callback_data=f'rmath:{user_id}')

           ]]
           txt = f"Successfully set up chat math riddle!\n\nRiddle: `Enabled` 📢\nRiddle time: `{time}` ⏰"
           return await query.message.edit(
                   text=change_font(txt),
                   reply_markup=InlineKeyboardMarkup(button)
           )
                                



@bot.on_callback_query(filters.regex('^rmoff'))
async def off_riddle_chat(_, query):
       user_id = query.from_user.id
       chat_id = query.message.chat.id
      
       admin_id = int(query.data.split(':')[1])
       if user_id != admin_id:
             return await query.answer(
               text=change_font("🔐 Sorry this not for you. try you're own to customize.")
               , show_alert=True)
       else:
            await off_chat(chat_id, mode, type)
            await clear_chat_data(chat_id, mode, type)
            time = await get_chat_sleep(chat_id, mode, type)
            txt = f"Successfully turned off chat math riddle!\n\nChat riddle: `Disabled` 🛑\nChat riddle time: `{time}` 🛑"
            await query.message.edit(
                      text=change_font(txt)  
            )
            if chat_id in chats_id:
                   await bot.send_message(
                       chat_id=chat_id,
                          text=change_font('Ok. R-M 🔴')
                        )
                   chats_id[chat_id].cancel()
                   del chats_id[chat_id]
                   return await clear_chat_data(chat_id, mode, type)
             




        
async def send_math_riddle_tochat(chat_id: int):  
        
       lock = asyncio.Lock()
       async with lock:
           while True:                                 
               sleep_time = int(await get_chat_sleep(chat_id, mode, type))
               riddle = await make_math_riddle(chat_id)

               question = riddle[2]
               answer = riddle[1]
               photo = riddle[0]   
               
               msg = await bot.send_photo(
                    chat_id=chat_id,
                    photo=photo, 
                    caption=change_font("✨ Solve the Riddle ✨")
               )
               await save_chat_data(
                  chat_id=chat_id,
                  mode=mode,
                  type=type,
                  question=question,
                  answer=answer,
                  msg_time=str(msg.date).split()[1]
          )
               os.remove(photo)
               await asyncio.sleep(sleep_time)
               await clear_chat_data(chat_id, mode, type)
               await msg.delete()
               
          
               
               
               
               
               
               
@bot.on_message(filters.all & ~filters.bot & ~filters.private, group=2)
async def sends_math_riddle(_, message):
      chat_id = message.chat.id
      if not chat_id in chats_id:
            riddle = await is_chat(chat_id, mode, type)
            if riddle == 'on':
                  await clear_chat_data(chat_id, mode, type)
                  chats_id[chat_id] = asyncio.create_task(send_math_riddle_tochat(chat_id))
                  print(f"{type.capitalize()} task added in {message.chat.title}")
      else:
         return 
      





