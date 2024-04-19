
from collections import defaultdict
from nandha import DATABASE

async def get_rmath_gtop():
     db = DATABASE['USERS']
     all_users = db.find({})
     leaderboard = defaultdict(int)
     for user in all_users:
         if 'data' in user and 'riddle' in user['data'] and 'math' in user['data']['riddle']:
              for chat_id, points in user['data']['riddle']['math'].items():
                 name = user['data']['first_name'] if user['data'] and user['data']['first_name'] else None
                 leaderboard[user['user_id']] += points
                 pre_points = leaderboard[user['user_id']]
                 leaderboard[user['user_id']] = {'first_name': name, 'points': pre_points}             
     # Sort the leaderboard by points
     sorted_leaderboard = dict(sorted(leaderboard.items(), key=lambda x: x['points'], reverse=True))
     return sorted_leaderboard
  
async def get_rmath_top(chat_id: str):
       db = DATABASE['USERS']
       user_points = {}
       for user_data in db.find():
            user_id = user_data['user_id']
            data = user_data['data']
            if 'riddle' in data and 'math' in data['riddle'] and str(chat_id) in data['riddle']['math']:
                  points = data['riddle']['math'][str(chat_id)]
                  name = data['first_name'] if data and data['first_name'] else None
                  user_points[user_id] = {'first_name': name, 'points': points}
                  
       sorted_user_points = sorted(user_points.items(), key=lambda x: x['points'], reverse=True)
       return sorted_user_points
