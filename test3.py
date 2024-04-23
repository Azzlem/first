from PyQt5.QtCore import QObject, pyqtSignal
import serial
import json
import threading


class SerialReader(QObject):
    data_received = pyqtSignal(dict)

    def __init__(self, port, baudrate):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.serial = None

    def start_reading(self):
        self.serial = serial.Serial(self.port, baudrate=self.baudrate)
        thread = threading.Thread(target=self._read_data)
        thread.start()

    def _read_data(self):
        while self.serial and self.serial.is_open:
            line = self.serial.readline().decode().strip()
            if line:
                try:
                    data = json.loads(line)
                    self.data_received.emit(data)
                except ValueError as e:
                    print("JSON parse error:", e)

    def stop_reading(self):
        if self.serial and self.serial.is_open:
            self.serial.close()
