

from nandha import DATABASE
from nandha import bot
from pyrogram import filters

db = DATABASE['GIT-BOT']

import re
import requests


async def add_repo(user_id: int, repo_url: str, group_id: int, token=None):
    data = {
       'user_id': user_id,
       'repo_url': repo_url,
       'group_id': group_id,
       'token': token
    }
    db.insert_one(data)
    return True



  

@bot.on_message(filters.command('gitc'))
async def git_connect(_, message):
     user_id = message.from_user.id
  
     pattern = r'^https?:github.com\.com'
     if len(message.text.split()) < 2:
          return await message.reply(
            'Example: /gitc -r repo_url -g group_id'
          )
     repo_url = message.text.split('-r')[1]
     group_id = message.text.split('-g')[1]
     match = re.match(pattern, repo_url)
     if not match:
         return await message.reply(
           'Did not match as github repo url maybe use this format `https://github.com/username/repo`'
         )
     else:
         owner_name = repo_url.split('/')[-2]
         repo_name = repo_url.split('/')[-1]
         api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits'
         req = requests.get(api_url).json()
         if '-t' in message.text:
              token = message.text.split('-t')[1]
              await add_repo(
                  user_id=user_id,
                  repo_url=repo_url,
                  group_id=group_id,
                  token=token)
              return await message.reply(
               f'Successfully connected your {repo_url} private repo.\nJoin @NandhaBots'
              )
           
           
         if req['message']:
            return await message.reply('You are connecting a private repo, I need git token to access the private repos, use `/gitc -r repo_url -g group_id -t token`')
         
         elif req['id']:
             await add_repo(
                  user_id=user_id,
                  repo_url=repo_url,
                  group_id=group_id)
             return await message.reply(
               f'Successfully connected your {repo_url} public repo.\nJoin @NandhaBots'
             )
                  


              
           
         
 
           
           
    
