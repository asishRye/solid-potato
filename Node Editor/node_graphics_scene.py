from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import math


class QDMGraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Settings
        self.gridSize = 20

        self._color_background = QColor("#393939")
        self._color_light = QColor("#2f2f2f")

        self.scene_width, self.scene_height = 64000, 64000

        self._pen_light = QPen(self._color_light)
        self._pen_light.setWidth(1)

        self.setBackgroundBrush(self._color_background)
        self.setSceneRect(-self.scene_width//2, -self.scene_height//2,
                          self.scene_width, self.scene_height)

    def drawBackground(self, painter, rect):
        super().drawBackground(painter, rect)

        left = int(math.floor(rect.left()))
        right = int(math.ceil(rect.right()))
        top = int(math.floor(rect.top()))
        bottom = int(math.ceil(rect.bottom()))

        first_left = left - (left % self.gridSize)
        first_top = top - (top % self.gridSize)

        lines_light = []
        for x in range(first_left, right, self.gridSize):
            lines_light.append(QLine(x, top, x, bottom))

        for y in range(first_top, bottom, self.gridSize):
            lines_light.append(QLine(left, y, right, y))

        # lines_light.append(QLine(0, 0, 100, 100))

        painter.setPen(self._pen_light)
        painter.drawLines(*lines_light)
