import pyqtgraph as pg

pen = pg.mkPen(color=(0, 0, 0))


def toggle_plot_visibility(plot_widget):
    if plot_widget.isVisible():
        plot_widget.hide()
    else:
        plot_widget.show()


def clicked_button(button, widget):
    button.clicked.connect(lambda: toggle_plot_visibility(widget))


def time_biggest_max_point(self, max_points):
    for times, temperatures in [
        (self.ui.times_eeg, self.ui.temperatures_1),
        (self.ui.times_emg, self.ui.temperatures_2),
        (self.ui.times_ecg, self.ui.temperatures_3),
        (self.ui.times_gst, self.ui.temperatures_4)
    ]:
        if len(times) > max_points:
            times[:] = times[-max_points:]
            temperatures[:] = temperatures[-max_points:]


def update_sensor_data(sens_name, sens_to_send, times_list, temperatures_list, plot_widget, line):
    times_list.append(times_list[-1] + 1 if times_list else 1)
    temperatures_list.append(int(sens_to_send))

    if not line:
        line = plot_widget.plot(
            times_list,
            temperatures_list,
            name=f"{sens_name}",
            pen=pen,
            symbol="o",
            symbolSize=5,
            symbolBrush="b",
            connect='all',
        )
        plot_widget.setYRange(0, 10)
        plot_widget.setXRange(0, 100)
    else:
        line.setData(times_list, temperatures_list)




