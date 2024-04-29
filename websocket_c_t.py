import asyncio
import json

import websockets
from PyQt6 import QtCore
import io


class WebSocketClientThread(QtCore.QThread):
    temperature_received = QtCore.pyqtSignal(float, str)
    connection_succeeded = QtCore.pyqtSignal()
    connection_failed = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.running = False

    def run(self):
        self.running = True
        try:
            asyncio.run(self._run_async())
        except ConnectionRefusedError:
            self.connection_failed.emit()

    async def _run_async(self):
        while self.running:
            try:
                async with websockets.connect("ws://localhost:8000") as websocket:
                    # Send "Я готов" message
                    await websocket.send("Я готов")

                    self.connection_succeeded.emit()

                    while self.running:

                        reply = await websocket.recv()
                        if reply and reply != -1:
                            sens_to_send = int(reply[:reply.find(",")])
                            sens_name = reply[reply.find(",") + 1:]
                            self.temperature_received.emit(sens_to_send, sens_name)

                            # with io.open("data.json", 'r+') as f:
                            #     data = json.load(f)
                            #     data['items'].append({sens_name: sens_to_send})
                            #     f.seek(0)
                            #     json.dump(data, f, indent=4)
                        else:
                            print(reply)
                            print(f"Unexpected message: {reply} ({type(reply)})")
            except websockets.ConnectionClosed:
                print("WebSocket connection closed.")
            except ConnectionRefusedError:
                self.connection_failed.emit()
                await asyncio.sleep(1)

    def stop(self):
        self.running = False
