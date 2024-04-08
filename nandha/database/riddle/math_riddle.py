


from nandha import DATABASE

db = DATABASE['CHATS']

async def get_chat_timeline(chat_id: int):
    json = {'chat_id': chat_id}
    riddle = db.find_one(json)
    if riddle:
        return riddle['data']['riddle']['math']['time']
    else:
        return False
