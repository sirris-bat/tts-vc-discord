#!/bin/python
import discord
import logging

import asyncio

from discord.ext import commands

from .config import Config

config = Config()

intents = discord.Intents.none()

logger = logging.getLogger('discord')
logger.setLevel(config.logLevel)
if config.logFile is not None:
    handler = logging.FileHandler(filename=config.logFile, encoding='utf-8', mode='w')
    handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)

class TtsBot(commands.Bot):
    _voiceClient = None

    async def connect_to_vc(self, channelId):
        print(channelId)
        print(type(channelId))
        self._voiceClient = await self.get_channel(channelId).connect()

    async def on_ready(self):
        print('heck')
        logging.info('Logged in as {0.user}'.format(self))

class BotCommands(commands.Cog):
    def __init__(self, ttsbot):
        self.ttsbot = ttsbot

    @commands.command()
    async def join(self, ctx):
        if ctx.message.author.voice.channel is not None:
            await self.ttsbot.connect_to_vc(ctx.message.author.voice.channel.id)

    @commands.command()
    async def leave(self, ctx):
        await self.ttsbot.disconnect()

    @commands.command()
    async def say(self, ctx):
        # Call Bot's tts function
        return
