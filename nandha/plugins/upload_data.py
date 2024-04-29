import config

from nandha import *
from nandha.helpers.decorator import *
from datetime import *

from pyrogram import filters
from pyrogram.types import *

db = DATABASE['REQUESTS']

app = bot
types = [{"text": "General", "info": "just genral quiz"}, {"text": "rare", "info": "uff rarest quiz"}]

@app.on_message(filters.command('request', prefixes=config.PREFIXES))
async def request(_, message):
    m = message
    if m.chat.type != enums.ChatType.PRIVATE:
        return await m.reply_text("`Request Your Own Quiz On Dm`")
    else:
        if not (await db.find_one({"user_id": m.from_user.id})):
            buttons = []
            text = "**Choose Your Quiz Type: **\n\n"
            for x in types:
                buttons.append([InlineKeyboardButton(x["text"], callback_data=f"request:{x['text']}")])
                buttons.append([InlineKeyboardButton("Cancel 🚫", callback_data=f"delete:{m.from_user.id}")])            
                text += f"• `{x['text']}` - `{x['info']}`\n"
            await m.reply_text(text, reply_markup=Inlinekeyboardmarkup(buttons))
        else:
            return await message.reply_text("`Already Creating Quiz Process Going On`")

@app.on_callback_query(filters.regex("delete"))
async def delete(_, cq):
    user_id = int(cq.data.split("_")[1])
    if cq.from_user.id != user_id:
        return await cq.answer("This Wasn't Requested By You")
    else:
        if (await db.find_one({"user_id": cq.from_user.id})):
            await db.delete_one({"user_id": cq.from_user.id})
        await cq.message.delete()

@app.on_callback_query(filters.regex("request"))
async def request(_, cq):
    type = str(cq.data.split(":")[1])
    await cq.edit_text(f"**Alright You Choosed Quiz Type As** `{type}`\n\n`Wants To Cancel This Progress At Any Moment Send /cancel`")
    num = 0
    question = []
    options = []
    answer = []
    explain = []
    close_t = datetime.now() + timedelta(seconds=60)
    q = await cq.message.chat.ask(f"**Now Send Me Your Question For The Quiz**", filters=filters.text)
    if (q.text).split()[0] == "/cancel":
        await q.sent_message.edit_text("`Process Cancelled ✅`")
        exit()
    question.append(q.text)
    await q.sent_message.delete()
    while num < 4:
        num += 1
        op = await cq.message.chat.ask(f"**Now Send Me Your Option {num} For The Quiz**\n\n`There Should 4 Options`", filters=filters.text)
        if (op.text).split()[0] == "/cancel":
            await op.sent_message.edit_text("`Process Cancelled ✅`")
            exit()
        options.append(op.text)
        await op.sent_message.delete()

    ans = await cq.message.chat.ask(f"**Now Tell Me Which Option Is The Corect One**\n\n`Note:- Send Your Option As Digit Like If Option 1 is correct send 1`", filters=filters.text)
    if (ans.text).split()[0] == "/cancel":
        await ans.sent_message.edit_text("`Process Cancelled ✅`")
        exit()
    while not ans.text.isdigit() or int(ans.text) > 4 or int(ans.text) == 0and not (ans.text).split()[0] == "/cancel": # if ans text == /cancel the process should be cancelled 
        ans = await cq.message.chat.ask(f"**Now Tell Me Which Option Is The Corect One**\n\n`Note:- Send Your Option As Digit Like If Option 1 is correct send 1`", filters=filters.text)
    answer.append(int(ans.text))

    ex = await cq.message.chat.ask(f"**Now Give Me A Explanation For The Quiz**", filters=filters.text)
    if (ex.text).split()[0] == "/cancel":
        await ex.sent_message.edit_text("`Process Cancelled ✅`")
        exit()
    explain.append(ex.text)
    await ex.sent_message.delete()

    # Save quiz data in the database
    quiz_data = {
        "user_id": cq.from_user.id,
        "question": question[0],
        "type": type,
        "options": options,
        "explanation": explain[0],
        "answer": answer[0]
    }
    db.insert_one(quiz_data)

    text = f"**Question**: `{question[0]}`**:-**\n\n"
    text += f"**• Type:** `{type}`\n"
    ops = 1
    for x in options:
        text += f"**• Option {ops}**: `{x}`"
        ops += 1
    text += f"\n**• Answer:** `{options[answer[0] - 1]}`"
    text += f"\n**• Explanation:** `{explain[0]}`"
    keyboard = [[
        InlineKeyboardButton("Confirm ✅", callback_data=f"review:{cq.from_user.id}"),
        InlineKeyboardButton("Cancel 🚫", callback_data=f"delete:{cq.from_user.id}")
    ]]

    await bot.send_poll(
        chat_id=cq.from_user.id,
        question=question[0],
        options=options,
        explanation=explain[0],
        correct_option_id=answer[0],
        close_date=close_t,
        type=enums.PollType.QUIZ,
        is_anonymous=False
    )
    await bot.send_message(cq.from_user.id, text, reply_markup=Inlinekeyboardmarkup(keyboard))

@app.on_callback_query(filters.regex("review"))
async def review(_, cq):
    user_id = int(cq.data.split("_")[1])
    if cq.from_user.id != user_id:
        return await cq.answer("This Wasn't Requested By You")
    else:
        if not (await db.find_one({"user_id": cq.from_user.id})):
            return await cq.answer("Something Happened Sorry")
        else:
            uwu = await db.find_one({"user_id": cq.from_user.id})
            explain = uwu["explanation"]
            type = uwu["type"]
            question = uwu["question"]
            option1 = uwu["options"][0]
            option2 = uwu["options"][1]
            option3 = uwu["options"][2]
            option4 = uwu["options"][3]
            answer = int(uwu["answer"])
            keyboard = [[
                InlineKeyboardButton("Edit 📝", callback_data=f"edit"),
                InlineKeyboardButton("Accept ✅", callback_data=f"accept"),
                InlineKeyboardButton("Decline 🚫", callback_data=f"delete")
            ]]
            msg = await bot.send_message(chat_id=config.GROUP_ID,
                text=f"""\n
        **Type:** `{type}`

        **Question:** `{question}`
        **Option1:** `{option1}`
        **Option2:** `{option2}`
        **Option3:** `{option3}`
        **Option4:** `{option4}`
        **Explain:** `{explain}`
        **Answer:** `{answer}`

        **Question Requested By** `{user_id}`
        """, reply_markup=InlineKeyboardMarkup(keyboard))
            await bot.send_poll(
                chat_id=config.GROUP_ID,
                question=question,
                options=uwu["options"],
                explanation=explain,
                correct_option_id=answer,
                close_date=close_t,
                type=enums.PollType.QUIZ,
                is_anonymous=False
            ))
            await cq.message.reply_text(
       f'**Thank You For Participating, Here You Can See Your Post: {msg.link}**'
            )
            await cq.delete()
