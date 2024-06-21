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

START_IMAGE = 'https://i.imgur.com/A8kjpZF.jpeg'
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
LB_IMG = "https://graph.org/file/2b465e523b49414688c61.jpg"


STATS_STRING = (
     "**{name}'s Stats in {chat_name}**:\n\n"
     "➤ Riddle:\n"
     "  ✪ Solved Maths ➩〘 `{rmath_points}` 〙\n"
     "  ✪ Solved Words ➩〘 `{rwords_points}` 〙\n"
     "\n\n```\n➡️ MORE GAME WILL COMING SOON.```"
)

RIDDLE_WINNER_STRING = (
     "🎉  Congratulations, {}! You're the first to solve THE {} RIDDLE! 🥇\n\n"
     "🧠 Total Solved: {}\n"
     "🧠 Time Taken: {}\n"
)

####################################################################################################
