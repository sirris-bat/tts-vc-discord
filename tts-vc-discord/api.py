import asyncio
import websockets
from websockets import WebSocketServerProtocol

import logging

logging.basicConfig(level=logging.INFO)

class Api:
    def __init__(self):
        apiWebsocket = websockets.serve(self.handler, 'localhost', 4000)
        asyncio.get_event_loop().run_until_complete(apiWebsocket)

    async def handler(self, websocket, path):
        if path.startswith('/connect/'):
            channelId = path.split('/')[2]
            logging.info(channelId)
            await websocket.send(channelId)
