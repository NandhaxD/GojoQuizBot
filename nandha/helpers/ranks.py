
from collections import defaultdict
from nandha import DATABASE

async def get_user_rank(user_id: int, mode: str, type: str):
    db = DATABASE['USERS']
    all_users = db.find({})
    leaderboard = defaultdict(int)
    
    # Create the leaderboard
    for user in all_users:
        if 'data' in user and mode in user['data'] and type in user['data'][mode]:
            for chat_id, points in user['data'][mode][type].items():
                
                leaderboard[user['user_id']] += points

    # Sort the leaderboard by points
    sorted_leaderboard = dict(sorted(leaderboard.items(), key=lambda x: x[1], reverse=True))
    
    # Get the rank of the specific user
    rank = 1
    for user, points in sorted_leaderboard.items():
        if int(user) == user_id:
            return rank, points
        rank += 1
    
    # If the user is not found in the leaderboard
    return 0, 0

# Example usage:
# user_rank = await get_user_rank(12345, 'math')
# print(f"User rank: {user_rank}")


