from aiohttp import web
import os

webdir = "../web"

class WebServer(web.Application):
    def __init__(self):
        super().__init__()
        self.add_routes([web.static('/', os.path.join(os.getcwd(), webdir)),
                         web.get('/connect/{channelid}', self._ws_handle_connect)])
        web.run_app(self)

    async def _ws_handle_connect(request):
        channelid = request.match_info.get('channelid')
        ws = web.WebSocketResponse()
        await ws.prepare(request)
        ws.send_str(channelid)
        return ws
