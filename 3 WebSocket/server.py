import asyncio
import websockets

async def handle_websocket(websocket, path):
    try:
        while True:
            message = await websocket.recv()
            print(f"Received message: {message}")

            # Echo the received message back to the client
            await websocket.send(f"Server received: {message}")
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Connection closed with code: {e.code}, reason: {e.reason}")

start_server = websockets.serve(handle_websocket, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()