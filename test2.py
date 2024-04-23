import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QSplitter, QMessageBox, \
    QSizePolicy, QAction, QMainWindow, QMenu
from pyqtgraph import PlotWidget
import numpy as np
from collections import deque
from PyQt5.QtCore import QTimer, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Графики")

        self.graph_button1 = QPushButton("Скрыть график Пульса")
        self.graph_button2 = QPushButton("Скрыть график Давления")
        self.graph_button3 = QPushButton("Скрыть график Чего-то")

        self.screenshot_button1 = QPushButton("Скриншот 1")
        self.screenshot_button2 = QPushButton("Скриншот 2")
        self.screenshot_button3 = QPushButton("Скриншот 3")

        self.graph_button1.clicked.connect(self.toggle_graph1)
        self.graph_button2.clicked.connect(self.toggle_graph2)
        self.graph_button3.clicked.connect(self.toggle_graph3)

        self.screenshot_button1.clicked.connect(self.save_screenshot1)
        self.screenshot_button2.clicked.connect(self.save_screenshot2)
        self.screenshot_button3.clicked.connect(self.save_screenshot3)

        # Устанавливаем стили для кнопок
        self.set_button_style(self.graph_button1)
        self.set_button_style(self.graph_button2)
        self.set_button_style(self.graph_button3)

        self.set_button_style(self.screenshot_button1)
        self.set_button_style(self.screenshot_button2)
        self.set_button_style(self.screenshot_button3)

        self.plot_widget1 = PlotWidget()
        self.plot_widget2 = PlotWidget()
        self.plot_widget3 = PlotWidget()

        button_layout = QVBoxLayout()

        button_layout.addWidget(self.graph_button1)
        button_layout.addWidget(self.screenshot_button1)

        button_layout.addWidget(self.graph_button2)
        button_layout.addWidget(self.screenshot_button2)

        button_layout.addWidget(self.graph_button3)
        button_layout.addWidget(self.screenshot_button3)

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
        self.data_queue3 = deque(maxlen=100)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.add_random_data)
        self.timer.start(50)  # Вызывать метод add_random_data каждые 500 миллисекунд

        self.plot_data1()
        self.plot_data2()
        self.plot_data3()

        self.graph1_visible = True
        self.graph2_visible = True
        self.graph3_visible = True

        self.init_menu_bar()  # Инициализация менюбара

    def create_graph_splitter(self):
        graph_splitter = QSplitter()
        graph_splitter.setOrientation(Qt.Vertical)
        graph_splitter.addWidget(self.plot_widget1)
        graph_splitter.addWidget(self.plot_widget2)
        graph_splitter.addWidget(self.plot_widget3)
        return graph_splitter

    def plot_data1(self):
        self.x_data1 = np.arange(100)
        self.y_data1 = np.zeros(100)
        self.plot_widget1.plot(self.x_data1, self.y_data1, pen={'color': 'green', 'width': 2, 'style': Qt.SolidLine},
                               symbol='o', symbolPen='g', symbolBrush='g')
        self.plot_widget1.setLabel('left', 'Значение')
        self.plot_widget1.setLabel('bottom', 'Время')
        self.plot_widget1.getPlotItem().showGrid(True, True)

    def plot_data2(self):
        self.x_data2 = np.arange(100)
        self.y_data2 = np.zeros(100)
        self.plot_widget2.plot(self.x_data2, self.y_data2, pen={'color': 'green', 'width': 2, 'style': Qt.SolidLine},
                               symbol='o', symbolPen='g', symbolBrush='g')
        self.plot_widget2.setLabel('left', 'Значение')
        self.plot_widget2.setLabel('bottom', 'Время')
        self.plot_widget2.getPlotItem().showGrid(True, True)

    def plot_data3(self):
        self.x_data3 = np.arange(100)
        self.y_data3 = np.zeros(100)
        self.plot_widget3.plot(self.x_data3, self.y_data3, pen={'color': 'green', 'width': 2, 'style': Qt.SolidLine},
                               symbol='o', symbolPen='g', symbolBrush='g')
        self.plot_widget3.setLabel('left', 'Значение')
        self.plot_widget3.setLabel('bottom', 'Время')
        self.plot_widget3.getPlotItem().showGrid(True, True)

    def toggle_graph1(self):
        self.graph1_visible = not self.graph1_visible
        self.plot_widget1.setVisible(self.graph1_visible)
        if self.graph1_visible:
            self.graph_button1.setText("Скрыть график Пульса")
        else:
            self.graph_button1.setText("Показать график Пульса")

    def toggle_graph2(self):
        self.graph2_visible = not self.graph2_visible
        self.plot_widget2.setVisible(self.graph2_visible)
        if self.graph2_visible:
            self.graph_button2.setText("Скрыть график давления")
        else:
            self.graph_button2.setText("Показать график давления")

    def toggle_graph3(self):
        self.graph3_visible = not self.graph3_visible
        self.plot_widget3.setVisible(self.graph3_visible)
        if self.graph3_visible:
            self.graph_button3.setText("Скрыть график давления")
        else:
            self.graph_button3.setText("Показать график давления")

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

    def save_screen(self):
        screenshot = self.centralWidget().grab()
        screenshot.save("screenshot.png", "PNG")

    def save_screenshot1(self):
        self.save_screenshot(self.plot_widget1, "screenshot1.png")

    def save_screenshot2(self):
        self.save_screenshot(self.plot_widget2, "screenshot2.png")

    def save_screenshot3(self):
        self.save_screenshot(self.plot_widget3, "screenshot3.png")

    def save_screenshot(self, plot_widget, filename):
        try:
            plot_widget.grab().save(filename, "png")
            QMessageBox.information(self, "Информация", f"Скриншот сохранен как {filename}")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить скриншот: {str(e)}")

    def update_graph(self):
        if self.data_queue1 and self.data_queue2:
            data1 = self.data_queue1.popleft()
            data2 = self.data_queue2.popleft()
            data3 = self.data_queue3.popleft()

            puls = data1.get("puls", 0)
            ons = data2.get("ons", 0)
            ils = data3.get("ils", 0)

            self.y_data1[:-1] = self.y_data1[1:]
            self.y_data1[-1] = puls

            self.y_data2[:-1] = self.y_data2[1:]
            self.y_data2[-1] = ons

            self.y_data3[:-1] = self.y_data3[1:]
            self.y_data3[-1] = ils

            self.plot_widget1.clear()
            self.plot_widget2.clear()
            self.plot_widget3.clear()

            if self.graph1_visible:
                self.plot_widget1.plot(self.x_data1, self.y_data1,
                                       pen={'color': 'r', 'width': 2, 'style': Qt.SolidLine, 'cosmetic': True})

            if self.graph2_visible:
                self.plot_widget2.plot(self.x_data2, self.y_data2,
                                       pen={'color': 'g', 'width': 2, 'style': Qt.SolidLine, 'cosmetic': True})

            if self.graph3_visible:
                self.plot_widget3.plot(self.x_data3, self.y_data3,
                                       pen={'color': 'g', 'width': 2, 'style': Qt.SolidLine, 'cosmetic': True})

    def add_data(self, data1, data2, data3):
        print("Added data1:", data1)  # Проверка для отладки
        print("Added data2:", data2)  # Проверка для отладки
        print("Added data2:", data3)  # Проверка для отладки

        self.data_queue1.append(data1)
        self.data_queue2.append(data2)
        self.data_queue3.append(data3)
        self.update_graph()  # Добавляем вызов функции update_graph для обновления графиков сразу после добавления данных

    def add_random_data(self):
        data1 = {
            "puls": np.random.randint(0, 100),
            "ons": np.random.randint(0, 100)
        }
        data2 = {
            "puls": np.random.randint(0, 100),
            "ons": np.random.randint(0, 100)
        }
        data3 = {
            "puls": np.random.randint(0, 100),
            "ils": np.random.randint(0, 100)
        }
        self.add_data(data1, data2, data3)

    def generate_positive_values(self):
        data1 = {
            "puls": np.random.randint(0, 100),
            "ons": np.random.randint(0, 100),
            "ils": np.random.randint(0, 100)
        }
        print("Generated data1:", data1)  # Проверка для отладки

        data2 = {
            "puls": np.random.randint(0, 100),
            "ons": np.random.randint(0, 100),
            "ils": np.random.randint(0, 100)
        }
        print("Generated data2:", data2)  # Проверка для отладки

        data3 = {
            "puls": np.random.randint(0, 100),
            "ons": np.random.randint(0, 100),
            "ils": np.random.randint(0, 100)
        }
        print("Generated data3:", data3)  # Проверка для отладки

        return data1, data2, data3

    def set_button_style(self, button):
        button.setStyleSheet("""
            QPushButton {
                border-radius: 5px;
                background-color: #f0f0f0;
                border: 2px solid #8f8f91;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #d0d0d0;
            }
            QPushButton:pressed {
                background-color: #a0a0a0;
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 800, 600)
    window.show()

    # Пример использования generate_positive_values и add_data
    for _ in range(100):  # Добавляем случайные данные каждые 20 мс в течение 100 итераций
        data1, data2, data3 = window.generate_positive_values()  # Исправление для получения двух значений
        window.add_data(data1, data2, data3)

    sys.exit(app.exec_())
