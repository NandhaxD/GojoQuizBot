import random


async def get_question():     
     symbol = ['+','-','*']
     question = "({num1}{syb1}{num2}){syb2}{num3}".format(num1=random.randint(20, 44), syb1=random.choice(symbol), num2=random.randint(2, 9), syb2=random.choice(symbol), num3=random.randint (1, 30))     
     answer = eval(query)
     return {'question': question, 'answer': answer}


