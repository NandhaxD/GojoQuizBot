from nandha import DATABASE

db = DATABASE['CHATS']


async def get_chats() -> list:
   chats_id = [chats['chat_id'] for chats in db.find()]
   return chats_id
  


async def add_chat(chat_id: int):
    json_data = {
    'chat_id': chat_id,
    'data': {
        'riddle': {
            'math': {'switch': 'off', 'time': False, 'question': False, 'answer': False, 'msg_time': False}
        },
        'quize': {
            'math': {'switch': 'off', 'time': False},
            'phy': {'switch': 'off', 'time': False},
            'chem': {'switch': 'off', 'time': False},
            'zoo': {'switch': 'off', 'time': False}
        }
    }
    }
    chats_id = await get_chats()
    if not chat_id in chats_id:
        db.insert_one(json_data)
        return True
    else:
        return

async def remove_chat(chat_id: int):
     json = {'chat_id': chat_id}
     is_exsited = db.find_one(json)
     if is_exsited:
           db.delete_one(json)
           return True
     else:
         return 
       
  
