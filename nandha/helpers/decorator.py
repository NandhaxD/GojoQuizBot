
import config

from pyrogram import enums
from pyrogram.types import Message
from nandha import bot


async def is_stuffs(chat_id: int, user_id: int):
     userinfo = await bot.get_chat_member(chat_id, user_id)
     if userinfo.status in (enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER):
          return True, userinfo
     else:
          return False, userinfo


def devs_only(func):
     async def wrapped(bot: bot, message: Message):
          chat_id = message.chat.id
          user_id = message.from_user.id
          if not user_id in config.DEVS_ID:
              return
          return await func(bot, message)
     return wrapped
          

def admin_only(func): 
         async def wrapped(bot: bot, message: Message): 
             chat_id= message.chat.id 
             user_id= message.from_user.id          
             is_admin, userinfo = await is_stuffs(chat_id, user_id)
             if not is_admin:
                    return await message.reply(
                         "You're not admin."
                    )
             return await func(bot, message)                 
         return wrapped
     
     
