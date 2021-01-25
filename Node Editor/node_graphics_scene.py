from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class QDMGraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Settings
        self._color_background = QColor("#393939")
        self.scene_width, self.scene_height = 64000, 64000

        self.setBackgroundBrush(self._color_background)
        self.setSceneRect(-self.scene_width//2, -self.scene_height//2,
                          self.scene_width, self.scene_height)
