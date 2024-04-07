import random


async def get_question():     
     symbol = ['+','-','*']
     question = "({num1}{syb1}{num2}){syb2}{num3}".format(num1=randint(20, 44), syb1=choice(symbol), num2=randint(2, 9), syb2=choice(symbol), num3=randint (1, 30))     
     answer = eval(query)
     return {'question': question, 'answer': answer}


