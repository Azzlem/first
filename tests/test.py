import sys
import asyncio
import websockets
from PyQt6 import QtCore, QtWidgets
import pyqtgraph as pg


class WebSocketClientThread(QtCore.QThread):
    """
    Separate thread for handling WebSocket communication with the server.
    Emits a signal with the received temperature data.
    """
    temperature_received = QtCore.pyqtSignal(float, str)
    connection_closed = QtCore.pyqtSignal()

    def run(self):
        asyncio.run(self._run_async())  # Run the coroutine in the thread

    async def _run_async(self):
        try:
            async with websockets.connect("ws://localhost:8000") as websocket:
                # Send "Я готов" message
                await websocket.send("Я готов")

                while True:
                    # Receive messages from the server
                    reply = await websocket.recv()
                    if reply:
                        sens_to_send, sens_name = map(str.strip, reply.split(","))
                        self.temperature_received.emit(float(sens_to_send), sens_name)
                    else:
                        print("Received empty message.")
        except websockets.ConnectionClosed:
            print("WebSocket connection closed.")
            self.connection_closed.emit()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Create and start WebSocket client thread
        self.websocket_client_thread = WebSocketClientThread()
        self.websocket_client_thread.temperature_received.connect(self.update_plots)
        self.websocket_client_thread.connection_closed.connect(self.handle_connection_closed)
        self.websocket_client_thread.start()  # Start the thread

        # Layout for plots
        layout = QtWidgets.QVBoxLayout()

        # button
        temp_button = QtWidgets.QPushButton('Temperature')
        power_button = QtWidgets.QPushButton('Power')
        soul_button = QtWidgets.QPushButton('Soul')
        water_button = QtWidgets.QPushButton('Water')

        self.buttons = [temp_button, power_button, soul_button, water_button]

        buttons_layout = QtWidgets.QHBoxLayout()
        for button in self.buttons:
            buttons_layout.addWidget(button)

        layout.addLayout(buttons_layout)

        # Create four plots
        self.plot_widgets = []

        colors = ["w", "b", "y", "r"]
        titles = ["Temperature", "Power", "Water", "Soul"]
        y_labels = ["Temperature (°C)", "Power (H)", "Water (L)", "Soul (шт)"]

        for color, title, y_label in zip(colors, titles, y_labels):
            plot_widget = pg.PlotWidget()
            plot_widget.setBackground(color)
            plot_widget.setTitle(title, color="b", size="20pt")
            styles = {"color": "black", "font-size": "18px"}
            plot_widget.setLabel("left", y_label, **styles)
            plot_widget.setLabel("bottom", "Time (sec)", **styles)
            plot_widget.addLegend()
            plot_widget.showGrid(x=True, y=True)
            plot_widget.setYRange(20, 40)
            self.plot_widgets.append(plot_widget)
            layout.addWidget(plot_widget)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.plots_data = {f"sens_{i+1}": {"times": [], "temperatures": [], "lines": None} for i in range(4)}

    def update_plots(self, sens_to_send, sens_name):
        max_points = 100
        sens_data = self.plots_data[sens_name]
        times, temperatures = sens_data["times"], sens_data["temperatures"]

        if len(times) > max_points:
            sens_data["times"] = times[-max_points:]
            sens_data["temperatures"] = temperatures[-max_points:]

        times.append(times[-1] + 1 if times else 1)
        temperatures.append(sens_to_send)

        if not sens_data["lines"]:
            pen = pg.mkPen(color=(255, 0, 0))
            sens_data["lines"] = self.plot_widgets[int(sens_name[-1]) - 1].plot(
                times,
                temperatures,
                name=f"Temperature Sensor {sens_name}",
                pen=pen,
                symbol="o",
                symbolSize=15,
                symbolBrush="b",
            )
            self.plot_widgets[int(sens_name[-1]) - 1].setYRange(0, 10)
            self.plot_widgets[int(sens_name[-1]) - 1].setXRange(0, 100)
        else:
            sens_data["lines"].setData(times, temperatures)

        max_x = max([max(data["times"]) for data in self.plots_data.values()])
        min_x = max(max_x - max_points, 0)
        for plot_widget in self.plot_widgets:
            plot_widget.setXRange(min_x, max_x + 1)

    def handle_connection_closed(self):
        print("Connection closed.")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
