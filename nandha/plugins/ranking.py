
import config
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from nandha.helpers.decorator import admin_only
from nandha.helpers.leaderboard import (
get_riddle_group, get_riddle_global
)
from nandha.database.chats import add_chat
from nandha.helpers.scripts import react
from nandha import bot



@bot.on_message(filters.command(['tops','top', 'leaderboard'], prefixes=config.PREFIXES) & ~filters.private)
async def leaderboard(_, message):
         user_id = message.from_user.id
         chat_id = message.chat.id
         await react(message)
         button = [[
                InlineKeyboardButton('🌟 Riddle', callback_data=f'riddletop:{user_id}'),
                InlineKeyboardButton('💫 Quiz', callback_data=f'quiztop:{user_id}')
         ]]
         await add_chat(chat_id)
         return await message.reply(
                'To Check The Top Users In Chat Click Below Button.',
                reply_markup=InlineKeyboardMarkup(button)
         )


@bot.on_callback_query(filters.regex('^riddletop'))
async def riddletop(_, query):
       user_id = query.from_user.id
       admin_id = int(query.data.split(':')[1])

       if user_id != admin_id:
              return await query.answer(
                     'This command is not requested by you', show_alert=True
              )
       else:
                
            button = [[
             InlineKeyboardButton('𝗖𝗵𝗮𝘁 𝗥-𝗠', callback_data=f'rmathtop:{admin_id}'),
             InlineKeyboardButton('𝗚𝗹𝗼𝗯𝗮𝗹 𝗥-𝗠', callback_data=f'rmathgtop:{admin_id}'),
             InlineKeyboardButton('𝗖𝗵𝗮𝘁 𝗥-𝗪', callback_data=f'rwordstop:{admin_id}'),
             InlineKeyboardButton('𝗚𝗹𝗼𝗯𝗮𝗹 𝗥-𝗪', callback_data=f'rwordsgtop:{admin_id}')       
                   
            ]]
            name = query.message.chat.title
            return await query.message.edit(
                   f'**Click Here to See Global Top Users & Group Top Users!**',
                   reply_markup=InlineKeyboardMarkup(button)
            )
            
       
                     
@bot.on_callback_query(filters.regex('^rmathtop'))
async def rmath_top(_, query):
       user_id = query.from_user.id
       admin_id = int(query.data.split(':')[1])
       if user_id != admin_id:
              return await query.answer(
                     'This command is not requested by you', show_alert=True
              )
       else:
           chat_id = query.message.chat.id
           name = query.message.chat.title
           sorted_user_riddle_points = await get_riddle_group(chat_id=chat_id, type='math')
           text = f'🏆 ** Chat Top R-M Users in {name}** 👥\n\n'
           for i, (user_id, points) in enumerate(sorted_user_riddle_points[:15]):
              if str(user_id).isdigit():                       
                 text += f'{i+1}. **[{user_id}](tg://user?id={user_id})**: `{points}`\n'
              else:
                 text += f'{i+1}, **{user_id}**: `{points}`\n'
                       

           button = [[ InlineKeyboardButton('Back ⬅️', callback_data=f'riddletop:{admin_id}') ]]
           return await query.message.edit(text,
                                    reply_markup=InlineKeyboardMarkup(button)
                                          )


@bot.on_callback_query(filters.regex('^rmathgtop'))
async def rmath_gtop(_, query):
       user_id = query.from_user.id
       admin_id = int(query.data.split(':')[1])
       if user_id != admin_id:
              return await query.answer(
                     'This command is not requested by you', show_alert=True
              )
       else:
           name = query.message.chat.title
           text = f'🏆 **Global Top R-M Users In {name}**\n\n'
           sorted_leaderboard = await get_riddle_global(type='math')
           for i, (user_id, points) in enumerate(sorted_leaderboard.items()):
                  if i >= 15:
                     break
                  if str(user_id).isdigit():
                       text += f'{i+1}, **[{user_id}](tg://user?id={user_id})**: {points}\n'
                  else:
                       text += f'{i+1}, **{user_id}**: `{points}`\n'
                       

           button = [[ InlineKeyboardButton('Back ⬅️', callback_data=f'riddletop:{admin_id}') ]]
           return await query.message.edit(text,
                                    reply_markup=InlineKeyboardMarkup(button)
                                          )


       
@bot.on_callback_query(filters.regex('^rwordstop'))
async def rwords_top(_, query):
       user_id = query.from_user.id
       admin_id = int(query.data.split(':')[1])
       if user_id != admin_id:
              return await query.answer(
                     'This command is not requested by you', show_alert=True
              )
       else:
           chat_id = query.message.chat.id
           name = query.message.chat.title
           sorted_user_riddle_points = await get_riddle_group(chat_id=chat_id, type='words')
           text = f'🏆 **Chat Top R-W Users In {name}** 👥\n\n'
           for i, (user_id, points) in enumerate(sorted_user_riddle_points[:15]):
              if str(user_id).isdigit():                       
                 text += f'{i+1}. **[{user_id}](tg://user?id={user_id})**: `{points}`\n'
              else:
                 text += f'{i+1}, **{user_id}**: `{points}`\n'
                       

           button = [[ InlineKeyboardButton('Back ⬅️', callback_data=f'riddletop:{admin_id}') ]]
           return await query.message.edit(text,
                                    reply_markup=InlineKeyboardMarkup(button)

@bot.on_callback_query(filters.regex('^rwordsgtop'))
async def rwords_gtop(_, query):
       user_id = query.from_user.id
       admin_id = int(query.data.split(':')[1])
       if user_id != admin_id:
              return await query.answer(
                     'This command is not requested by you', show_alert=True
              )
       else:
           name = query.message.chat.title
           text = f'🏆 **Global Top R-W Users in {name}**\n\n'
           sorted_leaderboard = await get_riddle_global(type='words')
           for i, (user_id, points) in enumerate(sorted_leaderboard.items()):
                  if i >= 15:
                     break
                  if str(user_id).isdigit():
                       text += f'{i+1}, **[{user_id}](tg://user?id={user_id})**: {points}\n'
                  else:
                       text += f'{i+1}, **{user_id}**: `{points}`\n'
                       

           button = [[ InlineKeyboardButton('Back ⬅️', callback_data=f'riddletop:{admin_id}') ]]
           return await query.message.edit(text,
                                    reply_markup=InlineKeyboardMarkup(button)

       
