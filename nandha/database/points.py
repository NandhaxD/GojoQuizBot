from nandha.database.users import add_user
from nandha import DATABASE

db = DATABASE['USERS']

async def get_points(chat_id: int, user_id: int, module: str, type: str):
        filter = {'user_id': user_id}
        user = db.find_one(filter)
        if user:
            point = user['data'][module][type][str(chat_id)]
            return int(point)
        else:
            return False
    
async def edit_points(chat_id: int, user_id: int, module: str, type: str, point: int):
        filter = {'user_id': user_id}
        user = db.find_one(filter)
        if user:
            update = {'$set':
                      {
                          f'data.{module}.{type}.{str(chat_id)}': point
                      }}
            db.update_one(user, update)
            return True
        else:
            return False

async def add_points(chat_id: int, user_id: int, module: str, type: str):
        filter = {'user_id': user_id}
        user = db.find_one(filter)
        if user:
            try:
               point = await get_points(chat_id, user_id, module, type)
            except:
                update = {'$set':
                      {
                          f'data.{module}.{type}.{str(chat_id)}': 1
                      }}
                db.update_one(user, update)
                return True
                    
            point += 1
            update = {'$set':
                      {
                          f'data.{module}.{type}.{str(chat_id)}': point
                      }}
            db.update_one(user, update)
            return True
        else:
             return False


