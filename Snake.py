import copy
import random

from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QPaintEvent, QPainter, QKeyEvent, QColor, QBrush
from PyQt6.QtWidgets import QLabel, QErrorMessage


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

        self.__error_message = QErrorMessage()

        self.__brush_black = QBrush(QColor("black"))
        self.__brush_yellow = QBrush(QColor("yellow"))
        self.__brush_red = QBrush(QColor("red"))
        self.__brush_limegreen = QBrush(QColor("limegreen"))

        self.__list_of_rects = list()
        self.__list_of_rects.append(QRect(15 * self.__delta, 15 * self.__delta, self.__delta, self.__delta))

        random.seed("debug")
        #random.seed()
        self.__loot = self.generate_loot()

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

        painter.fillRect(self.__list_of_rects[0], self.__brush_limegreen)

        # paint loot
        painter.setBrush(self.__brush_red)
        painter.drawEllipse(self.__loot)

    def keyReleaseEvent(self, ev: QKeyEvent) -> None:
        super(Snake, self).keyReleaseEvent(ev)

        current_rect = self.__list_of_rects[0]

        if not self.__field.contains(current_rect):
            self.__error_message.showMessage("Out of boundary.")

        if self.__loot.contains(current_rect):
            self.__list_of_rects.append(QRect(current_rect.x(), current_rect.y(), self.__delta, self.__delta))

            self.__loot = self.generate_loot()

        x = current_rect.x()
        y = current_rect.y()

        last_rect = self.__list_of_rects.pop()

        last_rect.setRect(x, y, self.__delta, self.__delta)
        match ev.key():
            case Qt.Key.Key_Left:
                last_rect.translate(- self.__delta, 0)
            case Qt.Key.Key_Right:
                last_rect.translate(self.__delta, 0)
            case Qt.Key.Key_Up:
                last_rect.translate(0, - self.__delta)
            case Qt.Key.Key_Down:
                last_rect.translate(0, self.__delta)

        self.__list_of_rects.insert(0, last_rect)

        self.update()

    def generate_loot(self):
        loot_x = random.randrange(0, self.__number_x) * self.__delta
        loot_y = random.randrange(0, self.__number_y) * self.__delta

        return QRect(loot_x, loot_y, self.__delta, self.__delta)
