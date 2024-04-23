import numpy as np


def set_button_style(button):
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


def generate_positive_values():
    data1 = {
        "eeg": np.random.randint(0, 100),
        "emg": np.random.randint(0, 100),
        "ecg": np.random.randint(0, 100),
        "gsr": np.random.randint(0, 100),
    }
    # print("Generated data1:", data1)  # Проверка для отладки

    data2 = {
        "eeg": np.random.randint(0, 100),
        "emg": np.random.randint(0, 100),
        "ecg": np.random.randint(0, 100),
        "gsr": np.random.randint(0, 100),
    }
    # print("Generated data2:", data2)  # Проверка для отладки

    data3 = {
        "eeg": np.random.randint(0, 100),
        "emg": np.random.randint(0, 100),
        "ecg": np.random.randint(0, 100),
        "gsr": np.random.randint(0, 100),
    }

    data4 = {
        "eeg": np.random.randint(0, 100),
        "emg": np.random.randint(0, 100),
        "ecg": np.random.randint(0, 100),
        "gsr": np.random.randint(0, 100),
    }
    # print("Generated data3:", data3)  # Проверка для отладки

    return data1, data2, data3, data4

