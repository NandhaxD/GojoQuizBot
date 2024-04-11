


from nandha import DATABASE

db = DATABASE['CHATS']

async def save_chat_riddle(chat_id: int, question, answer, msg_time):
    json = {'chat_id': chat_id}
    update = {'$set': {
        'data.riddle.math.question': question,
        'data.riddle.math.answer': answer,
        'data.riddle.math.msg_time': msg_time}
             }
    db.update_one(json, update)
    return True

async def get_chat_riddle(chat_id: int):
       json = {'chat_id': chat_id}
       riddle = db.find_one(json)
       if riddle:
           question = riddle['data']['riddle']['math']['question']
           answer = riddle['data']['riddle']['math']['answer']
           taken_time = riddle['data']['riddle']['math']['msg_time']
           return question, answer, taken_time
       else:
           return False
           
    
async def clear_chat_riddle(chat_id: int):
    json = {'chat_id': chat_id}
    update = {'$set': {
        'data.riddle.math.question': False,
        'data.riddle.math.answer': False,
        'data.riddle.math.msg_time': False}
             }
    db.update_one(json, update)
    return True
                       

async def is_chat_riddle(chat_id: int):
    json = {'chat_id': chat_id}
    riddle = db.find_one(json)
    if bool(riddle): return riddle['data']['riddle']['math']['switch']
    else: return False

async def off_chat(chat_id: int):
    json = {'chat_id': chat_id}
    updated_json = {
        '$set': {
            'data.riddle.math.sleep': False,
            'data.riddle.math.switch': 'off',
            'data.riddle.math.msg_time': False}}
    riddle = db.update_one(json, updated_json)
    return True
    
async def on_chat(chat_id: int, time: int):
    json = {'chat_id': chat_id}
    updated_json = {
        '$set': {
            'data.riddle.math.sleep': time,
            'data.riddle.math.switch': 'on'
        }}
    riddle = db.update_one(json, updated_json)
    return True
    
                        
async def get_chat_sleep(chat_id: int):
    json = {'chat_id': chat_id}
    riddle = db.find_one(json)
    if riddle:
        return riddle['data']['riddle']['math']['sleep']
    else:
        return False




from nandha.database.users import add_user
from nandha import DATABASE

db = DATABASE['USERS']



async def get_point_user_chat(chat_id: int, user_id: int):
        filter = {'user_id': user_id}
        user = db.find_one(filter)
        if user:
            point = user['data']['riddle']['math'][str(chat_id)]
            return int(point)
        else:
            return False

    
async def edit_point_user_chat(chat_id: int, user_id: int, point: int):
        filter = {'user_id': user_id}
        user = db.find_one(filter)
        if user:
            update = {'$set':
                      {
                          f'data.riddle.math.{str(chat_id)}': point
                      }}
            db.update_one(user, update)
            return True
        else:
            return False

    

async def add_point_user_chat(chat_id: int, user_id: int):
        filter = {'user_id': user_id}
        user = db.find_one(filter)
        if user:
            point = await get_point_user_chat(chat_id, user_id)
            point += 1
            update = {'$set':
                      {
                          f'data.riddle.math.{str(chat_id)}': point
                      }}
            db.update_one(user, update)
            return True
        else:
             return False
           
           
           
     


        
