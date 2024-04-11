
import config
import random
import sys
import os

from datetime import datetime
from nandha import DATABASE 
from nandha.database.users import get_users
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup



async def get_rmath_lb(chat_id: str):
       db = DATABASE['USERS']
       user_riddle_points = {}
       for user_data in db.find():
            user_id = user_data['user_id']
            riddle_points = user_data['data']['riddle']['math'][str(chat_id)]
            user_riddle_points[user_id] = riddle_points
           
       sorted_user_riddle_points = sorted(user_riddle_points.items(), key=lambda x: x[1], reverse=True)
       return sorted_user_riddle_points

    



async def ask_start_pm(user_id: int, message):
    users = await get_users()    
    if not user_id in users:
         button = [[InlineKeyboardButton('Start PM', user_id=config.BOT_ID)]]
         await message.reply(
             'Start bot in private and then try solving puzzles chat.',
             reply_markup=InlineKeyboardMarkup(button))
         return False
    else:
         return True
           
     
    
    
async def restart():
    cmd = sys.argv #List of command-line arguments passed to the script.
    executable = sys.executable #Path to the current Python interpreter executable.
    os.execvp(executable, [ executable, *cmd ]) # Executes the program using the given path and arguments.
    return True
    
async def taken_time(start_time: str, end_time: str):
    time_format = "%H:%M:%S"
    time1 = datetime.strptime(start_time, time_format)
    time2 = datetime.strptime(end_time, time_format)
    # Calculate the difference in seconds
    time_diff_seconds = (time2 - time1).total_seconds()
    time_diff_seconds = round(time_diff_seconds, 3)
    if time_diff_seconds > 60:
            time_diff_minutes = time_diff_seconds / 60
            time_diff_minutes = round(time_diff_minutes, 3)
            return f"{time_diff_minutes}Min"
    # Convert seconds to minutes
    else:
         return f"{time_diff_seconds}Sec"



async def get_question():  
    
     symbol = ['+','-','*']
     num1=random.randint(20, 44)
     syb1=random.choice(symbol)
     num2=random.randint(2, 9)
     syb2=random.choice(symbol)
     num3=random.randint (1, 30)
    
     question = "({num1}{syb1}{num2}){syb2}{num3}".format(
         num1=num1, 
         syb1=syb1,
         num2=num2,
         syb2=syb2, 
         num3=num3
     )     
     ans = eval(question)
     
     if ans <= 0:
              answer = ans*-1
              question = "(({num1}{syb1}{num2}){syb2}{num3})(-1)".format(
              num1=num1, 
              syb1=syb1,
              num2=num2,
              syb2=syb2, 
              num3=num3
     )    
     else:
         question = question 
         answer = ans
         
     return {'question': question, 'answer': answer}


