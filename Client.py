# bot.py
import os
import discord
from dotenv import load_dotenv
import pandas as pd
import numpy as np

df = pd.read_csv("jokes.csv")
joke = df.sample(axis= 0)

class MyClient(discord.Client):

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_message(self, message):
        global joke
        #content = message.content
        
        if message.content.startswith("?joke"):
            question = np.array(joke["Question"])
            await message.channel.send(question[0])
        
        if message.content.startswith("?answer"):
            answer = np.array(joke["Answer"])
            await message.channel.send(answer[0])
            joke=df.sample(axis=0)

    # async def on_typing(self, channel, user, when):
    #     await self.wait_until_ready()
    #     await channel.send(f"Hey joh dikzak {str(user)[:-5]} wat zit je te typen??")

def main():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    client = MyClient()
    client.run(TOKEN)

if __name__=='__main__':
    main()
