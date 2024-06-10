

from pyrogram import filters, types, enums, errors
from nandha import bot

import random



async def react(message):
    try:
      await message.react(
         emoji=random.choice(config.EMOJI),
         big=True
       )
    except:
       pass

        
          
  
