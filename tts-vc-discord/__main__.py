import asyncio
import logging

from discord.ext import commands

from .config import Config
from .webserver import WebServer
from .bot import TtsBot, BotCommands


def main():
    #runner = None
    bot = None

    async def start_web(app, address='localhost', port=8080):
        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, address, port)
        await site.start()

    config = Config()

    logger = logging.getLogger('discord')
    logger.setLevel(config.logLevel)

    ttsbot = TtsBot(command_prefix=commands.when_mentioned_or('!'),
                    description='An obnoxious and unavoidable TTS bot')
    web = WebServer(ttsbot)
    ttsbot.add_cog(BotCommands(ttsbot))
    ttsbot.add_cog(web)
    ttsbot.loop.create_task(web.serve())
    ttsbot.run(config.token)


if __name__ == "__main__":
    main()
