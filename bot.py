#!/bin/python
import discord
import logging

import asyncio
import websockets

import time

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
    _voiceClient = None

    async def connect_to_vc(self, channelId):
        self._voiceClient = await self.get_channel(channelId).connect()

    async def on_ready(self):
        logging.info('Logged in as {0.user}'.format(self))

    async def on_message(self, message):
        # TODO: check config to see if this is enabled
        # Safety: Don't reply to self
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!connect'):
            # Connect to author's current voice channel
            if message.author.voice.channel is not None:
                await self.connect_to_vc(message.author.voice.channel.id)

        if message.content.startswith("!say"):
            # Speak in voice channel
            return

api = Api()
ttsBot = TtsBot()
ttsBot.run(config.token)
