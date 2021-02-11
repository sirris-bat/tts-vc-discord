#!/bin/python
import discord
import logging

import asyncio
import websockets

from config import Config
from api import Api

config = Config()

intents = discord.Intents.none()

logger = logging.getLogger('discord')
logger.setLevel(config.logLevel)
if config.logFile is not None:
    handler = logging.FileHandler(filename=config.logFile, encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

class TtsBot(discord.Client):
    async def on_ready():
        logging.info('Logged in as {0.user}'.format(client))

    async def on_message():
        # TODO: check config to see if this is enabled
        # Safety: Don't reply to self
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!connect'):
            # Connect to author's current voice channel
            return

        if message.content.startswith("!say"):
            # Speak in voice channel
            return

api = Api()
ttsBot = TtsBot()
ttsBot.run(config.token)
