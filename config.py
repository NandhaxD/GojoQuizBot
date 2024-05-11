import os


if bool(os.getenv('ENV')) == True:
     OWNER_ID = int(os.getenv('OWNER_ID'))
     BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
     API_ID = int(os.getenv('API_ID'))
     DB_URL = str(os.getenv('DB_URL'))
     API_HASH = str(os.getenv('API_HASH'))
else:
    API_ID = 1234567
    API_HASH = '<youre hash>' # my.telegram.org
    BOT_TOKEN = '<youre bot token>' # my.telegram.org
    DB_URL = '<db url>' #mongodb.com



# default variable
DEVS_ID = [ 5456798232 ] + [OWNER_ID]
     
NAME = 'GojoQuizBot'
SUPPORT = 'NandhaSupport'
CHANNEL = 'Nandhabots'
GROUP_ID =  -1002039454048
PREFIXES = ['/', '\\']
EMOJI = ['❤️', '⚡️', '😈', '👍', '🔥']
BOT_ID = int(BOT_TOKEN.split(':')[0])





RIDDLE_MATH_BG = [
     "https://graph.org/file/9b165baf9de57406d76ca.jpg",
     "https://graph.org/file/bd790b253ac3befdcff51.jpg",
     "https://graph.org/file/8ce59f8e42399029e9051.jpg",
     "https://graph.org/file/010811dae00123d74ad41.jpg"
]

START_IMAGE = 'https://graph.org/file/15a7cc4a22cad1f6189f0.jpg'
RIDDLE_ANSWER_GIF = 'https://graph.org/file/37cd114c92e1d74c9cc07.mp4'

