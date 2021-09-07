import asyncio
import websockets
import ssl


async def hello(uri):
    ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
    async with ws.connect(uri) as websocket:
        for i in range(10):
            await websocket.send(str(i))
            print(f"(client) send to server: " + str(i))
            name = await websocket.recv()
            print(f"(client) recv from server {name}")

asyncio.get_event_loop().run_until_complete(
    hello('wss://localhost:443'))
