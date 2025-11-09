from PyQt5.QtGui import QPalette, QColor

class ThemeManager:
    def apply_dark_mode(app):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#1e1e2f"))
        palette.setColor(QPalette.WindowText, QColor("#ecf0f1"))
        palette.setColor(QPalette.Base, QColor("#2c3e50"))
        palette.setColor(QPalette.Text, QColor("#ecf0f1"))
        palette.setColor(QPalette.Button, QColor("#3498db"))
        palette.setColor(QPalette.ButtonText, QColor("#ffffff"))
        app.setPalette(palette)

    def apply_light_mode(app):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#ffffff"))
        palette.setColor(QPalette.WindowText, QColor("#000000"))
        palette.setColor(QPalette.Base, QColor("#f0f0f0"))
        palette.setColor(QPalette.Text, QColor("#000000"))
        palette.setColor(QPalette.Button, QColor("#3498db"))
        palette.setColor(QPalette.ButtonText, QColor("#ffffff"))
        app.setPalette(palette)
