
import config
from pyrogram import filters, types
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from nandha.helpers.decorator import admin_only
from nandha.helpers.leaderboard import (
get_riddle_group, get_riddle_global
)
from nandha.database.chats import add_chat
from nandha.helpers.scripts import react
from nandha.helpers.func import change_font
from nandha import bot



@bot.on_message(filters.command(['tops','top', 'leaderboard'], prefixes=config.PREFIXES) & ~filters.private)
async def leaderboard(_, message):
         user_id = message.from_user.id
         chat_id = message.chat.id
         await react(message)
         button = [[
                InlineKeyboardButton(change_font('🌟 Riddle'), callback_data=f'riddletop:{user_id}'),
                InlineKeyboardButton(change_font('💫 Quiz'), callback_data=f'quiztop:{user_id}')
         ]]
         await add_chat(chat_id)
         photo_url = config.LB_IMG
         return await message.reply_photo(
                photo=photo_url,
                caption=change_font('To Check The Top Users In Chat Click Below Button.'),
                reply_markup=InlineKeyboardMarkup(button)
         )


@bot.on_callback_query(filters.regex('^riddletop'))
async def riddletop(_, query):
       user_id = query.from_user.id
       admin_id = int(query.data.split(':')[1])

       if user_id != admin_id:
              return await query.answer(
                     text=('This command is not requested by you')
                       , show_alert=True
              )
       else:
                
            button = [[
             InlineKeyboardButton(change_font('Chat R-M'), callback_data=f'rmathtop:{admin_id}'),
             InlineKeyboardButton(change_font('Global R-M'), callback_data=f'rmathgtop:{admin_id}'),
            ],[
             InlineKeyboardButton(change_font('Chat R-W'), callback_data=f'rwordstop:{admin_id}'),
             InlineKeyboardButton(change_font('Global R-W'), callback_data=f'rwordsgtop:{admin_id}')       
                   
            ]]
            name = query.message.chat.title
            return await query.message.edit_caption(
                   caption=change_font(f'**Click Here to See Global Top Users & Group Top Users!**'),
                   reply_markup=InlineKeyboardMarkup(button)
            )
            
       
                     
@bot.on_callback_query(filters.regex('^rmathtop'))
async def rmath_top(_, query):
       user_id = query.from_user.id
       admin_id = int(query.data.split(':')[1])
       if user_id != admin_id:
              return await query.answer(
                     text=change_font('This command is not requested by you'), show_alert=True
              )
       else:
           chat_id = query.message.chat.id
           chat_name = query.message.chat.title
           await query.message.edit_caption(
                    caption=change_font("⏳ Analyzing Leaderboard....")
           )
           
           sorted_user_riddle_points = await get_riddle_group(chat_id=chat_id, type='math')
           photo_url = await generate_lb_image(chat_id=chat_id, chat_name=chat_name, sorted_user_riddle_points=sorted_user_riddle_points, type='Math')
           text = change_font(f'🏆 ** Chat Top Riddle Math Users in {chat_name}** ✨\n\n')
           for i, (user_id, points) in enumerate(sorted_user_riddle_points[:10]):
              if str(user_id).isdigit():                       
                 text += f'{i+1}. **[{user_id}](tg://user?id={user_id})**: `{points}`\n'
              else:
                 text += f'{i+1}, **{user_id}**: `{points}`\n'
                       

           button = [[ InlineKeyboardButton(change_font('BACK ⬅️'), callback_data=f'riddletop:{admin_id}') ]]
           return await query.message.edit_media(
                    media=types.InputMedia(
                     types.InputMediaPhoto(
                           media=photo_url,
                           caption=text
                     )),
                 reply_markup=InlineKeyboardMarkup(button)
                     )


@bot.on_callback_query(filters.regex('^rmathgtop'))
async def rmath_gtop(_, query):
       user_id = query.from_user.id
       admin_id = int(query.data.split(':')[1])
       if user_id != admin_id:
              return await query.answer(
                     text=change_font('This command is not requested by you')
                       , show_alert=True
              )
       else:

           await query.message.edit_caption(
                    caption=change_font("⏳ Analyzing Leaderboard....")
           )
           
           sorted_leaderboard = await get_riddle_global(type='math')
           photo_url = await generate_lb_image(sorted_user_riddle_points=sorted_user_riddle_points, type='Math')  
           text = change_font(f'🏆 **Global Top Riddle math Users ✨**\n\n')
           
           for i, (user_id, points) in enumerate(sorted_leaderboard.items()):
                  if i >= 10:
                     break
                  if str(user_id).isdigit():
                       text += f'{i+1}, **[{user_id}](tg://user?id={user_id})**: {points}\n'
                  else:
                       text += f'{i+1}, **{user_id}**: `{points}`\n'
                       

           button = [[ InlineKeyboardButton(change_font('BACK ⬅️'), callback_data=f'riddletop:{admin_id}') ]]
           return await query.message.edit_media(
                    media=types.InputMedia(
                     types.InputMediaPhoto(
                           media=photo_url,
                           caption=text
                     )),
                 reply_markup=InlineKeyboardMarkup(button)
           )

       
@bot.on_callback_query(filters.regex('^rwordstop'))
async def rwords_top(_, query):
       user_id = query.from_user.id
       admin_id = int(query.data.split(':')[1])
       if user_id != admin_id:
              return await query.answer(
                     text=change_font('This command is not requested by you'), show_alert=True
              )
       else:
           chat_id = query.message.chat.id
           chat_name = query.message.chat.title

           await query.message.edit_caption(
                    caption=change_font("⏳ Analyzing Leaderboard....")
           )
                
           sorted_user_riddle_points = await get_riddle_group(chat_id=chat_id, type='words')
           photo_url = await generate_lb_image(chat_id=chat_id, chat_name=chat_name, sorted_user_riddle_points=sorted_user_riddle_points, type='Words')
                
           text = change_font(f'🏆 **Chat Top Riddle Words Users In {chat_name}** ✨\n\n')
           for i, (user_id, points) in enumerate(sorted_user_riddle_points[:10]):
              if str(user_id).isdigit():                       
                 text += f'{i+1}. **[{user_id}](tg://user?id={user_id})**: `{points}`\n'
              else:
                 text += f'{i+1}, **{user_id}**: `{points}`\n'
                       

           button = [[ InlineKeyboardButton(change_font('BACK ⬅️'), callback_data=f'riddletop:{admin_id}') ]]
           return await query.message.edit_media(
                    media=types.InputMedia(
                     types.InputMediaPhoto(
                           media=photo_url,
                           caption=text
                     )),
                 reply_markup=InlineKeyboardMarkup(button)
           )

@bot.on_callback_query(filters.regex('^rwordsgtop'))
async def rwords_gtop(_, query):
       user_id = query.from_user.id
       admin_id = int(query.data.split(':')[1])
       if user_id != admin_id:
              return await query.answer(
                     text=change_font('This command is not requested by you'), show_alert=True
              )
       else:

           await query.message.edit_caption(
                    caption=change_font("⏳ Analyzing Leaderboard....")
           )
                
           text = change_font(f'🏆 **Global Top Riddle Words Users ✨**\n\n')
           sorted_leaderboard = await get_riddle_global(type='words')
           photo_url = await generate_lb_image(sorted_user_riddle_points=sorted_user_riddle_points, type='Words')
           
                
           for i, (user_id, points) in enumerate(sorted_leaderboard.items()):
                  if i >= 10:
                     break
                  if str(user_id).isdigit():
                       text += f'{i+1}, **[{user_id}](tg://user?id={user_id})**: {points}\n'
                  else:
                       text += f'{i+1}, **{user_id}**: `{points}`\n'
                       

           button = [[ InlineKeyboardButton(change_font('BACK ⬅️'), callback_data=f'riddletop:{admin_id}') ]]
           return await query.message.edit_media(
                    media=types.InputMedia(
                     types.InputMediaPhoto(
                           media=photo_url,
                           caption=text
                     )),
                 reply_markup=InlineKeyboardMarkup(button)
           )
       
