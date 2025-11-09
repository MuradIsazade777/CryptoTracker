from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpinBox, QPushButton
from core.password_manager import PasswordManager

class PasswordTab(QWidget):
    def __init__(self):
        super().__init__()
        self.manager = PasswordManager()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.length_input = QSpinBox()
        self.length_input.setRange(6, 64)
        self.length_input.setValue(12)

        self.generate_button = QPushButton("Generate Password")
        self.result_label = QLabel("Generated password will appear here.")

        self.generate_button.clicked.connect(self.generate_password)

        layout.addWidget(QLabel("Select password length:"))
        layout.addWidget(self.length_input)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def generate_password(self):
        length = self.length_input.value()
        password = self.manager.generate_password(length)
        self.result_label.setText(password)
