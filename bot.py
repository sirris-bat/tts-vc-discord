#!/bin/python
import discord
import logging

from config import Config

config = Config()

intents = discord.Intents.none()
client = discord.Client()

logger = logging.getLogger('discord')
logger.setLevel(config.logLevel)
if config.logFile is not None:
    handler = logging.FileHandler(filename=config.logFile, encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

@client.event
async def on_ready():
    logging.info('Logged in as {0.user}'.format(client))

client.run(config.token)
