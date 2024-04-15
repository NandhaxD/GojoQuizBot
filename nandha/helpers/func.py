
import config
import requests 
import random
import sys
import os
import io

from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

from nandha import DATABASE 
from nandha.database.users import get_users
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup




anime_gif_key = [
       "lurk", "shoot", "sleep", "shrug", "stare", "wave", "poke", "smile", "peck",
       "wink", "blush", "smug", "tickle", "yeet", "think", "highfive", "feed",
       "bite", "bored", "nom", "yawn", "facepalm", "cuddle", "kick", "happy",
       "hug", "baka", "pat", "nod", "nope", "kiss", "dance", "punch", "handshake",
       "slap", "cry", "pout", "handhold", "thumbsup", "laugh"]

async def get_anime_gif(key):
    data = requests.get(f"https://nekos.best/api/v2/{key}").json()
    img = data['results'][0]["url"]
    return img



async def get_rmath_lb(chat_id: str):
       db = DATABASE['USERS']
       user_points = {}
       for user_data in db.find():
            user_id = user_data['user_id']
            data = user_data['data']
            if 'riddle' in data and 'math' in data['riddle'] and str(chat_id) in data['riddle']['math']:
                  points = data['riddle']['math'][str(chat_id)]
                  user_points[user_id] = points
       sorted_user_points = sorted(user_points.items(), key=lambda x: x[1], reverse=True)
       return sorted_user_points



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



async def make_math_riddle(chat_id: int):
     img = Image.open(io.BytesIO(requests.get(random.choice(config.RIDDLE_MATH_BG)).content))
     draw = ImageDraw.Draw(img)
     url = "https://github.com/JulietaUla/Montserrat/raw/master/fonts/otf/Montserrat-ExtraBold.otf"
     k = requests.get(url)
     open(url.split("/")[-1], "wb").write(k.content)
     font = ImageFont.truetype(url.split("/")[-1], size=100)
     math = await get_question()
     question = math['question'] + " = ?"
     answer = math['answer']
     tbox = font.getbbox(question)
     w = tbox[2] - tbox[0]
     h = tbox[3] - tbox[1]
     # Set the center of the image as the position for the text
     width, height = img.size
     position = (width // 2, height // 2)
     color = (255, 255, 255)
     draw.text(((width-w)//2, (height-h)//2), question, font=font, fill=color)
     img = img.resize((int(width*1.5), int(height*1.5)), Image.LANCZOS)
     path = f"{chat_id}rm.jpg"
     img.save(path)    
     return path, answer, question 




