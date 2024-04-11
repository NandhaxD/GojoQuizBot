
import config
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from nandha.helpers.decorator import admin_only
from nandha.helpers.func import get_rmath_lb
from nandha.database.chats import add_chat
from nandha import bot



@bot.on_message(filters.command('leaderboard', prefixes=config.PREFIXES) & ~filters.private)
@admin_only
async def leaderboard(_, message):
         user_id = message.from_user.id
         chat_id = message.chat.id
         
         button = [[
                InlineKeyboardButton('Riddle', callback_data=f'riddlelb:{user_id}'),
                InlineKeyboardButton('Quiz', callback_data=f'quizelb:{user_id}')
         ]]
         await add_chat(chat_id)
         return await message.reply(
                'To Check the top users in chat click below button.',
                reply_mark=InlineKeyboardMarkup(button)
         )


@bot.on_callback_query(filters.regex('^riddlelb'))
async def riddlelb(_, query):
       user_id = query.from_user.id
       admin_id = int(query.data.split(':')[1])
       if user_id != admin_id:
              return await query.answer(
                     'This command is not requested by you', show_alert=True
              )
       else:
            button = [[
             InlineKeyboardButton('Math leaderboard', callback_data=f'rmathlb:{user_id}')
                   
            ]]
            return await query.message.edit(
                   'Click here for know the chat top users 🏆',
                   reply_markup=InlineKeyboardMarkup(button)
            )
            
       
                     
@bot.on_callback_query(filters.regex('^rmathlb'))
async def rmath_leaderboard(_, query):
       user_id = query.from_user.id
       admin_id = int(query.data.split(':')[1])
       if user_id != admin_id:
              return await query.answer(
                     'This command is not requested by you', show_alert=True
              )
       else:
           chat_id = query.message.chat.id
           name = query.message.chat.title
           sorted_user_riddle_points = await get_rmath_lb(chat_id)
           text = '🏆 Top Users in {name}\n'
           for i, (user, points) in enumerate(sorted_user_riddle_points[:10]):
              text += f'{i+1}. {user}: `{points}`\n'

           button = [[ InlineKeyboardButton('Back ⬅️', callback_data=f'riddlelb':{user_id}') ]]
           return await query.message.edit(text,
                                    reply_markup=InlineKeyboardMarkup(button)
                                          )
       

       

       
       
