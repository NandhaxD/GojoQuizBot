from pyrogram.types import Message
from nandha import bot


async def is_stuffs(chat_id: int, user_id: int):
     user = await bot.get_chat_member(chat_id, user_id)
     is_admin = user.status == enums.ChatMemberStatus.ADMINISTRATOR
     is_owner = user.status == enums.ChatMemberStatus.OWNER
     if (is_admin or is_owner) is True:
           return True, user
     else:
           return False
     
     
