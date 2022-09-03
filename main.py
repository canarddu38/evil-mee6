import discord
from discord import Webhook
import os
import requests
import aiohttp
import random

class evil-mee6(discord.Client):
    async def on_ready(self):
        print("Ready!")
        

    async def on_member_join(member):
        



    async def on_message(self, message):
        if message.content.startswith('/help'):
            await message.channel.send("test")


intents = discord.Intents.default()
intents.message_content = True
client = evil-mee6(intents=intents)


client.run(os.environ['DISCORD_TOKEN'])
