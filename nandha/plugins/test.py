import requests

from bs4 import BeautifulSoup

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto

from nandha import bot

profile_stats = """
**🌀 Name:** `{}`

**✨ Ninjutsu:** `{}`
**🥊 Taijutsu:** `{}`
**👁️‍🗨️ Genjutsu:** `{}`
**🧠 Intelligence:** `{}`
**💪 Strength:** `{}`
**⚡ Speed:** `{}`
**🏃‍♂️ Stamina:** `{}`
**✌️ Hand Seals:** `{}`

**🥷 Total:** `{}`
"""

async def get_db():
    url = "https://naruto.fandom.com/wiki/Category:Character_stats"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    names = []
    for link in soup.find_all('a', href=True):
        if link['href'].startswith("/wiki/Infobox:"):
            name = link.text.strip()
            names.append(name.replace("Infobox:", "").replace(" Stats", ""))
        return names

async def fetch_naruto_profile(char_name):
    url = f"https://naruto.fandom.com/wiki/Infobox:{char_name.replace('ō', '%C5%8D').replace('ū', '%C5%AB').replace(' ', '_')}_Stats"
    response = requests.get(url)

    if response.status_code!= 200:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    stats = {}
    table = soup.find("table")

    if not table:
        return None

    headers = [th.text.strip() for th in table.find_all("th")]
    data_rows = table.find_all("tr")[1:]

    for row in data_rows:
        data = [td.text.strip() for td in row.find_all(["th", "td"])]

        if len(headers)!= len(data):
            return None

        stats_dict = {}
        for i, header in enumerate(headers):
            stats_dict[header] = data[i]

        stats.update(stats_dict)

    images = []
    img_link = f"https://naruto.fandom.com/wiki/{char_name.replace('ō', '%C5%8D').replace('ū', '%C5%AB').replace(' ', '_')}"
    response = requests.get(img_link)
    soup = BeautifulSoup(response.content, 'html.parser')
    images = soup.find_all('img', class_='thumbborder')

    image_list = []
    for img in images:
        image_list.append(InputMediaPhoto(img['src'], caption=img['alt']))

    return stats, image_list

@bot.on_message(filters.command("naruto"))
async def naruto(_, m: Message):
    db = await get_db()
    char_name = m.text.split()[1]
    for num in range(len(db)):
        if char_name.lower() == db[num].split()[0].lower() or char_name.lower() == db[num].lower():
            char_name = db[num]
    similar_names = []
    for num in range(len(db)):
        if char_name.lower() in db[num].lower():
            similar_names.append(db[num])
    if similar_names:
        if len(similar_names) == 1:
            await m.reply_text(f"**Did You Mean** `{similar_names[0]}` **?**")
        else:
            await m.reply_text(f"**Did You Mean One Of These:** `{', '.join(similar_names)}` **?**")
    else:
        await m.reply_text(f"`{char_name}` **Not Found In The Database.**")

    stats, image_list = await fetch_naruto_profile(char_name)

    if stats:
        await bot.send_media_group(m.chat.id, media=image_list, reply_to_message_id=m.id)
        await m.reply_text(profile_stats.format(char_name, stats.get("Ninjutsu"), stats.get("Taijutsu"), stats.get("Genjutsu"), stats.get("Intelligence"), stats.get("Strength"), stats.get("Speed"), stats.get("Stamina"), stats.get("Hand seals"), stats.get("Total")))
    else:
        await m.reply_text("`Error Occured`")
