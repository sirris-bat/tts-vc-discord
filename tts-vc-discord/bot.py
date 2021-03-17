#!/bin/python
import discord
import logging

import asyncio

from io import BytesIO
from discord.ext import commands
from gtts import gTTS

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
    async def connect_to_vc(self, channelId):
        # Ensure only one voice client is active
        if self.voice_clients is not None:
            for client in self.voice_clients:
                await client.disconnect()
        # Connect with new voice client
        await self.get_channel(channelId).connect()
        self.voice_clients[0].stop()

    async def say(self, phrase):
        mp3fp = BytesIO()
        tts = gTTS(phrase)
        tts.save('x.mp3')
        self.voice_clients[0].play(discord.FFmpegPCMAudio(source='x.mp3'))

    async def on_ready(self):
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
    async def say(self, ctx, *, phrase):
        # Call Bot's tts function
        await self.ttsbot.say(phrase)
