from PyQt5 import Qt, QtCore
import pyqtgraph as pg


from base import read_csv_my1


class Window(Qt.QWidget):

    def __init__(self):
        super(Window, self).__init__()


        self.index = None
        layout = Qt.QVBoxLayout(self)

        self.view = view = pg.PlotWidget()
        self.curve = view.plot(name="Line")

        self.btn = Qt.QPushButton("тыкни сюда")
        self.btn.clicked.connect(self.start_animation)

        layout.addWidget(Qt.QLabel("Some text"))
        layout.addWidget(self.view)
        layout.addWidget(self.btn)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_plot)
        self.points = []

    def start_animation(self):
        my_array = read_csv_my1()
        self.points = [float(i[1].replace(",", ".")) for i in my_array.values]
        self.index = 0
        self.timer.start(100)  # milliseconds

    def update_plot(self):
        if self.index < len(self.points):

            x = list(range(self.index + 1))
            y = self.points[:self.index + 1]
            self.curve.setData(x, y)
            self.index += 1
        else:
            self.timer.stop()


if __name__ == "__main__":
    app = Qt.QApplication([])
    w = Window()
    w.show()
    app.exec()
