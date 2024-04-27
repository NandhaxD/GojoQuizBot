
import config

from pyrogram import enums
from pyrogram.types import Message
from nandha import bot


async def is_stuffs(chat_id: int, user_id: int):
     user = await bot.get_chat_member(chat_id, user_id)
     is_admin = user.status == enums.ChatMemberStatus.ADMINISTRATOR
     is_owner = user.status == enums.ChatMemberStatus.OWNER
     if (is_admin or is_owner) is True:
           return [True, user]
     else:
           return [False]


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
              
             if message.chat.type==enums.ChatType.PRIVATE: 
                 return await message.reply(
                      'This command only work in groups.'
                 )            
             user = await is_stuffs(chat_id, user_id)
             if bool(user[0]) is not True:
                    return await message.reply(
                         "You're not admin."
                    )
             return await func(bot, message)                 
         return wrapped
     
     
