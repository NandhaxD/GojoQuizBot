


from nandha import DATABASE

db = DATABASE['CHATS']

async def save_chat_riddle(chat_id: int, text, msg_time):
    json = {'chat_id': chat_id}
    update = {'$set': {
        'data.riddle.words.text': text,
        'data.riddle.words.msg_time': msg_time}
             }
    db.update_one(json, update, upsert=True)
    return True

async def get_chat_riddle(chat_id: int):
       json = {'chat_id': chat_id}
       riddle = db.find_one(json)
       if riddle:
           question = riddle['data']['riddle']['words']['text']
           taken_time = riddle['data']['riddle']['words']['msg_time']
           return text, taken_time
       else:
           return False
           
    
async def clear_chat_riddle(chat_id: int):
    json = {'chat_id': chat_id}
    update = {'$set': {
        'data.riddle.words.text': False,
        'data.riddle.words.msg_time': False}
             }
    db.update_one(json, update, upsert=True)
    return True
                       


async def is_chat_riddle(chat_id: int):
    json = {'chat_id': chat_id}
    riddle = await db.find_one(json)
    return riddle.get('data', {}).get('riddle', {}).get('words', {}).get('switch', False)



async def off_chat(chat_id: int):
    json = {'chat_id': chat_id}
    updated_json = {
        '$set': {
            'data.riddle.words.sleep': False,
            'data.riddle.words.switch': 'off',
            'data.riddle.words.msg_time': False}}
    riddle = db.update_one(json, updated_json, upsert=True)
    return True
    
async def on_chat(chat_id: int, time: int):
    json = {'chat_id': chat_id}
    updated_json = {
        '$set': {
            'data.riddle.words.sleep': time,
            'data.riddle.words.switch': 'on'
        }}
    riddle = db.update_one(json, updated_json, upsert=True)
    return True
    
                        
async def get_chat_sleep(chat_id: int):
    json = {'chat_id': chat_id}
    riddle = db.find_one(json)
    if riddle:
        return riddle['data']['riddle']['words']['sleep']
    else:
        return False


