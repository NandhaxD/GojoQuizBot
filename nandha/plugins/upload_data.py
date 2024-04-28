
import config

from nandha import bot, DATABASE
from nandha.helpers.decorator import devs_only
from datetime import datetime, timedelta

from pyrogram import filters, enums, types


def format_data(text):
   type = text.split('#type')[1].split('#q')[0]
   question = text.split('#q')[1].split("#1")[0]
   option1 = text.split('#1')[1].split('#2')[0]
   option2 = text.split('#2')[1].split('#3')[0]
   option3 = text.split('#3')[1].split('#4')[0]
   option4 = text.split('#4')[1].split('#e')[0]
   explain = text.split('#e')[1].split('#a')[0]
   
   answer = text.split()[-1]
   return type, question, option1, option2, option3, option4, explain, answer


data = {}

@bot.on_message(filters.command('upload', prefixes=config.PREFIXES))
async def upload_data(_, message):
    chat_id = message.chat.id 
    mention = message.from_user.mention
    user_id = message.from_user.id

    
    # /upload -q {question} -1 {option1} -2 {option2} -3 {option3} -4 {option4} -a {answer}
    try:
        text = format_data(message.text)
    except IndexError:
        return await message.reply(
            "Invalid message format. Please use the format `#q question #1 option1 #2 option2 #3 option3 #4 option4 #e text #a num`"
        )
    button = [[
       types.InlineKeyboardButton(
          text='Save ✅', callback_data=f'save:{user_id}')
    ]]
    msg = await bot.send_message(chat_id=config.GROUP_ID,
        text=f'''\n
**Type**: {text[0]}   

**Question**: `{text[1]}`
**Option1**: `{text[2]}`
**Option2**: `{text[3]}`
**Option3**: `{text[4]}`
**Option4**: `{text[5]}`
**Explain**: `{text[6]}`
**Answer**: `{text[7]}`

**Question Uploaded by {mention}**
        ''', reply_markup=types.InlineKeyboardMarkup(button))
    await message.reply(
       f'**Thank you for participating, here you can see your post: {msg.link}**'
    )
    close_t = datetime.now() + timedelta(seconds=60)
    explain = text[6]
    question = text[1]
    option1 = text[2]
    option2 = text[3]
    option3 = text[4]
    option4 = text[5]
    answer = int(text[7])
    if bool(await bot.send_poll(
        chat_id=config.GROUP_ID,
        question=question,
        options=[option1, option2, option3, option4],
        explanation=explain,
        correct_option_id=answer,
        close_date=close_t,
        type=enums.PollType.QUIZ,
        is_anonymous=False
    )):
       if user_id in data:
          data[user_id].append(text)
       else:
          data[user_id] = [text]
    return await message.reply(data)
