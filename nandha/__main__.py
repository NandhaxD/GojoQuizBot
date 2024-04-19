import asyncio
from nandha import bot

async def main():
    await bot.start()
    print('The bot has now started.')
    
    info = await bot.get_me()
    bot_username = info.username
    bot_id = info.id

if __name__ == "__main__":
    asyncio.run(main())
