from aiohttp import web
import os

webdir = "web"

class WebServer(web.Application):
    def __init__(self):
        super().__init__()
        self.add_routes([web.get('/', self._http_handler_index),
                         web.get('/script.js', self._http_handler_js),
                         web.get('/style.css', self._http_handler_css),
                         web.get('/connect/{channelid}', self._ws_handler_connect)])

    def run(self):
        return web.run_app(self)

    async def _http_handler_index(self, request):
        return web.FileResponse(os.path.join(os.getcwd(), webdir, 'index.html'))

    async def _http_handler_js(self, request):
        return web.FileResponse(os.path.join(os.getcwd(), webdir, 'script.js'))

    async def _http_handler_css(self, request):
        return web.FileResponse(os.path.join(os.getcwd(), webdir, 'style.css'))

    async def _ws_handler_connect(self, request):
        channelid = request.match_info.get('channelid')

        ws = web.WebSocketResponse()
        await ws.prepare(request)
        await ws.send_str(channelid)
        await ws.close()

        return ws
