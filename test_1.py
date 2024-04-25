import sys
from PyQt6 import QtWidgets
import pyqtgraph as pg

from plots import make_plot_temp, make_plot_water, make_plot_power, make_plot_soul
from websocket_c_t import WebSocketClientThread


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Create and start WebSocket client thread
        self.websocket_client_thread = WebSocketClientThread()
        self.websocket_client_thread.temperature_received.connect(self.update_plots)
        self.websocket_client_thread.connection_failed.connect(self.handle_connection_failed)
        self.websocket_client_thread.start()  # Start the thread

        # Layout for plots
        self.layout = QtWidgets.QVBoxLayout()

        # button
        self.temp_button = QtWidgets.QPushButton('Temperature')
        self.power_button = QtWidgets.QPushButton('Power')
        self.soul_button = QtWidgets.QPushButton('Soul')
        self.water_button = QtWidgets.QPushButton('Water')

        self.buttons = []
        self.buttons.append(self.temp_button)
        self.buttons.append(self.power_button)
        self.buttons.append(self.soul_button)
        self.buttons.append(self.water_button)

        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout.addWidget(self.temp_button)
        self.buttons_layout.addWidget(self.power_button)
        self.buttons_layout.addWidget(self.soul_button)
        self.buttons_layout.addWidget(self.water_button)

        self.layout.addLayout(self.buttons_layout)

        self.temp_button.clicked.connect(
            lambda: self.plot_widget_temp.hide() if self.plot_widget_temp.isVisible() else self.plot_widget_temp.show())
        self.water_button.clicked.connect(
            lambda: self.plot_widget_water.hide() if self.plot_widget_water.isVisible() else self.plot_widget_water.show())
        self.power_button.clicked.connect(
            lambda: self.plot_widget_power.hide() if self.plot_widget_power.isVisible() else self.plot_widget_power.show())
        self.soul_button.clicked.connect(
            lambda: self.plot_widget_soul.hide() if self.plot_widget_soul.isVisible() else self.plot_widget_soul.show())

        # Создание списка графиков
        self.plot_widgets = []
        # создание графиков
        self.plot_widget_temp = make_plot_temp(self)
        self.plot_widget_power = make_plot_power(self)
        self.plot_widget_water = make_plot_water(self)
        self.plot_widget_soul = make_plot_soul(self)

        self.central_widget = QtWidgets.QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

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

    def handle_connection_failed(self):
        self.setWindowTitle("Прибор не подключен")

    def update_plots(self, sens_to_send, sens_name):
        self.setWindowTitle("Прибор подключен")
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
        print("Close event triggered")
        self.websocket_client_thread.quit()  # Signal the thread to stop
        self.websocket_client_thread.wait()  # Wait for the thread to finish
        print("а сюда")
        super().closeEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
