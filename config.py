import os


####################################################################################################


# required variable's

OWNER_ID = int(os.getenv('OWNER_ID', 5696053228))
BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
API_ID = int(os.getenv('API_ID'))
DB_URL = str(os.getenv('DB_URL'))
API_HASH = str(os.getenv('API_HASH'))


####################################################################################################

# infos

NAME = 'GojoQuizBot'
SUPPORT = 'NandhaSupport'
CHANNEL = 'Nandhabots'
GROUP_ID =  -1002039454048
LOGS_CHANNEL = 'GojoQuizLogs'
BOT_ID = int(BOT_TOKEN.split(':')[0])
DEVS_ID = [5696053228, 5456798232]

####################################################################################################


# tools

START_IMAGE = 'https://graph.org/file/15a7cc4a22cad1f6189f0.jpg'
PREFIXES = ['/', '\\']
EMOJI = ['❤️', '⚡️', '😈', '👍', '🔥']

####################################################################################################


# Images #bgs #game #riddle #quiz

RIDDLE_MATH_BG = [
     "https://graph.org/file/9b165baf9de57406d76ca.jpg",
     "https://graph.org/file/bd790b253ac3befdcff51.jpg",
     "https://graph.org/file/8ce59f8e42399029e9051.jpg",
     "https://graph.org/file/010811dae00123d74ad41.jpg"
]


RIDDLE_WORDS_BG = [
"https://graph.org/file/b4089de39d879004cc683.jpg",
"https://graph.org/file/5a971d88327c65606a930.jpg",
"https://graph.org/file/87ebdf345c715c5af7d98.jpg",
]


RIDDLE_ANSWER_GIF = 'https://graph.org/file/37cd114c92e1d74c9cc07.mp4'

####################################################################################################


#String #game #riddle #quiz


S_STICKERS = [
 "CAACAgUAAxkBAALnzmZojaKJX4bDz51wnwOHGa3ZbO0EAAI8EAACn2JIV-lJWjkdlCApHgQ",
 "CAACAgUAAxkBAALn02ZojpVCCYkJGQOCUjd7RUPi6EyqAAJpDwACim6xVg7ShW4Xm3hkHgQ",
 "CAACAgUAAxkBAALn1mZojs4nrmgkGXmwYgj-wWkGEMfIAAJEFQACqvWoVoI0H5FDdmu8HgQ",
 "CAACAgUAAxkBAALn4mZokTKQDIEIWe7wrony-YKTldqWAALZDAACpMtIV216Zo3l6fqYHgQ"
]
     

STATS_IMG = "https://graph.org/file/83c7b808673099eda0dc6.jpg"

STATS_STRING = (
     "**{name}'s 𝗦𝘁𝗮𝘁𝘀 in {chat_name}**:\n\n"
     "➤ 𝐑𝐢𝐝𝐝𝐥𝐞:\n"
     "  ✪ 𝐒𝐨𝐥𝐯𝐞𝐝 𝐌𝐚𝐭𝐡𝐬 ➩〘 `{rmath_points}` 〙\n"
     "  ✪ 𝐒𝐨𝐥𝐯𝐞𝐝 𝐖𝐨𝐫𝐝𝐬 ➩〘 `{rwords_points}` 〙\n"
     "\n\n```\n➡️ MORE GAME WILL COMING SOON.```"
)

RIDDLE_WINNER_STRING = (
     "🎉  𝐂𝐨𝐧𝐠𝐫𝐚𝐭𝐮𝐥𝐚𝐭𝐢𝐨𝐧𝐬, {}! 𝐘𝐨𝐮'𝐫𝐞 𝐭𝐡𝐞 𝐟𝐢𝐫𝐬𝐭 𝐭𝐨 𝐬𝐨𝐥𝐯𝐞 𝐓𝐇𝐄 {} 𝐑𝐈𝐃𝐃𝐋𝐄! 🥇\n\n"
     "🧠 𝐓𝐨𝐭𝐚𝐥 𝐒𝐨𝐥𝐯𝐞𝐝: {}\n"
     "🧠 𝐓𝐢𝐦𝐞 𝐓𝐚𝐤𝐞𝐧: {}\n"
)

     

####################################################################################################
