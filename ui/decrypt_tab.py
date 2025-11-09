from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
from core.crypto_engine import CryptoEngine

class DecryptTab(QWidget):
    def __init__(self):
        super().__init__()
        self.engine = CryptoEngine()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.input_text = QTextEdit()
        self.decrypt_button = QPushButton("Decrypt")
        self.result_label = QLabel("Decrypted text will appear here.")

        self.decrypt_button.clicked.connect(self.decrypt_text)

        layout.addWidget(QLabel("Enter encrypted text:"))
        layout.addWidget(self.input_text)
        layout.addWidget(self.decrypt_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def decrypt_text(self):
        encrypted = self.input_text.toPlainText()
        decrypted = self.engine.decrypt_text(encrypted)
        self.result_label.setText(decrypted)
