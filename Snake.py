import random

from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QPaintEvent, QPainter, QKeyEvent, QColor, QBrush
from PyQt6.QtWidgets import QLabel


class Snake(QLabel):
    def __init__(self, parent=None):
        super(Snake, self).__init__(parent)

        self.__delta = 10
        self.__number_x = 30
        self.__number_y = 25

        self.__w = self.__number_x * self.__delta
        self.__h = self.__number_y * self.__delta
        self.__field = QRect(0, 0, self.__w, self.__h)

        self.setFixedSize(self.__field.size())

        self.__brush_black = QBrush(QColor("black"))
        self.__brush_yellow = QBrush(QColor("yellow"))
        self.__brush_red = QBrush(QColor("red"))

        self.__list_of_rects = list()
        self.__list_of_rects.append(QRect(15 * self.__delta, 15 * self.__delta, self.__delta, self.__delta))

        random.seed("debug")
        #random.seed()
        self.__loot_x = random.randrange(0, self.__number_x) * self.__delta
        self.__loot_y = random.randrange(0, self.__number_y) * self.__delta

        self.activateWindow()
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)

        # paint background
        painter.setBrush(self.__brush_black)
        painter.drawRect(self.__field)

        # paint snake
        for rect in self.__list_of_rects:
            painter.drawRect(rect)
            painter.fillRect(rect, self.__brush_yellow)

        # paint loot
        painter.setBrush(self.__brush_red)
        painter.drawEllipse(self.__loot_x, self.__loot_y, self.__delta, self.__delta)

    def keyReleaseEvent(self, ev: QKeyEvent) -> None:
        super(Snake, self).keyReleaseEvent(ev)

        match ev.key():
            case Qt.Key.Key_Left:
                for rect in self.__list_of_rects:
                    rect.translate(- self.__delta, 0)
            case Qt.Key.Key_Right:
                for rect in self.__list_of_rects:
                    rect.translate(self.__delta, 0)
            case Qt.Key.Key_Up:
                for rect in self.__list_of_rects:
                    rect.translate(0, - self.__delta)
            case Qt.Key.Key_Down:
                for rect in self.__list_of_rects:
                    rect.translate(0, self.__delta)

        self.update()
