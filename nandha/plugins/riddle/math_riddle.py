import io
import os
import requests
import asyncio




from PIL import Image, ImageDraw, ImageFont
from pyrogram import filters 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from nandha.database.riddle.math_riddle import is_chat_riddle, get_chat_time, off_chat, on_chat, save_chat_riddle, clear_chat_riddle, get_chat_riddle
from nandha.database.chats import add_chat
from nandha.helpers.func import get_question
from nandha import bot

chats_id = []



@bot.on_message(filters.text & ~filters.private & ~filters.bot, group=-3)
async def send_math_riddles(_, message):
        chat_id = message.chat.id
        if not chat_id in chats_id:
               return
        else:
            riddle = await get_chat_riddle(chat_id)
            if riddle == False:
                    return
            else:
                 answer = int(riddle[1])
                 mention = message.from_user.mention
                 try:
                    text = int(message.text)                
                    if text == answer:
                         await message.reply(
                                 f'🥳 OwO! {mention} answered the riddle 🧠.')
                         return await clear_chat_riddle(chat_id)
                 except:
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
         time = await get_chat_time(chat_id)
         button = [[
           InlineKeyboardButton(text='60 seconds', callback_data=f'rmtime:{user_id}:60'),
           InlineKeyboardButton(text='1 hour ', callback_data=f'rmtime:{user_id}:3600'),],
                   [InlineKeyboardButton(text='3 hours', callback_data=f'rmtime:{user_id}:10800'),
                    InlineKeyboardButton(text='6 hours', callback_data=f'rmtime:{user_id}:21600'), ],
                   [ InlineKeyboardButton(text='back ⬅️', callback_data=f'cb_riddle:{user_id}')
           
]]
            
         off_button = [[
               InlineKeyboardButton(text='off', callback_data=f'rmoff:{user_id}'),
               InlineKeyboardButton(text='back ⬅️', callback_data=f'cb_riddle:{user_id}')
 ]]
         if riddle == 'on':
               return await query.message.edit(
                     "Hello! This chat has already set up the math riddle time. You need to turn off the current math riddle and try again.",
                     reply_markup=InlineKeyboardMarkup(off_button))
                     
         else:
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
           await on_chat(chat_id, time)
           riddle = await is_chat_riddle(chat_id)
           time = await get_chat_time(chat_id)   
           return await query.message.edit(
                 f"Successfully set-up you're chat math riddle!\n\n<b>You're chat riddle is</b>: {riddle}\n<b>You're chat riddle time</b>: {time}"
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
            riddle = await is_chat_riddle(chat_id)
            time = await get_chat_time(chat_id)   
            return await query.message.edit(
                 f"Successfully turn offend you're chat math riddle!\n\n<b>You're chat riddle is</b>: {riddle}\n<b>You're chat riddle time</b>: {time}"
           )
             

async def make_math_riddle():
     img = Image.open(io.BytesIO(requests.get("https://graph.org/file/9b165baf9de57406d76ca.jpg").content))
     draw = ImageDraw.Draw(img)
     url = "https://github.com/JulietaUla/Montserrat/raw/master/fonts/otf/Montserrat-ExtraBold.otf"
     k = requests.get(url)
     open(url.split("/")[-1], "wb").write(k.content)
     font = ImageFont.truetype(url.split("/")[-1], size=100)
     math = await get_question()
     question = math['query'] + " = ?"
     answer = math['result']
     tbox = font.getbbox(question)
     w = tbox[2] - tbox[0]
     h = tbox[3] - tbox[1]
     # Set the center of the image as the position for the text
     width, height = img.size
     position = (width // 2, height // 2)
     color = (255, 255, 255)
     draw.text(((width-w)//2, (height-h)//2), question, font=font, fill=color)
     img = img.resize((int(width*1.5), int(height*1.5)), Image.LANCZOS)
     path = "rmaths_quiz.jpg"
     img.save(path)    
     return path, answer 


async def send_math_riddle_tochat(chat_id: int):
       while True:
          riddle = await is_chat_riddle(chat_id)
          if riddle == 'off':
                return await bot.send_message(
                      'Ok! stopped math riddle. 🔴'
                )
          time = int(await get_chat_time(chat_id))
          riddle = await make_math_riddle()
          await save_chat_riddle(
                  chat_id=chat_id,
                  question=question,
                  answer=answer
          )
          msg = await bot.send_photo(
                chat_id=chat_id,
                photo=riddle[0], 
                caption="<code>Please don't use any userbot to solve quizzes. If you do, you're preventing yourself from growing.</code>")
          os.remove(riddle[0])
          await asyncio.sleep(time)
          await clear_chat_riddle(chat_id)
          try:      
            await msg.delete()
          except:
                pass


@bot.on_message(filters.text & ~filters.private, group=1)
async def sends_math_riddle(_, message):
      chat_id = message.chat.id
      if not chat_id in chats_id:
            riddle = await is_chat_riddle(chat_id)
            if riddle == 'on':
                  chats_id.append(chat_id)
                  await send_math_riddle_tochat(chat_id)
                  
      else:
         return 
      





