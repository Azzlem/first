import pyqtgraph as pg
from PyQt6 import QtCore
from PyQt6.QtCore import QSize

styles = {"color": "black", "font-size": "18px"}


def make_plot_eeg(self):
    self.eeg_widget = pg.PlotWidget()
    self.eeg_widget.setFixedSize(QtCore.QSize(1400, 200))
    # self.plot_widget.setAspectLocked()
    self.eeg_widget.setBackground("w")
    self.eeg_widget.setYRange(0, 10)
    self.eeg_widget.setTitle("EEG", color="b", size="20pt")
    self.eeg_widget.setLabel("left", "EEG ", **styles)
    self.eeg_widget.setLabel("bottom", "Time", **styles)
    self.eeg_widget.addLegend()
    self.eeg_widget.showGrid(x=True, y=True)
    self.plot_widgets.append(self.eeg_widget)
    self.verticalLayout_10.addWidget(self.eeg_widget)
    return self.eeg_widget


def make_plot_emg(self):
    self.emg_widget = pg.PlotWidget()
    self.emg_widget.setFixedSize(QtCore.QSize(1400, 200))
    self.emg_widget.setBackground("y")
    self.emg_widget.setTitle("EMG", color="g", size="20pt")
    self.emg_widget.setLabel("left", "EMG", **styles)
    self.emg_widget.setLabel("bottom", "Time", **styles)
    self.emg_widget.addLegend()
    self.emg_widget.showGrid(x=True, y=True)
    # self.emg_widget.setYRange(20, 40)
    self.plot_widgets.append(self.emg_widget)
    self.verticalLayout_9.addWidget(self.emg_widget)
    return self.emg_widget


def make_plot_ecg(self):
    self.ecg_widget = pg.PlotWidget()
    self.ecg_widget.setFixedSize(QtCore.QSize(1400, 200))
    self.ecg_widget.setBackground("b")
    self.ecg_widget.setTitle("ECG", color="w", size="20pt")
    self.ecg_widget.setLabel("left", "ECG", **styles)
    self.ecg_widget.setLabel("bottom", "Time", **styles)
    self.ecg_widget.addLegend()
    self.ecg_widget.showGrid(x=True, y=True)
    # self.ecg_widget.setYRange(20, 40)
    self.plot_widgets.append(self.ecg_widget)
    self.verticalLayout_8.addWidget(self.ecg_widget, stretch=1)
    return self.ecg_widget


def make_plot_gsr(self):
    self.gsr_widget = pg.PlotWidget()
    self.gsr_widget.setFixedSize(QtCore.QSize(1400, 200))
    self.gsr_widget.setBackground("r")
    self.gsr_widget.setTitle("GSR", color="b", size="20pt")
    self.gsr_widget.setLabel("left", "GSR", **styles)
    self.gsr_widget.setLabel("bottom", "Time", **styles)
    self.gsr_widget.addLegend()
    self.gsr_widget.showGrid(x=True, y=True)
    # self.gsr_widget.setYRange(20, 40)
    self.plot_widgets.append(self.gsr_widget)
    self.verticalLayout_7.addWidget(self.gsr_widget)
    return self.gsr_widget
