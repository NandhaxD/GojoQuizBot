


from nandha import DATABASE

db = DATABASE['CHATS']

async def save_chat_riddle(chat_id: int, question, answer, msg_time):
    json = {'chat_id': chat_id}
    update = {'$set': {
        'data.riddle.words.question': question,
        'data.riddle.words.answer': answer,
        'data.riddle.words.msg_time': msg_time}
             }
    db.update_one(json, update)
    return True

async def get_chat_riddle(chat_id: int):
       json = {'chat_id': chat_id}
       riddle = db.find_one(json)
       if riddle:
           question = riddle['data']['riddle']['words']['question']
           answer = riddle['data']['riddle']['words']['answer']
           taken_time = riddle['data']['riddle']['words']['msg_time']
           return question, answer, taken_time
       else:
           return False
           
    
async def clear_chat_riddle(chat_id: int):
    json = {'chat_id': chat_id}
    update = {'$set': {
        'data.riddle.words.question': False,
        'data.riddle.words.answer': False,
        'data.riddle.words.msg_time': False}
             }
    db.update_one(json, update)
    return True
                       

async def is_chat_riddle(chat_id: int):
    json = {'chat_id': chat_id}
    riddle = db.find_one(json)
    if bool(riddle): return riddle['data']['riddle']['words']['switch']
    else: return False

async def off_chat(chat_id: int):
    json = {'chat_id': chat_id}
    updated_json = {
        '$set': {
            'data.riddle.words.sleep': False,
            'data.riddle.words.switch': 'off',
            'data.riddle.words.msg_time': False}}
    riddle = db.update_one(json, updated_json)
    return True
    
async def on_chat(chat_id: int, time: int):
    json = {'chat_id': chat_id}
    updated_json = {
        '$set': {
            'data.riddle.words.sleep': time,
            'data.riddle.words.switch': 'on'
        }}
    riddle = db.update_one(json, updated_json)
    return True
    
                        
async def get_chat_sleep(chat_id: int):
    json = {'chat_id': chat_id}
    riddle = db.find_one(json)
    if riddle:
        return riddle['data']['riddle']['words']['sleep']
    else:
        return False


