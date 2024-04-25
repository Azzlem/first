import pyqtgraph as pg

styles = {"color": "black", "font-size": "18px"}


def make_plot_temp(self):
    self.plot_widget_temp = pg.PlotWidget()
    self.plot_widget_temp.setBackground("w")
    self.plot_widget_temp.setTitle("Temperature", color="b", size="20pt")

    self.plot_widget_temp.setLabel("left", "Temperature (°C)", **styles)
    self.plot_widget_temp.setLabel("bottom", "Time (sec)", **styles)
    self.plot_widget_temp.addLegend()
    self.plot_widget_temp.showGrid(x=True, y=True)
    self.plot_widget_temp.setYRange(20, 40)
    self.plot_widget_temp.setFixedSize(1200, 200)  # Set fixed size
    self.plot_widgets.append(self.plot_widget_temp)
    self.layout.addWidget(self.plot_widget_temp)
    return self.plot_widget_temp


def make_plot_water(self):
    self.plot_widget_water = pg.PlotWidget()
    self.plot_widget_water.setBackground("y")
    self.plot_widget_water.setTitle("Water", color="g", size="20pt")
    self.plot_widget_water.setLabel("left", "Water (L)", **styles)
    self.plot_widget_water.setLabel("bottom", "Time (sec)", **styles)
    self.plot_widget_water.addLegend()
    self.plot_widget_water.showGrid(x=True, y=True)
    self.plot_widget_water.setYRange(20, 40)
    self.plot_widget_water.setFixedSize(1200, 200)  # Set fixed size
    self.plot_widgets.append(self.plot_widget_water)
    self.layout.addWidget(self.plot_widget_water)
    return self.plot_widget_water


def make_plot_power(self):
    self.plot_widget_power = pg.PlotWidget()
    self.plot_widget_power.setBackground("b")
    self.plot_widget_power.setTitle("Power", color="w", size="20pt")
    self.plot_widget_power.setLabel("left", "Power (H)", **styles)
    self.plot_widget_power.setLabel("bottom", "Time (sec)", **styles)
    self.plot_widget_power.addLegend()
    self.plot_widget_power.showGrid(x=True, y=True)
    self.plot_widget_power.setYRange(20, 40)
    self.plot_widget_power.setFixedSize(1200, 200)  # Set fixed size
    self.plot_widgets.append(self.plot_widget_power)
    self.layout.addWidget(self.plot_widget_power)
    return self.plot_widget_power


def make_plot_soul(self):
    self.plot_widget_soul = pg.PlotWidget()
    self.plot_widget_soul.setBackground("r")
    self.plot_widget_soul.setTitle("Soul", color="b", size="20pt")
    self.plot_widget_soul.setLabel("left", "Soul (шт)", **styles)
    self.plot_widget_soul.setLabel("bottom", "Time (sec)", **styles)
    self.plot_widget_soul.addLegend()
    self.plot_widget_soul.showGrid(x=True, y=True)
    self.plot_widget_soul.setYRange(20, 40)
    self.plot_widget_soul.setFixedSize(1200, 200)  # Set fixed size
    self.plot_widgets.append(self.plot_widget_soul)
    self.layout.addWidget(self.plot_widget_soul)
    return self.plot_widget_soul
