from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPaintEvent, QPainter, QKeyEvent
from PyQt6.QtWidgets import QLabel


class Snake(QLabel):
    def __init__(self, parent=None):
        super(Snake, self).__init__(parent)

        self.__x = 50
        self.__y = 50

        self.activateWindow()
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def paintEvent(self, a0: QPaintEvent) -> None:
        painter = QPainter(self)

        painter.drawText(self.__x, self.__y, "Hallo Welt")

    def keyReleaseEvent(self, ev: QKeyEvent) -> None:
        super(Snake, self).keyReleaseEvent(ev)

        match ev.key():
            case Qt.Key.Key_Left:
                self.__x -= 10
            case Qt.Key.Key_Right:
                self.__x += 10
            case Qt.Key.Key_Up:
                self.__y -= 10
            case Qt.Key.Key_Down:
                self.__y += 10

        self.update()
