import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow
from main import Ui_Medical_application
from plots_new import make_plot_eeg, make_plot_emg, make_plot_ecg, make_plot_gsr
from utils import clicked_button, time_biggest_max_point, update_sensor_data
from websocket_c_t import WebSocketClientThread


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Medical_application()
        self.ui.setupUi(self)
        self.ui.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.websocket_client_thread = WebSocketClientThread()
        self.websocket_client_thread.temperature_received.connect(self.update_plots)
        self.websocket_client_thread.connection_failed.connect(self.handle_connection_failed)
        self.websocket_client_thread.start()

        self.ui.eeg_frame_btn_cheb.setStyleSheet("background-color: darkCyan;")
        self.ui.emg_frame_btn_cheb.setStyleSheet("background-color: darkCyan;")
        self.ui.ecg_frame_btn_cheb.setStyleSheet("background-color: darkCyan;")
        self.ui.gsr_frame_btn_cheb.setStyleSheet("background-color: darkCyan;")
        self.ui.pulse_frame.setStyleSheet("background-color: darkCyan;")

        self.ui.eeg_checkbox.setStyleSheet("color: black;")
        self.ui.emg_checkbox.setStyleSheet("color: black")
        self.ui.ecg_checkbox.setStyleSheet("color: black")
        self.ui.gsr_checkbox.setStyleSheet("color: black")

        self.ui.eeg_screenshot_button.setStyleSheet("color: black; background-color: darkCyan;border: none;")
        self.ui.emg_screenshot_button.setStyleSheet("color: black; background-color: darkCyan;border: none;")
        self.ui.ecg_screenshot_button.setStyleSheet("color: black; background-color: darkCyan;border: none;")
        self.ui.gsr_screenshot_button.setStyleSheet("color: black; background-color: darkCyan;border: none;")
        self.ui.pulse_screenshot_button.setStyleSheet("color: black; background-color: black;border: none;")

        self.ui.eeg_screenshot_button.setIcon(QIcon("tests/icons/free-icon-screenshot-5370960.png"))
        self.ui.emg_screenshot_button.setIcon(QIcon("tests/icons/free-icon-screenshot-5370960.png"))
        self.ui.ecg_screenshot_button.setIcon(QIcon("tests/icons/free-icon-screenshot-5370960.png"))
        self.ui.gsr_screenshot_button.setIcon(QIcon("tests/icons/free-icon-screenshot-5370960.png"))
        self.ui.pulse_screenshot_button.setIcon(QIcon("tests/icons/free-icon-screenshot-5370960.png"))

        self.ui.plot_widgets = []
        self.ui.eeg_widget = make_plot_eeg(self.ui)
        self.ui.emg_widget = make_plot_emg(self.ui)
        self.ui.ecg_widget = make_plot_ecg(self.ui)
        self.ui.gsr_widget = make_plot_gsr(self.ui)

        clicked_button(self.ui.eeg_checkbox, self.ui.eeg_widget)
        clicked_button(self.ui.emg_checkbox, self.ui.emg_widget)
        clicked_button(self.ui.ecg_checkbox, self.ui.ecg_widget)
        clicked_button(self.ui.gsr_checkbox, self.ui.gsr_widget)

        self.ui.times_eeg = []
        self.ui.times_emg = []
        self.ui.times_ecg = []
        self.ui.times_gst = []
        self.ui.times = []
        self.ui.times.append(self.ui.times_eeg)
        self.ui.times.append(self.ui.times_emg)
        self.ui.times.append(self.ui.times_ecg)
        self.ui.times.append(self.ui.times_gst)

        self.ui.temperatures_1 = []
        self.ui.temperatures_2 = []
        self.ui.temperatures_3 = []
        self.ui.temperatures_4 = []

        self.ui.lines_1 = []
        self.ui.lines_2 = []
        self.ui.lines_3 = []
        self.ui.lines_4 = []

    def handle_connection_failed(self):
        self.setWindowTitle("Прибор не подключен")

    def update_plots(self, sens_to_send, sens_name):
        self.setWindowTitle("Прибор подключен")
        max_points = 100
        time_biggest_max_point(self, max_points)

        # if sens_name == "temp":
        #     update_sensor_data(sens_name, sens_to_send, self.ui.times_eeg, self.ui.temperatures_1,
        #                        self.ui.plot_widgets[0], self.ui.lines_1)
        # elif sens_name == "power":
        #     update_sensor_data(sens_name, sens_to_send, self.ui.times_emg, self.ui.temperatures_2,
        #                        self.ui.plot_widgets[1], self.ui.lines_2)
        # elif sens_name == "water":
        #     update_sensor_data(sens_name, sens_to_send, self.ui.times_ecg, self.ui.temperatures_3,
        #                        self.ui.plot_widgets[2], self.ui.lines_3)
        # elif sens_name == "soul":
        #     update_sensor_data(sens_name, sens_to_send, self.ui.times_gst, self.ui.temperatures_4,
        #                        self.ui.plot_widgets[3], self.ui.lines_4)
        # if sens_name == "hr":
        #     self.ui.hr_widget.setText(str(sens_to_send))
        # elif sens_name == "spo":
        #     self.ui.spo_widget.setText(str(sens_to_send))
        # elif sens_name == "red":
        #     self.ui.red_widget.setText(str(sens_to_send))
        # elif sens_name == "ir":
        #     self.ui.ir_widget.setText(str(sens_to_send))

        match sens_name:
            case "temp":
                update_sensor_data(sens_name, sens_to_send, self.ui.times_eeg, self.ui.temperatures_1,
                                   self.ui.plot_widgets[0], self.ui.lines_1)
            case "power":
                update_sensor_data(sens_name, sens_to_send, self.ui.times_emg, self.ui.temperatures_2,
                                   self.ui.plot_widgets[1], self.ui.lines_2)
            case "water":
                update_sensor_data(sens_name, sens_to_send, self.ui.times_ecg, self.ui.temperatures_3,
                                   self.ui.plot_widgets[2], self.ui.lines_3)
            case "soul":
                update_sensor_data(sens_name, sens_to_send, self.ui.times_gst, self.ui.temperatures_4,
                                   self.ui.plot_widgets[3], self.ui.lines_4)
            case "hr":
                self.ui.hr_widget.setText(str(sens_to_send))
            case "spo":
                self.ui.spo_widget.setText(str(sens_to_send))
            case "red":
                self.ui.red_widget.setText(str(sens_to_send))
            case "ir":
                self.ui.ir_widget.setText(str(sens_to_send))

        for i, plot_widget in enumerate(self.ui.plot_widgets):
            max_x = max(self.ui.times_eeg + self.ui.times_emg + self.ui.times_ecg + self.ui.times_gst, default=0)
            min_x = max(max_x - max_points, 0)
            plot_widget.setXRange(min_x, max_x + 1)

    def closeEvent(self, event):
        self.websocket_client_thread.exit(0)
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
