from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import QTimer, QPoint, Qt
import random

class ParticlesWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.particles = [self.random_particle() for _ in range(50)]
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_particles)
        self.timer.start(50)

    def random_particle(self):
        return {
            "x": random.randint(0, self.width()),
            "y": random.randint(0, self.height()),
            "dx": random.choice([-1, 1]) * random.uniform(0.5, 1.5),
            "dy": random.choice([-1, 1]) * random.uniform(0.5, 1.5),
            "size": random.randint(2, 6),
            "color": QColor(52, 152, 219, 180)
        }

    def update_particles(self):
        for p in self.particles:
            p["x"] += p["dx"]
            p["y"] += p["dy"]
            if p["x"] < 0 or p["x"] > self.width():
                p["dx"] *= -1
            if p["y"] < 0 or p["y"] > self.height():
                p["dy"] *= -1
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        for p in self.particles:
            painter.setBrush(QBrush(p["color"], Qt.SolidPattern))
            painter.drawEllipse(QPoint(int(p["x"]), int(p["y"])), p["size"], p["size"])
