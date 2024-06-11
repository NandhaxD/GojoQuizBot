from nandha.database.users import add_user
from nandha import DATABASE

db = DATABASE['USERS']



async def get_user_points(user_id: str, module: str, type: str):
    points = 0
    user = db.find_one({'user_id': user_id})
    data = user.get('data', {}).get(module, {}).get(type, {})
    if not data:
        return points
    else:
       for point in data.values():
            points += point
       return points
    
    

      


####################################################################################################

async def get_user_chat_points(chat_id: int, user_id: int, module: str, type: str):
        filter = {'user_id': user_id}
        user = db.find_one(filter)
        if user:
            point = user.get('data', {}).get(module, {}).get(type, {}).get(str(chat_id), 0)
            return int(point)
        else:
            return False
    
async def edit_user_chat_points(chat_id: int, user_id: int, module: str, type: str, point: int):
        filter = {'user_id': user_id}
        user = db.find_one(filter)
        if user:
            update = {'$set':
                      {
                          f'data.{module}.{type}.{str(chat_id)}': point
                      }}
            db.update_one(user, update, upsert=True)
            return True
        else:
            return False

async def add_user_chat_points(chat_id: int, user_id: int, module: str, type: str):
        filter = {'user_id': user_id}
        user = db.find_one(filter)
        if user:
            try:
               point = await get_user_chat_points(chat_id, user_id, module, type)
            except:
                update = {'$set':
                      {
                          f'data.{module}.{type}.{str(chat_id)}': 1
                      }}
                db.update_one(user, update, upsert=True)
                return True
                    
            point += 1
            update = {'$set':
                      {
                          f'data.{module}.{type}.{str(chat_id)}': point
                      }}
            db.update_one(user, update, upsert=True)
            return True
        else:
             return False

####################################################################################################
