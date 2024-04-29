import asyncio
import random

import websockets


async def send_periodic_message(websocket):
    while True:
        await asyncio.sleep(0.25)
        temp = random.randint(1, 10)
        power = random.randint(1, 10)
        water = random.randint(1, 10)
        soul = random.randint(1, 10)
        hr = random.randint(1, 10)
        spo = random.randint(1, 10)
        red = random.randint(1, 10)
        ir = random.randint(1, 10)

        list_sensors = [temp, power, water, soul, hr, spo, red, ir]
        sensor_to_send = random.choice(list_sensors)
        name_sensor_list = ['temp', 'power', 'water', 'soul', 'hr', 'spo', 'red', 'ir']
        name_sensor = random.choice(name_sensor_list)

        await websocket.send(f'{sensor_to_send},{name_sensor}')


async def handle_client(websocket, path):
    while True:
        try:
            # Прием сообщения от клиента
            data = await websocket.recv()
            print(f"Received from {path}: {data}")

            # Проверка сообщения "Я готов"
            if data == "Я готов":
                # Запуск отправки периодических сообщений
                await asyncio.create_task(send_periodic_message(websocket))
                print("Periodic messages started.")
            else:
                print(f"Invalid message: {data}")

        except websockets.ConnectionClosedError:
            print(f"Client {path} disconnected.")
            break


async def main():
    async with websockets.serve(handle_client, "localhost", 8000):
        print("WebSocket server is running on port 8000.")
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
