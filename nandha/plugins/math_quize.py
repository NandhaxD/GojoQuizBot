#coming


import config

from pyrogram import filters
from nandha import bot

@bot.on_message(filters.command('punda', prefixes=config.PREFIXES))
async def send_punda(_, message):
       return await message.reply('Hi PUNDA')
  
