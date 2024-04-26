import sys
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton, QCheckBox
from PyQt6 import QtWidgets
from plots import make_plot_temp, make_plot_power, make_plot_water, make_plot_soul


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Установка имени приложения
        self.setWindowTitle("My App")

        # Объявление центрального виджета
        self.widget_main = QtWidgets.QWidget(self)
        self.widget_main.setStyleSheet("background-color: rgb(0, 0, 0);")

        # Объявление кнопок
        self.button1 = QPushButton()
        self.button1.setIcon(QIcon("icons/free-icon-screenshot-5370960.png"))
        self.button1.setIconSize(QSize(38, 38))

        self.button2 = QPushButton()
        self.button2.setIcon(QIcon("icons/free-icon-screenshot-5370960.png"))
        self.button2.setIconSize(QSize(38, 38))

        self.button3 = QPushButton()
        self.button3.setIcon(QIcon("icons/free-icon-screenshot-5370960.png"))
        self.button3.setIconSize(QSize(38, 38))

        self.button4 = QPushButton()
        self.button4.setIcon(QIcon("icons/free-icon-screenshot-5370960.png"))
        self.button4.setIconSize(QSize(38, 38))

        self.button5 = QCheckBox("Температура!")
        self.button6 = QCheckBox("Вода!")
        self.button7 = QCheckBox("Сила!")
        self.button8 = QCheckBox("Дух!")
        self.button9 = QPushButton("Press Me9!")
        self.button10 = QPushButton("Press Me10!")

        # Создание макетов
        self.layout = QtWidgets.QHBoxLayout()
        self.layout_left = QtWidgets.QVBoxLayout()
        self.layout_right = QtWidgets.QVBoxLayout()
        self.layout_left_up = QtWidgets.QVBoxLayout()
        self.layout_left_down = QtWidgets.QHBoxLayout()
        self.layout_right_up = QtWidgets.QHBoxLayout()
        self.layout_right_down = QtWidgets.QVBoxLayout()

        # Добавление макетов в макеты
        self.layout.addLayout(self.layout_left)
        self.layout.addLayout(self.layout_right)
        self.layout_left.addLayout(self.layout_left_up)
        self.layout_left.addLayout(self.layout_left_down)
        self.layout_right.addLayout(self.layout_right_up)
        self.layout_right.addLayout(self.layout_right_down)

        # Добавление виджетов в макеты
        self.layout_right_up.addWidget(self.button5)
        self.layout_right_up.addWidget(self.button1)
        self.layout_right_up.addWidget(self.button6)
        self.layout_right_up.addWidget(self.button2)
        self.layout_right_up.addWidget(self.button7)
        self.layout_right_up.addWidget(self.button3)
        self.layout_right_up.addWidget(self.button8)
        self.layout_right_up.addWidget(self.button4)
        self.layout_left_up.addWidget(self.button9)
        self.layout_left_down.addWidget(self.button10)

        # Не удалять важно
        self.plot_widgets = []

        # создание графиков
        self.plot_widget_temp = make_plot_temp(self)
        self.plot_widget_power = make_plot_power(self)
        self.plot_widget_water = make_plot_water(self)
        self.plot_widget_soul = make_plot_soul(self)

        # Добавление центрального макета в центральный Виджет
        self.widget_main.setLayout(self.layout)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(self.widget_main)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.showMaximized()
    sys.exit(app.exec())
