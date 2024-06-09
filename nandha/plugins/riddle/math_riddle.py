
import os
import config
import asyncio
import random

from pyrogram import filters 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from nandha.database.riddle.math_riddle import is_chat_riddle, get_chat_sleep, off_chat, on_chat, save_chat_riddle, clear_chat_riddle, get_chat_riddle
from nandha.database.points import add_points, get_points
from nandha.database.chats import add_chat
from nandha.helpers.func import get_question, ask_start_pm, make_math_riddle
from nandha import bot, DATABASE

chats_id = {}




@bot.on_message(filters.text & ~filters.private & ~filters.bot, group=-2 )
async def check_user_rmath_ans(_, message):
        chat_id = message.chat.id
        
        
        if not chat_id in chats_id:
               return
        else:
            riddle = list(await get_chat_riddle(chat_id))
            if riddle == False:
                    return
            else:
                 answer = int(riddle[1])
                 start_time = str(riddle[2])
                    
                 if message.sender_chat:
                         return
                                  
                 try:
                    text = int(message.text)
               
                    if text == int(answer):
                         mention = message.from_user.mention
                         user_id = message.from_user.id
                         first_name = message.from_user.first_name
                         msg_id = message.id
                            
                         if (await ask_start_pm(user_id, message)) == False:
                                return 

                         db = DATABASE['USERS']
                           # for update the user name in db whenever he/she answered the riddle
                         db.update_one(
                                 {'user_id': user_id},
                                 {'$set': {'data.first_name': first_name}}
                         )
                         try:
                            await bot.send_reaction(
                                 chat_id=chat_id, 
                                 message_id=msg_id, 
                                 emoji=random.choice(config.EMOJI), 
                                 big=True
                         )
                         except: pass
                         end_time = str(message.date).split()[1]
                         a_time = await taken_time(
                                start_time=start_time, 
                                 end_time=end_time
                        ) 
                         await clear_chat_riddle(chat_id)
                         await add_points(chat_id, user_id, 'riddle', 'math')
                         points = await get_points(chat_id, user_id, 'riddle', 'math')
                         
                         await message.reply_animation(animation=config.RIDDLE_ANSWER_GIF,
                                 caption=f"🥳 **Congratulation {mention}, You have answered first 🥇 THE MATH RIDDLE** 🥇.\n\n🧠 **Solved Puzzles**: {points}\n🧠 **Taken Time**: {a_time}"
                         ) 
                 except Exception as e:
                         pass
                 


@bot.on_callback_query(filters.regex('^rmath'))
async def riddle_math(_, query):
      user_id = query.from_user.id
      chat_id = query.message.chat.id
        
      admin_id = int(query.data.split(':')[1])
      if user_id != admin_id:
            return await query.answer("🔐 Sorry this not for you. try you're own to customize.", show_alert=True)
      else:
         riddle = await is_chat_riddle(chat_id)
         time = await get_chat_sleep(chat_id)
         button = [[
           InlineKeyboardButton(text='60 Sec', callback_data=f'rmtime:{user_id}:60'),
           InlineKeyboardButton(text='3 Min', callback_data=f'rmtime:{user_id}:90'),],
                   [InlineKeyboardButton(text='10 Min', callback_data=f'rmtime:{user_id}:600'),
                    InlineKeyboardButton(text='30 Min', callback_data=f'rmtime:{user_id}:1800'), ],
                   [ InlineKeyboardButton(text='Back ⬅️', callback_data=f'cb_riddle:{user_id}')
           
]]
            
         off_button = [[
               InlineKeyboardButton(text='OFF 🛑', callback_data=f'rmoff:{user_id}'),
               InlineKeyboardButton(text='Back ⬅️', callback_data=f'cb_riddle:{user_id}')
 ]]
         if riddle == 'on':
               return await query.message.edit(
                     "This chat has already set up the timing for sending math riddles. To change the settings, turn them off and try again.",
                     reply_markup=InlineKeyboardMarkup(off_button))
                     
         else:
             return await query.message.edit(
                f"Hello! You can now set up a time for your chat. Click the button below to do so.\n\nChat Riddle: `Disabled` 🛑\nChat Riddle Time: `{time}` ⏰",
                reply_markup=InlineKeyboardMarkup(button)
             )


@bot.on_callback_query(filters.regex('^rmtime'))
async def set_riddle_chat_time(_, query):
       user_id = query.from_user.id
       chat_id = query.message.chat.id
       
        
       admin_id = int(query.data.split(':')[1])
       if user_id != admin_id:
             return await query.answer("🔐 Sorry this not for you. try your own to customize.", show_alert=True)
       else:
           time = int(query.data.split(':')[2])
           await on_chat(chat_id, time)
           riddle = await is_chat_riddle(chat_id) 
           time = await get_chat_sleep(chat_id) 
           button = [[
                   InlineKeyboardButton('Back ⬅️', callback_data=f'rmath:{user_id}')

           ]]
           return await query.message.edit(
                  f"Successfully set up chat math riddle!\n\n<b>Riddle is</b>: `Enabled` 📢\n<b>Riddle time</b>: `{time}` ⏰",
                   reply_markup=InlineKeyboardMarkup(button)
           )
                                



@bot.on_callback_query(filters.regex('^rmoff'))
async def off_riddle_chat(_, query):
       user_id = query.from_user.id
       chat_id = query.message.chat.id
      
       admin_id = int(query.data.split(':')[1])
       if user_id != admin_id:
             return await query.answer("🔐 Sorry this not for you. try you're own to customize.", show_alert=True)
       else:
            await off_chat(chat_id)
            await clear_chat_riddle(chat_id)  
            await query.message.edit(
                 f"Successfully turned off chat math riddle!\n\n<b>Chat riddle is</b>: `Disabled` 🛑\n<b>Chat riddle time</b>: `{time}` 🛑",
           )
            if chat_id in chats_id:
                   await bot.send_message(
                       chat_id=chat_id,
                          text='**Ok. R-M** 🔴'
                        )
                   chats_id[chat_id].cancel()
                   del chats_id[chat_id]
                   return await clear_chat_riddle(chat_id)
             




        
async def send_math_riddle_tochat(chat_id: int):  
        
       lock = asyncio.Lock()
       async with lock:
           while True:                                 
               sleep_time = int(await get_chat_sleep(chat_id))
               riddle = await make_math_riddle(chat_id)

               question = riddle[2]
               answer = riddle[1]
               photo = riddle[0]   
               
               msg = await bot.send_photo(
                    chat_id=chat_id,
                    photo=photo, 
                    caption="<code>🔥 Solve the Riddle 🔥</code>")
               await save_chat_riddle(
                  chat_id=chat_id,
                  question=question,
                  answer=answer,
                  msg_time=str(msg.date).split()[1]
          )
               os.remove(photo)
               await asyncio.sleep(sleep_time)
               await clear_chat_riddle(chat_id)
               try:      
                 await msg.delete()
               except: pass
          
               
               
               
               
               
               
@bot.on_message(filters.all & ~filters.bot & ~filters.private, group=2)
async def sends_math_riddle(_, message):
      chat_id = message.chat.id
      if not chat_id in chats_id:
            riddle = await is_chat_riddle(chat_id)
            if riddle == 'on':
                  await clear_chat_riddle(chat_id)
                  chats_id[chat_id] = asyncio.create_task(send_math_riddle_tochat(chat_id))                  
      else:
         return 
      





