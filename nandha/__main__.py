from nandha import bot



if __name__ == "__main__":
      bot.run()
      print('The bot has now started.')
    


info = bot.get_me()
bot_username = info.username
bot_id = info.id
