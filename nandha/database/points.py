from nandha.database.users import add_user
from nandha import DATABASE

db = DATABASE['USERS']

async def get_point_user_chat(chat_id: int, user_id: int, module: str, type: str):
        filter = {'user_id': user_id}
        user = db.find_one(filter)
        if user:
            point = user['data'][module][type][str(chat_id)]
            return int(point)
        else:
            return False
    
async def edit_point_user_chat(chat_id: int, user_id: int, point: int, module: str, key: str):
        filter = {'user_id': user_id}
        user = db.find_one(filter)
        if user:
            update = {'$set':
                      {
                          f'data.{module}.{key}.{str(chat_id)}': point
                      }}
            db.update_one(user, update)
            return True
        else:
            return False

async def add_point_user_chat(chat_id: int, user_id: int, module: str, type: str):
        filter = {'user_id': user_id}
        user = db.find_one(filter)
        if user:
            point = await get_point_user_chat(chat_id, user_id, module, type)
            point += 1
            update = {'$set':
                      {
                          f'data.{module}.{key}.{str(chat_id)}': point
                      }}
            db.update_one(user, update)
            return True
        else:
             return False


