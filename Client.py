# bot.py
import os
import discord
from dotenv import load_dotenv

class MyClient(discord.Client):
    
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_message(self, message):
        content = message.content
        msg = "Your typed message is: " + content[3:]
        if message.content.startswith("?dj"):
            await message.channel.send(msg)

    async def on_typing(self, channel, user, when):
        await self.wait_until_ready()
        await channel.send(f"Hey joh dikzak {str(user)[:-5]} wat zit je te typen??")

def main():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    client = MyClient()
    client.run(TOKEN)

if __name__=='__main__':
    main()