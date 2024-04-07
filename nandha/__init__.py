import config 
import logging


from pyrogram import Client
from pymongo import MongoClient, errors as pymongo_errors


FORMAT = f"[{config.NAME}] %(message)s"
logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler('logs.txt'),
              logging.StreamHandler()], format=FORMAT)


# bot client 
bot = Client(  
  name=config.NAME,
  api_id=config.API_ID,
  api_hash=config.API_HASH,
  bot_token=config.BOT_TOKEN,
  plugins=dict(root="nandha"))

# database mongo_db
DB = MongoClient(config.DB_URL)

try:
   DB.server_info()
except pymongo_errors.ConnectionFailure:
     print("Connection failure, INVALID MONGO DB URL maybe!, DOWN!")
     sys.exit()


DATABASE = DB['GOJO-QUIZE']


