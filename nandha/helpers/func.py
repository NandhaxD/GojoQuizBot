import random

from datetime import datetime


async def taken_time(start_time: str, end_time: str):
     time_format = "%M:%S"
     time1 = datetime.strptime(start_time, time_format)
     time2 = datetime.strptime(end_time, time_format)
     # Calculate the difference
     time_diff = time2 - time1
     return time_diff



async def get_question():     
     symbol = ['+','-','*']
     question = "({num1}{syb1}{num2}){syb2}{num3}".format(num1=random.randint(20, 44), syb1=random.choice(symbol), num2=random.randint(2, 9), syb2=random.choice(symbol), num3=random.randint (1, 30))     
     answer = eval(question)
     return {'question': question, 'answer': answer}


