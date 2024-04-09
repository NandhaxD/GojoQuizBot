import random

from datetime import datetime


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
     question = "({num1}{syb1}{num2}){syb2}{num3}".format(num1=random.randint(20, 44), syb1=random.choice(symbol), num2=random.randint(2, 9), syb2=random.choice(symbol), num3=random.randint (1, 30))     
     answer = eval(question)
     return {'question': question, 'answer': answer}


