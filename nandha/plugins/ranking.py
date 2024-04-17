
import config
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from nandha.helpers.decorator import admin_only
from nandha.helpers.leaderboard import get_rmath_top, get_rmath_gtop
from nandha.database.chats import add_chat
from nandha import bot



@bot.on_message(filters.command('tops', prefixes=config.PREFIXES) & ~filters.private)
async def leaderboard(_, message):
         user_id = message.from_user.id
         chat_id = message.chat.id
         
         button = [[
                InlineKeyboardButton('Riddle', callback_data=f'riddletop:{user_id}'),
                InlineKeyboardButton('Quiz', callback_data=f'quiztop:{user_id}')
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
             InlineKeyboardButton('Group R-M 👥', callback_data=f'rmathtop:{user_id}'),
             InlineKeyboardButton('Global R-M 👥', callback_data=f'rmathgtop:{user_id}')
                   
            ]]
            name = query.message.chat.title
            return await query.message.edit(
                   f'Click Here For Know Global Top / Group Top Users',
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
           sorted_user_riddle_points = await get_rmath_top(chat_id)
           text = f'🏆 **Top R-M Users in {name}** 👥\n\n'
           for i, (user, points) in enumerate(sorted_user_riddle_points[:10]):
              text += f'{i+1}. [{user}](tg://user?id={user}): `{points}`\n'

           button = [[ InlineKeyboardButton('Back ⬅️', callback_data=f'riddlelb:{user_id}') ]]
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
           text = f'🏆 **Top Global Riddle Math Users** 👥\n\n'
           sorted_leaderboard = await get_rmath_gtop()
           for i, (user_id, point) in enumerate(sorted_leaderboard.items()):
                  if i >= 10:
                     break
                  text += f'{i+1}, [{user_id}](tg://user?id={user_id}): {point}\n'

           button = [[ InlineKeyboardButton('Back ⬅️', callback_data=f'riddletop:{user_id}') ]]
           return await query.message.edit(text,
                                    reply_markup=InlineKeyboardMarkup(button)
                                          )


       

       
       
