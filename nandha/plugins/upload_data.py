
from nandha import bot, DATABASE
from nandha.helpers.decorator import devs_only
from datetime import datetime, timedelta

from pyrogram import filters, enums


def text_json(text):
   question = text.split('#q')[1].split("#1")[0]
   option1 = text.split('#1')[1].split('#2')[0]
   option2 = text.split('#2')[1].split('#3')[0]
   option3 = text.split('#3')[1].split('#4')[0]
   option4 = text.split('#4')[1].split('#e')[0]
   explain = text.split('#e')[1].split('#a')[0]
   
   answer = text.split()[-1]
   return question, option1, option2, option3, option4, explain, answer



@bot.on_message(filters.command('upload'))
@devs_only
async def data_upload(_, message):
    chat_id = message.chat.id 
    # /upload -q {question} -1 {option1} -2 {option2} -3 {option3} -4 {option4} -a {answer}
    try:
        text = text_json(message.text)
    except IndexError:
        return await message.reply(
            "Invalid message format. Please use the format `#q question #1 option1 #2 option2 #3 option3 #4 option4 #e text #a num`"
        )
    button = [[
       InlineKeyboardButton(
          text='Save ✅', callback_data=f'save:{config.OWNER_ID}:{text}')
    ]]
    await message.reply(
        f'''\n
**Question**: {text[0]}
**Option1**: {text[1]}
**Option2**: {text[2]}
**Option3**: {text[3]}
**Option4**: {text[4]}
**Explain**: {text[5]}
**Answer**: {text[6]}
        ''', reply_markup=pyrogram.types.InlineKeyboardMarkup(button))
    close_t = datetime.now() + timedelta(seconds=60)
    explain = text[5]
    question = text[0]
    option1 = text[1]
    option2 = text[2]
    option3 = text[3]
    option4 = text[4]
    answer = int(text[6])
    await bot.send_poll(
        chat_id=chat_id,
        question=question,
        options=[option1, option2, option3, option4],
        explanation=explain,
        correct_option_id=answer,
        close_date=close_t,
        type=enums.PollType.QUIZ,
        is_anonymous=False
    )
