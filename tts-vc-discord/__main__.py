import sys

from discord.ext import commands

from .config import Config
from .webserver import WebServer
from .bot import TtsBot, BotCommands

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    config = Config()

    webserver = WebServer()
    webserver.run()
    ttsbot = TtsBot(command_prefix=commands.when_mentioned_or('!'),
                    description='An obnoxious and unab=voidable TTS bot')
    ttsbot.add_cog(BotCommands(ttsbot))
    ttsbot.run(config.token)

if __name__ == "__main__":
    sys.exit(main())
