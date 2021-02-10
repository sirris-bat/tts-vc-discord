#!/bin/python
import discord
import logging

import asyncio
import websockets

from config import Config
from api import Api

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

api = Api()
startApi = websockets.serve(api.handler, 'localhost', 4000)
asyncio.get_event_loop().run_until_complete(startApi)
asyncio.get_event_loop().run_forever()
client.run(config.token)
