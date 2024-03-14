from PyQt6.QtCore import Qt, QRect
from PyQt6.QtGui import QPaintEvent, QPainter, QKeyEvent
from PyQt6.QtWidgets import QLabel


class Snake(QLabel):
    def __init__(self, parent=None):
        super(Snake, self).__init__(parent)

        self.__delta = 10
        self.setFixedSize(30 * self.__delta, 30 * self.__delta)

        self.__list_of_rects = list()
        self.__list_of_rects.append(QRect(15 * self.__delta, 15 * self.__delta, self.__delta, self.__delta))

        self.activateWindow()
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)

        painter.drawRects(self.__list_of_rects)

        # Zeichen Sie einen roten Kreis, welche unsere Schlange später isst.

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
