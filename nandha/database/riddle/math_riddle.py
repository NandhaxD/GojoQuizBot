


from nandha import DATABASE

db = DATABASE['CHATS']



async def is_chat_riddle(chat_id: int):
    json = {'chat_id': chat_id}
    riddle = db.find_one(json)
    if riddle:
         return riddle['data']['riddle']['math']['switch']        
    else:
        return None



async def off_chat(chat_id: int, time: int):
    json = {'chat_id': chat_id}
    updated_json = {
        '$set': {
            'data.riddle.math.time': False,
            'data.riddle.math.switch': 'off'
        }}
    riddle = db.update_one(json, updated_json)
    return True
    
async def on_chat(chat_id: int, time: int):
    json = {'chat_id': chat_id}
    updated_json = {
        '$set': {
            'data.riddle.math.time': time,
            'data.riddle.math.switch': 'on'
        }}
    riddle = db.update_one(json, updated_json)
    return True
    
                        
async def get_chat_time(chat_id: int):
    json = {'chat_id': chat_id}
    riddle = db.find_one(json)
    if riddle:
        return riddle['data']['riddle']['math']['time']
    else:
        return None
        
