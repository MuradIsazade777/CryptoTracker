from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
from core.crypto_engine import CryptoEngine

class EncryptTab(QWidget):
    def __init__(self):
        super().__init__()
        self.engine = CryptoEngine()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.input_text = QTextEdit()
        self.encrypt_button = QPushButton("Encrypt")
        self.result_label = QLabel("Encrypted text will appear here.")

        self.encrypt_button.clicked.connect(self.encrypt_text)

        layout.addWidget(QLabel("Enter text to encrypt:"))
        layout.addWidget(self.input_text)
        layout.addWidget(self.encrypt_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def encrypt_text(self):
        text = self.input_text.toPlainText()
        encrypted = self.engine.encrypt_text(text)
        self.result_label.setText(encrypted)
