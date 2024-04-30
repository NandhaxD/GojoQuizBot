
import os
import io
import sys
import time
import config
import traceback
import subprocess 

from pyrogram import filters, enums
from nandha.helpers.func import restart
from nandha.helpers.decorator import devs_only
from nandha.database.chats import get_chats
from nandha.database.users import get_users

from nandha import bot




def p(*args, **kwargs):
    print(*args, **kwargs)

async def aexec(code, bot, m, r):
    exec(
        "async def __aexec(bot, m, r): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](bot, m, r)
  

 
@bot.on_message(filters.command('statics', prefixes=config.PREFIXES))
async def statics(_, message):
      if message.from_user.id != config.OWNER_ID:
            return await message.reply('Only owner can use this command.', quote=True)
      users = len(await get_users())
      chats = len(await get_chats())
      return await message.reply(
         f'<b>Users</b>: <code>{users}</code>\n'
         f'<b>Chats</b>: <code>{chats}</code>\n\n'
         '<b>By @NANDHABOTS**</b>'
      )
	
@bot.on_message(filters.command('restart', prefixes=config.PREFIXES))
@devs_only
async def retart_script(_, message):
	 await message.reply(
		 "`Restarting Script...`"
	 )
	 await restart()


@bot.on_message(filters.command('bcast', prefixes=config.PREFIXES))
@devs_only
async def broadcast(_, message):
    reply = message.reply_to_message
    from_chat_id = message.chat.id

    if not reply:
        return await message.reply(
            '`Reply to the message for execute broadcast in all my chats.`'
        )
    else:
        done = 0
        message_id = reply.message_id
        chats_id = (await get_chats()) + (await get_users())
        msg = await message.reply(
            '`Broadcasting...`'
        )
        for chat_id in chats_id:
            try:
                await bot.forward_messages(chat_id, from_chat_id, message_ids=message_id)
                done += 1
                if done % 5 == 0:
                    await msg.edit_text(f'**Successfully forwarded to {done} chats loop processing. ❤️**.')
                    await asyncio.sleep(5)
            except Exception as e:
                pass
                #print(f"Failed to forward message to {chat_id}: {e}")
        undone = len(chats_id) - done
        await msg.delete()
        return await message.reply(
            f'**Successfully completed!**.\n**Success forwards**: `{done}`.\n**Failed forwards**: `{undone}`'
	)

	   
	    
							   
@bot.on_message(filters.command('sh', prefixes=config.PREFIXES))
@devs_only
async def shell(_, message):
    if len(message.text.split()) > 1:
        code = message.text.split(None, 1)[1]
        shell = subprocess.getoutput(code)
        return await message.reply(
            f"<pre language='python'>\nSHELL output:\n{shell}</pre>", 
            quote=True,
            parse_mode=enums.ParseMode.HTML
	)

@bot.on_message(filters.command("e",prefixes=config.PREFIXES))
@devs_only
async def evaluate(bot , message):
    global r, m
    status_message = await message.reply_text("`Running ...`")
    try:
        cmd = message.text.split(maxsplit=1)[1]
    except IndexError:
        await status_message.delete()
        return
    start_time = time.time()

    r = message.reply_to_message	
    m = message

    if r:
        reply_to_id = r.id
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, bot, m, r)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    taken_time = round((time.time() - start_time), 3)
    output = evaluation.strip()
	
    final_output = "<pre>Command:</pre><pre language='python'>{}</pre> \n<pre>Takem Time To Output: {}'s:</pre><pre language='python'>{}</pre>".format(cmd, taken_time, output)
	
    if len(final_output) > 4096:
        filename = "output.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(final_output))
        await message.reply_document(
            document=filename,
            thumb=THUMB_ID,
            caption=cmd,
            quote=True,
            
        )
        os.remove(filename)
        await status_message.delete()
        return
    else:
        await status_message.edit(final_output, parse_mode=enums.ParseMode.HTML)
        return 
