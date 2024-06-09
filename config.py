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
BOT_ID = int(BOT_TOKEN.split(':')[0])
DEVS_ID = [ 5456798232, 5696053228, 7132604388]

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


RIDDLE_WINNER_STRING = (
     "🎉 Congratulations, {}! You're the first to solve **THE MATH RIDDLE**!  🥇\n\n"
     "🧠 **Solved Puzzles:** {}\n"
     "🧠 **Time Taken:** {}\n"
)
     
