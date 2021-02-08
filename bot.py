#!/bin/python
import discord

from config import Config

intents = discord.Intents.none()
client = discord.Client()

config = Config()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

client.run(config.token)
