


from nandha import DATABASE

db = DATABASE['CHATS']



async def is_chat_riddle(chat_id: int):
    json = {'chat_id': chat_id}
    riddle = db.find_one(json)
    if riddle:
         return riddle['data']['riddle']['math']['switch']        
    else:
        return None


async def get_chat_time(chat_id: int):
    json = {'chat_id': chat_id}
    riddle = db.find_one(json)
    if riddle:
        return riddle['data']['riddle']['math']['time']
    else:
        return None
        
