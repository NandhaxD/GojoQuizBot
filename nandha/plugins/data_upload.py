
from nandha import bot, DATABASE
from nandha.database.decorator import devs_only

from pyrogram import filters


def text_json(text):
   question = text.split('#q')[1].split("#1")[0]
   option1 = text.split('#1')[1].split('#2')[0]
   option2 = text.split('#2')[1].split('#3')[0]
   option3 = text.split('#3')[1].split('#4')[0]
   option4 = text.split('#4')[1].split('#a')[0]
   answer = text.split()[-1]
   return question, option1, option2, option3, option4, answer



@bot.on_message(filters.command('upload'))
@devs_only
async def data_upload(_, message):
  # /upload -q {question} -1 {option1} -2 {option2} -3 {option3} -4 {option4} -a {answer}
      try:
          text = text_json(message.text)
       except IndexError:
          return await message.reply(
                "Invalid message format. Please use the format '#q question #1 option1 -
                #2 option2 #3 option3 #4 option4 a answer'"
          )
      await message.reply(text)




             
