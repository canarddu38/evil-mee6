import discord
from discord import Webhook
import os
import requests
import aiohttp
import random

class DSbot(discord.Client):
    async def on_ready(self):
        print("Ready!")
        

    async def on_member_join(member):
        



    async def on_message(self, message):
        if message.content.startswith('/help'):


intents = discord.Intents.default()
intents.message_content = True
client = DSbot(intents=intents)


client.run(os.environ['DISCORD_TOKEN'])
