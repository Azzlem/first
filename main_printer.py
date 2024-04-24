import asyncio
import websockets

async def connect_to_server():
    async with websockets.connect("ws://localhost:8000") as websocket:
        # Отправка сообщения "Я готов"
        await websocket.send("Я готов")

        while True:
            # Получение сообщений от сервера
            reply = await websocket.recv()

            if reply == "Я работаю":
                print(f"Server message: {reply}")
            else:
                print(f"Unexpected message: {reply} ({type(reply)})")


try:
    asyncio.run(connect_to_server())
except KeyboardInterrupt:
    pass
