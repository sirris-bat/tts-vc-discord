from aiohttp import web
from discord.ext import commands
import os

webdir = "web"


class WebServer(commands.Cog):
    def __init__(self, ttsbot):
        self.ttsbot = ttsbot

    async def serve(self, address='localhost', port=8080):
        app = web.Application()
        app.add_routes([web.get('/', self._http_handler_index),
                         web.get('/script.js', self._http_handler_js),
                         web.get('/style.css', self._http_handler_css),
                         web.get('/connect/{channelid}', self._ws_handler_connect),
                         web.get('/say', self._ws_handler_say)])
        runner = web.AppRunner(app)
        await runner.setup()
        self.site = web.TCPSite(runner, address, port)
        await self.ttsbot.wait_until_ready()
        await self.site.start()

    def _unload(self):
        asyncio.ensure_future(self.site.stop())

    async def _http_handler_index(self, request):
        return web.FileResponse(os.path.join(os.getcwd(), webdir, 'index.html'))

    async def _http_handler_js(self, request):
        return web.FileResponse(os.path.join(os.getcwd(), webdir, 'script.js'))

    async def _http_handler_css(self, request):
        return web.FileResponse(os.path.join(os.getcwd(), webdir, 'style.css'))

    async def _ws_handler_connect(self, request):
        channelid = request.match_info.get('channelid')

        await self.ttsbot.connect_to_vc(int(channelid))

        ws = web.WebSocketResponse()
        await ws.prepare(request)
        await ws.send_str(channelid)
        await ws.close()

        return ws

    async def _ws_handler_say(self, request):
        ws = web.WebSocketResponse()
        await ws.prepare(request)

        async for msg in ws:
            phrase = msg.data
            await self.ttsbot.say(phrase)
            await ws.send_str(phrase)

        await ws.close()

        return ws
