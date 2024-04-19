import copy
import random

from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QPaintEvent, QPainter, QKeyEvent, QColor, QBrush, QFont
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

        self.__text_message = None

        self.__brush_black = QBrush(QColor("black"))
        self.__brush_yellow = QBrush(QColor("yellow"))
        self.__brush_red = QBrush(QColor("red"))
        self.__brush_limegreen = QBrush(QColor("limegreen"))

        self.__list_of_rects = list()
        self.__list_of_rects.append(QRect(15 * self.__delta, 15 * self.__delta, self.__delta, self.__delta))

        random.seed("debug")
        # random.seed()
        self.__loot = self.generate_loot()

        self.activateWindow()
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)

        # paint background
        painter.setBrush(self.__brush_black)
        painter.drawRect(self.__field)

        # paint snakes body
        for rect in self.__list_of_rects[1:]:
            painter.drawRect(rect)
            painter.fillRect(rect, self.__brush_yellow)

        # paint snakes head
        painter.drawRect(self.__list_of_rects[0])
        painter.fillRect(self.__list_of_rects[0], self.__brush_limegreen)

        # paint loot
        painter.setBrush(self.__brush_red)
        painter.drawEllipse(self.__loot)

        if self.__text_message:
            painter.setPen(QColor("limegreen"))
            painter.drawText(100, 100, self.__text_message)

    def keyReleaseEvent(self, ev: QKeyEvent) -> None:
        super(Snake, self).keyReleaseEvent(ev)

        next_rect = copy.deepcopy(self.__list_of_rects[0])

        match ev.key():
            case Qt.Key.Key_Left:
                next_rect.translate(- self.__delta, 0)
            case Qt.Key.Key_Right:
                next_rect.translate(self.__delta, 0)
            case Qt.Key.Key_Up:
                next_rect.translate(0, - self.__delta)
            case Qt.Key.Key_Down:
                next_rect.translate(0, self.__delta)

        if not self.__field.contains(next_rect):
            self.__text_message = "Out of boundary."

        for rect in self.__list_of_rects:
            if rect.contains(next_rect):
                self.__text_message = "Sneak bits itself."

        if self.__loot.contains(next_rect):
            self.__loot = self.generate_loot()
        else:
            self.__list_of_rects.pop()

        self.__list_of_rects.insert(0, next_rect)

        self.update()

    def generate_loot(self):
        loot_x = random.randrange(0, self.__number_x) * self.__delta
        loot_y = random.randrange(0, self.__number_y) * self.__delta

        return QRect(loot_x, loot_y, self.__delta, self.__delta)
