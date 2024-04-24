import sys
import asyncio
from random import randint

import websockets
from PyQt6 import QtCore, QtWidgets
import pyqtgraph as pg


class WebSocketClientThread(QtCore.QThread):
    """
    Separate thread for handling WebSocket communication with the server.
    Emits a signal with the received temperature data.
    """
    temperature_received = QtCore.pyqtSignal(float, str)

    def run(self):
        asyncio.run(self._run_async())  # Run the coroutine in the thread

    async def _run_async(self):
        async with websockets.connect("ws://localhost:8000") as websocket:
            # Send "Я готов" message
            await websocket.send("Я готов")

            while True:
                try:
                    # Receive messages from the server
                    reply = await websocket.recv()
                    if reply or reply != -1:
                        # Simulate receiving temperature data

                        sens_to_send = int(reply.split(",")[0])
                        sens_name = reply.split(",")[1]
                        self.temperature_received.emit(sens_to_send, sens_name)
                        print(sens_name, sens_to_send)
                    else:
                        print(reply)
                        print(f"Unexpected message: {reply} ({type(reply)})")
                except websockets.ConnectionClosed:
                    print("WebSocket connection closed.")
                    break


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Create and start WebSocket client thread
        self.websocket_client_thread = WebSocketClientThread()
        self.websocket_client_thread.temperature_received.connect(self.update_plots)
        self.websocket_client_thread.start()  # Start the thread

        # Layout for plots
        layout = QtWidgets.QVBoxLayout()

        # Create four plots
        self.plot_widgets = []
        # for _ in range(4):
        #     plot_widget = pg.PlotWidget()
        #     plot_widget.setBackground("w")
        #     pen = pg.mkPen(color=(255, 0, 0))
        #     plot_widget.setTitle("Temperature vs Time", color="b", size="20pt")
        #     styles = {"color": "red", "font-size": "18px"}
        #     plot_widget.setLabel("left", "Temperature (°C)", **styles)
        #     plot_widget.setLabel("bottom", "Time (sec)", **styles)
        #     plot_widget.addLegend()
        #     plot_widget.showGrid(x=True, y=True)
        #     plot_widget.setYRange(20, 40)
        #     self.plot_widgets.append(plot_widget)
        #     layout.addWidget(plot_widget)

        plot_widget_temp = pg.PlotWidget()
        plot_widget_temp.setBackground("w")
        pen = pg.mkPen(color=(255, 0, 0))
        plot_widget_temp.setTitle("Temperature", color="b", size="20pt")
        styles = {"color": "black", "font-size": "18px"}
        plot_widget_temp.setLabel("left", "Temperature (°C)", **styles)
        plot_widget_temp.setLabel("bottom", "Time (sec)", **styles)

        plot_widget_temp.addLegend()
        plot_widget_temp.showGrid(x=True, y=True)
        plot_widget_temp.setYRange(20, 40)
        self.plot_widgets.append(plot_widget_temp)
        layout.addWidget(plot_widget_temp)

        plot_widget_power = pg.PlotWidget()
        plot_widget_power.setBackground("b")
        pen = pg.mkPen(color=(255, 0, 0))
        plot_widget_power.setTitle("Power", color="w", size="20pt")
        styles = {"color": "black", "font-size": "18px"}
        plot_widget_power.setLabel("left", "Power (H)", **styles)
        plot_widget_power.setLabel("bottom", "Time (sec)", **styles)
        plot_widget_power.addLegend()
        plot_widget_power.showGrid(x=True, y=True)
        plot_widget_power.setYRange(20, 40)
        self.plot_widgets.append(plot_widget_power)
        layout.addWidget(plot_widget_power)

        plot_widget_water = pg.PlotWidget()
        plot_widget_water.setBackground("y")
        pen = pg.mkPen(color=(255, 0, 0))
        plot_widget_water.setTitle("Water", color="g", size="20pt")
        styles = {"color": "black", "font-size": "18px"}
        plot_widget_water.setLabel("left", "Water (L)", **styles)
        plot_widget_water.setLabel("bottom", "Time (sec)", **styles)
        plot_widget_water.addLegend()
        plot_widget_water.showGrid(x=True, y=True)
        plot_widget_water.setYRange(20, 40)
        self.plot_widgets.append(plot_widget_water)
        layout.addWidget(plot_widget_water)

        plot_widget_soul = pg.PlotWidget()
        plot_widget_soul.setBackground("r")
        pen = pg.mkPen(color=(255, 0, 0))
        plot_widget_soul.setTitle("Soul", color="b", size="20pt")
        styles = {"color": "black", "font-size": "18px"}
        plot_widget_soul.setLabel("left", "Soul (шт)", **styles)
        plot_widget_soul.setLabel("bottom", "Time (sec)", **styles)
        plot_widget_soul.addLegend()
        plot_widget_soul.showGrid(x=True, y=True)
        plot_widget_soul.setYRange(20, 40)
        self.plot_widgets.append(plot_widget_soul)
        layout.addWidget(plot_widget_soul)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Initialize data for plots
        # self.times = [[] for _ in range(4)]
        # self.temperatures = [[] for _ in range(4)]
        # self.lines = [None] * 4

        self.times_1 = []
        self.times_2 = []
        self.times_3 = []
        self.times_4 = []

        self.temperatures_1 = []
        self.temperatures_2 = []
        self.temperatures_3 = []
        self.temperatures_4 = []

        self.lines_1 = []
        self.lines_2 = []
        self.lines_3 = []
        self.lines_4 = []

    def update_plots(self, sens_to_send, sens_name):
        max_points = 100
        if len(self.times_1) > max_points:
            self.times_1 = self.times_1[-max_points:]
            self.temperatures_1 = self.temperatures_1[-max_points:]
        if len(self.times_2) > max_points:
            self.times_2 = self.times_2[-max_points:]
            self.temperatures_2 = self.temperatures_2[-max_points:]
        if len(self.times_3) > max_points:
            self.times_3 = self.times_3[-max_points:]
            self.temperatures_3 = self.temperatures_3[-max_points:]
        if len(self.times_4) > max_points:
            self.times_4 = self.times_4[-max_points:]
            self.temperatures_4 = self.temperatures_4[-max_points:]



        if sens_name == "temp":
            self.times_1.append(self.times_1[-1] + 1 if self.times_1 else 1)
            self.temperatures_1.append(int(sens_to_send))

            if not self.lines_1:
                pen = pg.mkPen(color=(255, 0, 0))
                self.lines_1 = self.plot_widgets[0].plot(
                    self.times_1,
                    self.temperatures_1,
                    name=f"Temperature Sensor {sens_name}",
                    pen=pen,
                    symbol="o",
                    symbolSize=15,
                    symbolBrush="b",
                )
                self.plot_widgets[0].setYRange(0, 10)
                self.plot_widgets[0].setXRange(0, 100)
                # self.plot_widgets[0].enableAutoRange(pg.ViewBox.XAxis, enable=True)
                # self.plot_widgets[0].enableAutoRange(axis='x')

            else:
                self.lines_1.setData(self.times_1, self.temperatures_1)

        if sens_name == "power":
            self.times_2.append(self.times_2[-1] + 1 if self.times_2 else 1)
            self.temperatures_2.append(int(sens_to_send))
            if not self.lines_2:
                pen = pg.mkPen(color=(255, 0, 0))
                self.lines_2 = self.plot_widgets[1].plot(
                    self.times_2,
                    self.temperatures_2,
                    name=f"Temperature Sensor {sens_name}",
                    pen=pen,
                    symbol="o",
                    symbolSize=15,
                    symbolBrush="b",
                )
                self.plot_widgets[1].setYRange(0, 10)
                self.plot_widgets[1].setXRange(0, 100)
            else:
                self.lines_2.setData(self.times_2, self.temperatures_2)

        if sens_name == "water":
            self.times_3.append(self.times_3[-1] + 1 if self.times_3 else 1)
            self.temperatures_3.append(int(sens_to_send))
            if not self.lines_3:
                pen = pg.mkPen(color=(255, 0, 0))
                self.lines_3 = self.plot_widgets[2].plot(
                    self.times_3,
                    self.temperatures_3,
                    name=f"Temperature Sensor {sens_name}",
                    pen=pen,
                    symbol="o",
                    symbolSize=15,
                    symbolBrush="b",
                )
                self.plot_widgets[2].setYRange(0, 10)
                self.plot_widgets[2].setXRange(0, 100)
            else:
                self.lines_3.setData(self.times_3, self.temperatures_3)

        if sens_name == "soul":
            self.times_4.append(self.times_4[-1] + 1 if self.times_4 else 1)
            self.temperatures_4.append(int(sens_to_send))
            if not self.lines_4:
                pen = pg.mkPen(color=(255, 0, 0))
                self.lines_4 = self.plot_widgets[3].plot(
                    self.times_4,
                    self.temperatures_4,
                    name=f"Temperature Sensor {sens_name}",
                    pen=pen,
                    symbol="o",
                    symbolSize=15,
                    symbolBrush="b",
                )
                self.plot_widgets[3].setYRange(0, 10)
                self.plot_widgets[3].setXRange(0, 100)
            else:
                self.lines_4.setData(self.times_4, self.temperatures_4)

        for i, plot_widget in enumerate(self.plot_widgets):
            max_x = max(self.times_1 + self.times_2 + self.times_3 + self.times_4)
            min_x = max(max_x - max_points, 0)
            plot_widget.setXRange(min_x, max_x + 1)

    def closeEvent(self, event):
        """
        Stop the WebSocket client thread gracefully when the window is closed.
        """
        self.websocket_client_thread.quit()  # Signal the thread to stop
        self.websocket_client_thread.wait()  # Wait for the thread to finish
        super().closeEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
