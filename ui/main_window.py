import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QTabWidget, QPushButton
)
from PyQt5.QtCore import QFile
from PyQt5.QtGui import QPalette, QColor

from ui.encrypt_tab import EncryptTab
from ui.decrypt_tab import DecryptTab
from ui.password_tab import PasswordTab
from ui.wallet_tab import WalletTab
from ui.particles_widget import ParticlesWidget
from ui.theme_manager import ThemeManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CryptoTracker 🔐")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()
        self.apply_stylesheet()

    def init_ui(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Particles background
        self.particles = ParticlesWidget()
        self.particles.setFixedHeight(150)
        layout.addWidget(self.particles)

        # Tabs
        self.tabs = QTabWidget()
        self.tabs.addTab(EncryptTab(), "Encrypt")
        self.tabs.addTab(DecryptTab(), "Decrypt")
        self.tabs.addTab(PasswordTab(), "Password")
        self.tabs.addTab(WalletTab(), "Wallet")
        layout.addWidget(self.tabs)

        # Theme toggle button
        self.toggle_button = QPushButton("Toggle Dark/Light Mode")
        self.toggle_button.clicked.connect(self.toggle_theme)
        layout.addWidget(self.toggle_button)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def apply_stylesheet(self):
        style_path = os.path.join("style", "style.qss")
        if os.path.exists(style_path):
            file = QFile(style_path)
            file.open(QFile.ReadOnly | QFile.Text)
            style = str(file.readAll(), encoding="utf-8")
            self.setStyleSheet(style)

    def toggle_theme(self):
        current_bg = self.palette().color(QPalette.Window).name()
        if current_bg == "#1e1e2f":
            ThemeManager.apply_light_mode(QApplication.instance())
        else:
            ThemeManager.apply_dark_mode(QApplication.instance())

def run_app():
    app = QApplication([])
    ThemeManager.apply_dark_mode(app)  # Default theme
    window = MainWindow()
    window.show()
    app.exec_()
