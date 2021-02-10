import asyncio
import websockets
from websockets import WebSocketServerProtocol

import logging

logging.basicConfig(level=logging.INFO)

class Api:
    async def handler(self, websocket, path):
        if path.startswith('/connect/'):
            channelId = path.split('/')[2]
            logging.info(channelId)
            await websocket.send(channelId)
