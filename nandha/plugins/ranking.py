
import config
from pyrogram import filters
from nandha.helpers.decorator import admin_only
from nandha.helpers.func import get_rmath_lb
from nandha import bot



@bot.on_message(filters.command('leaderboard', prefixes=config.PREFIXES) & ~filters.private)
@admin_only
async def leaderboard(_, message):
       chat_id = message.chat.id
       name = message.chat.title
       data = await get_rmath_lb(chat_id)
       text = '🏆 Top Users in {name}\n'
       for i, (user_id, points) in enumerate(sorted_user_riddle_points[:10]):
              text += f'{i+1}. {user_id}: {points}\n'
       await message.reply(text)
       
