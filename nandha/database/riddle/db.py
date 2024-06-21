


from nandha import DATABASE

db = DATABASE['CHATS']

async def save_chat_data(chat_id: int, mode: str, type: str, question, answer, msg_time):
    json = {'chat_id': chat_id}
    update = {'$set': {
        f'data.{mode}.{type}.question': question,
        f'data.{mode}.{type}.answer': answer,
        f'data.{mode}.{type}.msg_time': msg_time}
             }
    db.update_one(json, update)
    return True

async def get_chat_data(chat_id: int, mode: str, type: str):
       json = {'chat_id': chat_id}
       chat = db.find_one(json)
       if chat:
           question = chat['data'][mode][type]['question']
           answer = chat['data'][mode][type]['answer']
           taken_time = chat['data'][mode][type]['msg_time']
           return question, answer, taken_time
       else:
           return False
           
    
async def clear_chat_data(chat_id: int, mode: str, type: str):
    json = {'chat_id': chat_id}
    update = {'$set': {
        f'data.{mode}.{type}.question': False,
        f'data.{mode}.{type}.answer': False,
        f'data.{mode}.{type}.msg_time': False}
             }
    db.update_one(json, update)
    return True
                       

async def is_chat_data(chat_id: int):
    json = {'chat_id': chat_id}
    chat = db.find_one(json)
    if bool(chat): return riddle['data']['riddle']['math']['switch']
    else: return False

async def off_chat(chat_id: int, mode: str, type: str):
    json = {'chat_id': chat_id}
    updated_json = {
        '$set': {
            f'data.{mode}.{type}.sleep': False,
            f'data.{mode}.{type}.switch': False,
            f'data.{mode}.{type}.msg_time': False}}
    riddle = db.update_one(json, updated_json)
    return True
    
async def on_chat(chat_id: int, mode: str, type: str, time: int):
    json = {'chat_id': chat_id}
    updated_json = {
        '$set': {
            f'data.{mode}.{type}.sleep': time,
            f'data.{mode}.{type}.switch': True
        }}
    riddle = db.update_one(json, updated_json)
    return True
    
                        
async def get_chat_sleep(chat_id: int, mode: str, type: str):
    json = {'chat_id': chat_id}
    riddle = db.find_one(json)
    if chat:
        return chat['data'][mode][type]['sleep']
    else:
        return False


