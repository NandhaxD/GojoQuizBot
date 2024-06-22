


from nandha import DATABASE

db = DATABASE['CHATS']


async def save_chat_data(chat_id: int, mode: str, type: str, answer, msg_time, question=None):
    json = {'chat_id': chat_id}
  
    update = {'$set': {
        f'data.{mode}.{type}.answer': answer,
        f'data.{mode}.{type}.msg_time': msg_time
    }}
    
    if question is not None:
        update['$set'][f'data.{mode}.{type}.question'] = question
    
    await db.update_one(json, update)
    return True


async def get_chat_data(chat_id: int, mode: str, type: str):
    json = {'chat_id': chat_id}
    chat = db.find_one(json)  # Assuming this is an async call
    if chat:
        data = chat['data'][mode][type]
        question = data.get('question')
        answer = data['answer']
        taken_time = data['msg_time']
        if question is not None:
            return question, answer, taken_time
        else:
            return answer, taken_time
    else:
        return False



async def clear_chat_data(chat_id: int, mode: str, type: str):
    json = {'chat_id': chat_id}
    update = {
        '$set': {
            f'data.{mode}.{type}.answer': False,
            f'data.{mode}.{type}.msg_time': False
        }
    }

    # Fetch the chat data to check if the question exists
    chat = db.find_one(json)
    if chat and 'question' in chat['data'][mode][type]:
        update['$set'][f'data.{mode}.{type}.question'] = False

    await db.update_one(json, update)
    return True
  
                       

async def is_chat(chat_id: int, mode: str, type: str):
    json = {'chat_id': chat_id}
    chat = db.find_one(json)
    if bool(chat): return chat.get('data', {}).get(mode, {}).get(type, {}).get('switch', False)
    else: return False


async def off_chat(chat_id: int, mode: str, type: str):
    json = {'chat_id': chat_id}
    updated_json = {
        '$set': {
            f'data.{mode}.{type}.sleep': False,
            f'data.{mode}.{type}.switch': False,
            f'data.{mode}.{type}.msg_time': False
        }
    }
    db.update_one(json, updated_json)
    return True
    
async def on_chat(chat_id: int, mode: str, type: str, time: int):
    json = {'chat_id': chat_id}
    updated_json = {
        '$set': {
            f'data.{mode}.{type}.sleep': time,
            f'data.{mode}.{type}.switch': True
        }}
    db.update_one(json, updated_json)
    return True
    
                        
async def get_chat_sleep(chat_id: int, mode: str, type: str):
    json = {'chat_id': chat_id}
    chat = db.find_one(json)
    if chat:
        return chat.get('data', {}).get(mode, {}).get(type, {}).get('sleep', False)
    else:
        return False

