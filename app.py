import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow
from main import Ui_MainWindow  # Замените 'your_module_name' на имя вашего модуля


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.ui.eeg_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.emg_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.ecg_widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ui.gsr_widget.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.ui.eeg_frame_btn_cheb.setStyleSheet("background-color: white;")
        self.ui.emg_frame_btn_cheb.setStyleSheet("background-color: white;")
        self.ui.ecg_frame_btn_cheb.setStyleSheet("background-color: white;")
        self.ui.gsr_frame_btn_cheb.setStyleSheet("background-color: white;")
        self.ui.pulse_frame.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.ui.eeg_checkbox.setStyleSheet("color: black;")
        self.ui.emg_checkbox.setStyleSheet("color: black")
        self.ui.ecg_checkbox.setStyleSheet("color: black")
        self.ui.gsr_checkbox.setStyleSheet("color: black")

        self.ui.eeg_screenshot_button.setStyleSheet("color: black; background-color: white;border: none;")
        self.ui.emg_screenshot_button.setStyleSheet("color: black; background-color: white;border: none;")
        self.ui.ecg_screenshot_button.setStyleSheet("color: black; background-color: white;border: none;")
        self.ui.gsr_screenshot_button.setStyleSheet("color: black; background-color: white;border: none;")
        self.ui.pulse_screenshot_button.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(0, 0, 0);border: "
                                                      "none;")

        self.ui.eeg_screenshot_button.setIcon(QIcon("tests/icons/free-icon-screenshot-5370960.png"))
        self.ui.emg_screenshot_button.setIcon(QIcon("tests/icons/free-icon-screenshot-5370960.png"))
        self.ui.ecg_screenshot_button.setIcon(QIcon("tests/icons/free-icon-screenshot-5370960.png"))
        self.ui.gsr_screenshot_button.setIcon(QIcon("tests/icons/free-icon-screenshot-5370960.png"))
        self.ui.pulse_screenshot_button.setIcon(QIcon("tests/icons/free-icon-screenshot-5370960.png"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
