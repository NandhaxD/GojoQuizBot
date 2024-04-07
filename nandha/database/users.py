from nandha import DATABASE

db = DATABASE['USERS']


async def get_users() -> list:
    users_id = [ user['user_id'] for user in db.find()]
    return users_id

async def add_user(user_id: int):
    json = {'user_id': user_id}
    users_id = await get_users()
    if user_id in users_id:
           return
    else:
        db.insert_one(json)
        return True

async def remove_user(user_id: int):
      json = {'user_id': user_id}
      users_id = await get_users()
      if user_id in users_id:
          db.delete_one(json)
          return True
      return 
