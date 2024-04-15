import os

# default variable
NAME = 'GojoQuizeBot'
SUPPORT_URL = 'nandhasupport.t.me'
CHANNEL_URL = 'nandhabots.t.me'
PREFIXES = ['@','.','?','!','/','~']


START_IMAGE = 'https://graph.org/file/15a7cc4a22cad1f6189f0.jpg'

RIDDLE_MATH_BG = [
     "https://graph.org/file/9b165baf9de57406d76ca.jpg",
     "https://graph.org/file/bd790b253ac3befdcff51.jpg",
     "https://graph.org/file/8ce59f8e42399029e9051.jpg",
     "https://graph.org/file/010811dae00123d74ad41.jpg"
]




# checks if the env is true then program takes variable from environment else here.
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




BOT_ID = int(BOT_TOKEN.split(':')[0])


