import datetime
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QSplitter, QMessageBox, \
    QAction, QMainWindow, QCheckBox
from pyqtgraph import PlotWidget
import numpy as np
from collections import deque
from PyQt5.QtCore import QTimer, Qt

from utils import set_button_style, generate_positive_values


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Графики")
        self.setStyleSheet("background-color: beige;")

        self.graph_button1 = QPushButton("Скрыть график EEG")
        self.graph_button2 = QPushButton("Скрыть график EMG")
        self.graph_button3 = QPushButton("Скрыть график ECG")
        self.graph_button4 = QPushButton("Скрыть график GSR")

        self.screenshot_button1 = QPushButton("Скриншот")
        self.screenshot_button2 = QPushButton("Скриншот")
        self.screenshot_button3 = QPushButton("Скриншот")
        self.screenshot_button4 = QPushButton("Скриншот")

        self.graph_button1.clicked.connect(self.toggle_graph1)
        self.graph_button2.clicked.connect(self.toggle_graph2)
        self.graph_button3.clicked.connect(self.toggle_graph3)
        self.graph_button4.clicked.connect(self.toggle_graph4)

        self.screenshot_button1.clicked.connect(self.save_screenshot1)
        self.screenshot_button2.clicked.connect(self.save_screenshot2)
        self.screenshot_button3.clicked.connect(self.save_screenshot3)
        self.screenshot_button4.clicked.connect(self.save_screenshot4)

        # Устанавливаем стили для кнопок
        set_button_style(self.graph_button1)
        set_button_style(self.graph_button2)
        set_button_style(self.graph_button3)
        set_button_style(self.graph_button4)

        set_button_style(self.screenshot_button1)
        set_button_style(self.screenshot_button2)
        set_button_style(self.screenshot_button3)
        set_button_style(self.screenshot_button4)

        self.plot_widget1 = PlotWidget()
        self.plot_widget2 = PlotWidget()
        self.plot_widget3 = PlotWidget()
        self.plot_widget4 = PlotWidget()

        self.plot_widget1.setBackground('beige')
        self.plot_widget2.setBackground('beige')
        self.plot_widget3.setBackground('beige')
        self.plot_widget4.setBackground('beige')

        button_layout = QVBoxLayout()

        button_layout.addWidget(self.graph_button1)
        button_layout.addWidget(self.screenshot_button1)

        button_layout.addWidget(self.graph_button2)
        button_layout.addWidget(self.screenshot_button2)

        button_layout.addWidget(self.graph_button3)
        button_layout.addWidget(self.screenshot_button3)

        button_layout.addWidget(self.graph_button4)
        button_layout.addWidget(self.screenshot_button4)

        button_container = QWidget()
        button_container.setLayout(button_layout)
        button_container.setStyleSheet("background-color: beige;")

        splitter_layout = QHBoxLayout()
        splitter = QSplitter(Qt.Horizontal)  # Создаем горизонтальный QSplitter
        splitter.addWidget(button_container)  # Добавляем левую часть с кнопками
        splitter.addWidget(self.create_graph_splitter())  # Добавляем правую часть с графиками

        # Устанавливаем фиксированный размер для левой части с кнопками
        splitter.setSizes([200, 600])

        splitter_layout.addWidget(splitter)  # Добавляем QSplitter на основной лейаут

        self.setCentralWidget(QWidget())  # Устанавливаем центральный виджет для QMainWindow
        self.centralWidget().setLayout(splitter_layout)  # Устанавливаем лейаут в центральный виджет

        self.data_queue1 = deque(maxlen=100)  # Хранит данные для графика 1
        self.data_queue2 = deque(maxlen=100)  # Хранит данные для графика 2
        self.data_queue3 = deque(maxlen=100)  # Хранит данные для графика 3
        self.data_queue4 = deque(maxlen=100)  # Хранит данные для графика 4

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.add_random_data)
        self.timer.start(50)  # Вызывать метод add_random_data каждые 500 миллисекунд

        self.plot_data1()
        self.plot_data2()
        self.plot_data3()
        self.plot_data4()

        self.graph1_visible = True
        self.graph2_visible = True
        self.graph3_visible = True
        self.graph4_visible = True

        self.init_menu_bar()

    def create_graph_splitter(self):
        graph_splitter = QSplitter()
        graph_splitter.setOrientation(Qt.Vertical)
        graph_splitter.addWidget(self.plot_widget1)
        graph_splitter.addWidget(self.plot_widget2)
        graph_splitter.addWidget(self.plot_widget3)
        graph_splitter.addWidget(self.plot_widget4)
        return graph_splitter

    def plot_data1(self):
        self.x_data1 = np.arange(100)
        self.y_data1 = np.zeros(100)
        self.plot_curve1 = self.plot_widget1.plot(self.x_data1, self.y_data1,
                                                  pen={'color': 'blue', 'width': 2, 'style': Qt.SolidLine},
                                                  symbol='o', symbolPen='b', symbolBrush='b')  # Изменил цвет на синий

        self.plot_widget1.setLabel('left', 'Значение EEG')
        self.plot_widget1.getPlotItem().showGrid(True, True)

    def plot_data2(self):
        self.x_data2 = np.arange(100)
        self.y_data2 = np.zeros(100)
        self.plot_curve2 = self.plot_widget2.plot(self.x_data2, self.y_data2,
                                                  pen={'color': 'green', 'width': 2, 'style': Qt.SolidLine},
                                                  symbol='o', symbolPen='g', symbolBrush='g')
        self.plot_widget2.setLabel('left', 'Значение EMG')
        self.plot_widget2.getPlotItem().showGrid(True, True)

    def plot_data3(self):
        self.x_data3 = np.arange(100)
        self.y_data3 = np.zeros(100)
        self.plot_curve3 = self.plot_widget3.plot(self.x_data3, self.y_data3,
                                                  pen={'color': 'green', 'width': 2, 'style': Qt.SolidLine},
                                                  symbol='o', symbolPen='g', symbolBrush='g')
        self.plot_widget3.setLabel('left', 'Значение ECG')
        self.plot_widget3.getPlotItem().showGrid(True, True)

    def plot_data4(self):
        self.x_data4 = np.arange(100)
        self.y_data4 = np.zeros(100)
        self.plot_curve4 = self.plot_widget4.plot(self.x_data4, self.y_data4,
                                                  pen={'color': 'green', 'width': 2, 'style': Qt.SolidLine},
                                                  symbol='o', symbolPen='g', symbolBrush='g')
        self.plot_widget4.setLabel('left', 'Значение GSR')
        self.plot_widget4.getPlotItem().showGrid(True, True)

    def toggle_graph1(self):
        self.graph1_visible = not self.graph1_visible
        self.plot_widget1.setVisible(self.graph1_visible)
        if self.graph1_visible:
            self.graph_button1.setText("Скрыть график EEG")
        else:
            self.graph_button1.setText("Показать график EEG")

    def toggle_graph2(self):
        self.graph2_visible = not self.graph2_visible
        self.plot_widget2.setVisible(self.graph2_visible)
        if self.graph2_visible:
            self.graph_button2.setText("Скрыть график EMG")
        else:
            self.graph_button2.setText("Показать график EMG")

    def toggle_graph3(self):
        self.graph3_visible = not self.graph3_visible
        self.plot_widget3.setVisible(self.graph3_visible)
        if self.graph3_visible:
            self.graph_button3.setText("Скрыть график ECG")
        else:
            self.graph_button3.setText("Показать график ECG")

    def toggle_graph4(self):
        self.graph4_visible = not self.graph4_visible
        self.plot_widget4.setVisible(self.graph4_visible)
        if self.graph4_visible:
            self.graph_button4.setText("Скрыть график GSR")
        else:
            self.graph_button4.setText("Показать график GSR")

    def init_menu_bar(self):
        menubar = self.menuBar()

        # Создаем меню "Файл"
        file_menu = menubar.addMenu('Файл')

        # Добавляем пункт "Сохранить"
        save_action = QAction('Сохранить', self)
        save_action.triggered.connect(self.save_screen)
        file_menu.addAction(save_action)

        # Добавляем разделитель
        file_menu.addSeparator()

        # Добавляем пункт "Выход"
        exit_action = QAction('Выход', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Создаем меню "Настройки"
        settings_menu = menubar.addMenu('Настройки')

        # Создаем меню "Помощь"
        help_menu = menubar.addMenu('Помощь')

        # Добавляем элемент управления для графика EEG
        self.checkbox_eeg = QAction('Отображать график EEG', self, checkable=True)
        self.checkbox_eeg.setChecked(True)  # По умолчанию график отображается
        self.checkbox_eeg.triggered.connect(lambda: self.toggle_graph1_from_menu(self.checkbox_eeg.isChecked()))
        settings_menu.addAction(self.checkbox_eeg)

        # Добавляем элемент управления для графика EMG
        self.checkbox_emg = QAction('Отображать график EMG', self, checkable=True)
        self.checkbox_emg.setChecked(True)  # По умолчанию график отображается
        self.checkbox_emg.triggered.connect(lambda: self.toggle_graph2_from_menu(self.checkbox_eeg.isChecked()))
        settings_menu.addAction(self.checkbox_emg)

        # Добавляем элемент управления для графика ECG
        self.checkbox_ecg = QAction('Отображать график ECG', self, checkable=True)
        self.checkbox_ecg.setChecked(True)  # По умолчанию график отображается
        self.checkbox_ecg.triggered.connect(lambda: self.toggle_graph3_from_menu(self.checkbox_eeg.isChecked()))
        settings_menu.addAction(self.checkbox_ecg)

        # Добавляем элемент управления для графика GSR
        self.checkbox_gsr = QAction('Отображать график GSR', self, checkable=True)
        self.checkbox_gsr.setChecked(True)  # По умолчанию график отображается
        self.checkbox_gsr.triggered.connect(lambda: self.toggle_graph4_from_menu(self.checkbox_eeg.isChecked()))
        settings_menu.addAction(self.checkbox_gsr)

    def update_graph_visibility_buttons(self):
        self.graph_button1.setChecked(self.graph1_visible)
        self.graph_button2.setChecked(self.graph2_visible)
        self.graph_button3.setChecked(self.graph3_visible)
        self.graph_button4.setChecked(self.graph4_visible)

    def update_graph_visibility_menu(self):
        self.checkbox_eeg.setChecked(self.graph1_visible)
        self.checkbox_emg.setChecked(self.graph2_visible)
        self.checkbox_ecg.setChecked(self.graph3_visible)
        self.checkbox_gsr.setChecked(self.graph4_visible)

    def toggle_graph1_from_menu(self, checked):
        self.graph1_visible = checked
        self.plot_widget1.setVisible(self.graph1_visible)

    def toggle_graph2_from_menu(self, checked):
        self.graph2_visible = checked
        self.plot_widget2.setVisible(self.graph2_visible)

    def toggle_graph3_from_menu(self, checked):
        self.graph3_visible = checked
        self.plot_widget3.setVisible(self.graph3_visible)

    def toggle_graph4_from_menu(self, checked):
        self.graph4_visible = checked
        self.plot_widget4.setVisible(self.graph4_visible)

    def save_screen(self):
        screenshot = self.centralWidget().grab()
        screenshot.save("screenshot.png", "PNG")

    def save_screenshot1(self):
        self.save_screenshot(self.plot_widget1, f"{datetime.datetime.now()}.png")

    def save_screenshot2(self):
        self.save_screenshot(self.plot_widget2, f"{datetime.datetime.now()}.png")

    def save_screenshot3(self):
        self.save_screenshot(self.plot_widget3, f"{datetime.datetime.now()}.png")

    def save_screenshot4(self):
        self.save_screenshot(self.plot_widget4, f"{datetime.datetime.now()}.png")

    def save_screenshot(self, plot_widget, filename):
        try:
            plot_widget.grab().save(filename, "png")
            QMessageBox.information(self, "Информация", f"Скриншот сохранен как {filename}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить скриншот: {str(e)}")

    def update_graph(self):
        if self.data_queue1 and self.data_queue2 and self.data_queue3 and self.data_queue4:
            data1 = self.data_queue1.popleft()
            data2 = self.data_queue2.popleft()
            data3 = self.data_queue3.popleft()
            data4 = self.data_queue4.popleft()

            eeg = data1.get("eeg", 0)
            emg = data2.get("emg", 0)
            ecg = data3.get("ecg", 0)
            gsr = data4.get("gsr", 0)

            self.y_data1[:-1] = self.y_data1[1:]
            self.y_data1[-1] = eeg
            self.plot_curve1.setData(self.x_data1, self.y_data1)

            self.y_data2[:-1] = self.y_data2[1:]
            self.y_data2[-1] = emg
            self.plot_curve2.setData(self.x_data2, self.y_data2)

            self.y_data3[:-1] = self.y_data3[1:]
            self.y_data3[-1] = ecg
            self.plot_curve3.setData(self.x_data3, self.y_data3)

            self.y_data4[:-1] = self.y_data4[1:]
            self.y_data4[-1] = gsr
            self.plot_curve4.setData(self.x_data4, self.y_data4)

    def add_data(self, data1, data2, data3, data4):
        self.data_queue1.append(data1)
        self.data_queue2.append(data2)
        self.data_queue3.append(data3)
        self.data_queue4.append(data4)

        # Добавляем вызов функции update_graph для обновления графиков сразу после добавления данных
        self.update_graph()

    def add_random_data(self):
        eeg = {
            "eeg": np.random.randint(0, 100),
        }
        emg = {
            "emg": np.random.randint(0, 100),
        }
        ecg = {
            "ecg": np.random.randint(0, 100),
        }
        gsr = {
            "gsr": np.random.randint(0, 100),
        }
        self.add_data(eeg, emg, ecg, gsr)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 800, 600)
    window.show()

    # Пример использования generate_positive_values и add_data
    for _ in range(100):  # Добавляем случайные данные каждые 20 мс в течение 100 итераций
        data1, data2, data3, data4 = generate_positive_values()  # Исправление для получения двух значений
        window.add_data(data1, data2, data3, data4)

    sys.exit(app.exec_())