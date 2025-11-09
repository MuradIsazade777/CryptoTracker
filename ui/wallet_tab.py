from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from core.wallet_store import WalletStore

class WalletTab(QWidget):
    def __init__(self):
        super().__init__()
        self.store = WalletStore()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.key_input = QLineEdit()
        self.save_button = QPushButton("Save Wallet")
        self.result_label = QLabel("Status will appear here.")

        self.save_button.clicked.connect(self.save_wallet)

        layout.addWidget(QLabel("Wallet name:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Private key:"))
        layout.addWidget(self.key_input)
        layout.addWidget(self.save_button)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def save_wallet(self):
        name = self.name_input.text()
        key = self.key_input.text()
        self.store.save_wallet(name, key)
        self.result_label.setText("Wallet saved securely.")
