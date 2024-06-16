
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







async def change_text(text):
       return "Enabled" if text == True else "Disabled" if text == False else text
                
async def restart():
    cmd = sys.argv #List of command-line arguments passed to the script.
    executable = sys.executable #Path to the current Python interpreter executable.
    os.execvp(executable, [ executable, *cmd ]) # Executes the program using the given path and arguments.
    return True



async def time_diffrence(start_time: str, end_time: str):
    time_format = "%H:%M:%S"
    time1 = datetime.strptime(start_time, time_format)
    time2 = datetime.strptime(end_time, time_format)
    time_diff_seconds = (time2 - time1).total_seconds()
    return time_diff_seconds
  

async def taken_time(start_time: str, end_time: str):
    time_diff_seconds = await time_diffrence(start_time, end_time)
    time_diff_seconds = round(time_diff_seconds, 3)
    if time_diff_seconds > 60:
          time_diff_minutes = time_diff_seconds / 60
          time_diff_minutes = round(time_diff_minutes, 3)
          return f"{time_diff_minutes:.2f} Min"
          # Convert seconds to minutes
    else:
          return f"{time_diff_seconds:.2f} Sec"




def change_font(text: str):
        style = {
            "a": "𝐚",
            "b": "𝐛",
            "c": "𝐜",
            "d": "𝐝",
            "e": "𝐞",
            "f": "𝐟",
            "g": "𝐠",
            "h": "𝐡",
            "i": "𝐢",
            "j": "𝐣",
            "k": "𝐤",
            "l": "𝐥",
            "m": "𝐦",
            "n": "𝐧",
            "o": "𝐨",
            "p": "𝐩",
            "q": "𝐪",
            "r": "𝐫",
            "s": "𝐬",
            "t": "𝐭",
            "u": "𝐮",
            "v": "𝐯",
            "w": "𝐰",
            "x": "𝐱",
            "y": "𝐲",
            "z": "𝐳",
            "A": "𝐀",
            "B": "𝐁",
            "C": "𝐂",
            "D": "𝐃",
            "E": "𝐄",
            "F": "𝐅",
            "G": "𝐆",
            "H": "𝐇",
            "I": "𝐈",
            "J": "𝐉",
            "K": "𝐊",
            "L": "𝐋",
            "M": "𝐌",
            "N": "𝐍",
            "O": "𝐎",
            "P": "𝐏",
            "Q": "𝐐",
            "R": "𝐑",
            "S": "𝐒",
            "T": "𝐓",
            "U": "𝐔",
            "V": "𝐕",
            "W": "𝐖",
            "X": "𝐗",
            "Y": "𝐘",
            "Z": "𝐙",
            "0": "𝟎",
            "1": "𝟏",
            "2": "𝟐",
            "3": "𝟑",
            "4": "𝟒",
            "5": "𝟓",
            "6": "𝟔",
            "7": "𝟕",
            "8": "𝟖",
            "9": "𝟗",
        }
        for i, j in style.items():
            text = text.replace(i, j)
        return text


################################################################################################################


#Riddle #math #function

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


################################################################################################################


#riddle #words #function


def get_random_word():
   with open("./resources/words_alpha.txt", "r") as f:
       words = [line.strip() for line in f.readlines()]
   random_word = random.choice(words)
   return random_word

async def make_words_riddle(chat_id: int):
       image_url = random.choice(config.RIDDLE_WORDS_BG)
       img = Image.open(io.BytesIO(requests.get(image_url).content))
       draw = ImageDraw.Draw(img)
       url = "https://github.com/JulietaUla/Montserrat/raw/master/fonts/otf/Montserrat-ExtraBold.otf"
       k = requests.get(url)
       open(url.split("/")[-1], "wb").write(k.content)
       font = ImageFont.truetype(url.split("/")[-1], size=38)
       text = get_random_word().capitalize()
       tbox = font.getbbox(text)
       w = tbox[2] - tbox[0]
       h = tbox[3] - tbox[1]
       width, height = img.size
       position = (width // 2, height // 2)
       color = (0, 0, 0)  # Change to black
       draw.text(((width-w)//2 + 180, (height-h)//2 + 40), config.NAME, font=font) # made by @nandha
       draw.text(((width-w)//2 - 120, (height-h)//2 + 15), text, font=font, fill=color)
       img = img.resize((int(width*1.5), int(height*1.5)), Image.LANCZOS)
       path = f"{chat_id}rw.jpg"
       img.save(path)
       return path, text
       

       
       

