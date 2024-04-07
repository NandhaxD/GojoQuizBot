import os

# default variable
NAME = 'GojoQuizeBot'
SUPPORT_URL = 'nandhasupport.t.me'
CHANNEL_URL = 'nandhabots.t.me'
PREFIXES = ['.','?','!','/','~']

START_IMAGE = 'https://graph.org/file/15a7cc4a22cad1f6189f0.jpg'

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
     
  
     


