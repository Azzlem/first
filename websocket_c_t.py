import asyncio
import websockets
from PyQt6 import QtCore, QtWidgets


class WebSocketClientThread(QtCore.QThread):
    """
    Separate thread for handling WebSocket communication with the server.
    Emits a signal with the received temperature data.
    """
    temperature_received = QtCore.pyqtSignal(float, str)
    connection_succeeded = QtCore.pyqtSignal()
    connection_failed = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.running = False

    def run(self):
        self.running = True
        try:
            asyncio.run(self._run_async())  # Run the coroutine in the thread
        except ConnectionRefusedError:
            self.connection_failed.emit()

    async def _run_async(self):
        while self.running:
            try:
                async with websockets.connect("ws://localhost:8000") as websocket:
                    # Send "Я готов" message
                    await websocket.send("Я готов")

                    # Connection established, update the window title
                    self.connection_succeeded.emit()

                    while self.running:
                        # Receive messages from the server
                        reply = await websocket.recv()
                        if reply or reply != -1:
                            # Simulate receiving temperature data
                            sens_to_send = int(reply.split(",")[0])
                            sens_name = reply.split(",")[1]
                            self.temperature_received.emit(sens_to_send, sens_name)
                            # print(sens_name, sens_to_send)
                        else:
                            print(reply)
                            print(f"Unexpected message: {reply} ({type(reply)})")
            except websockets.ConnectionClosed:
                print("WebSocket connection closed.")
            except ConnectionRefusedError:
                self.connection_failed.emit()
                await asyncio.sleep(1)  # Wait before retrying connection

    def stop(self):
        self.running = False
