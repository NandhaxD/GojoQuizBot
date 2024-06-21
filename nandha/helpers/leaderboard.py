
from collections import defaultdict
from nandha import DATABASE



####################################################################################################

#riddle 

async def get_leaderboard_global(mode: str, type: str):
     db = DATABASE['USERS']
     all_users = db.find({})
     leaderboard = defaultdict(int)
     for user in all_users:
         if 'data' in user and mode in user['data'] and type in user['data'][mode]:
              for chat_id, points in user['data'][mode][type].items():
                   try:
                      name = user['data']['first_name']
                      leaderboard[name] += points
                   except KeyError:
                        leaderboard[user['user_id']] += points 
                        
                        
               

     # Sort the leaderboard by points
     sorted_leaderboard = dict(sorted(leaderboard.items(), key=lambda x: x[1], reverse=True))
     return sorted_leaderboard
  

async def get_leaderboard_group(chat_id: str, mode: str, type: str):
       db = DATABASE['USERS']
       user_points = {}
       for user_data in db.find():
            user_id = user_data['user_id']
            data = user_data['data']
            if mode in data and type in data[mode] and str(chat_id) in data[mode][type]:
                  points = data[mode][type][str(chat_id)]
                  try:
                     name = data['first_name']
                     user_points[name] = points
                  except KeyError:
                       user_points[user_id] = points
                  
                 
       sorted_user_points = sorted(user_points.items(), key=lambda x: x[1], reverse=True)
       return sorted_user_points


####################################################################################################

