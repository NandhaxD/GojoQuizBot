
import config

from nandha.database.users import get_users
from nandha.database.chats import get_chats
from pyrogram import filters
from nandha import bot


@bot.on_message(filters.command('statics', prefixes=config.PREFIXES))
async def statics(_, message):
      if message.from_user.id != config.OWNER_ID:
            return await message.reply('Only owner can use this command', quote=True)
      users = len(await get_users())
      chats = len(await get_chats())
      return await message.reply(
         f'Users: {users}\n'
         f'Chats: {chats}\n'
         '@Nandhabots'
      )
      


