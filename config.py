import os

# default variable
NAME = 'GojoQuizeBot'
SUPPORT_URL = 'nandhasupport.t.me'
CHANNEL_URL = 'nandhabots.t.me'


# checks if the env is true then program takes variable from environment else here.
if bool(os.getenv('ENV')) == True:
     OWNER_ID = int(os.getenv('OWNER_ID'))
     BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
     API_ID = int(os.getenv('API_ID'))
     API_HASH = str(os.getenv('API_HASH'))
else:
    API_ID = 1234567
    API_HASH = ''
    BOT_TOKEN = ''
     
  
     


