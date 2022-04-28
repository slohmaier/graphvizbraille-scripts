import sys
from PySide6.QtWidgets import QMainWindow, QGridLayout, QLabel, QApplication, QWidget

class TactileSchematics(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        widget = QWidget()
        self._grid = QGridLayout(widget)
        self.setCentralWidget(widget)
        self._grid.addWidget(QLabel('HELLO'), 0, 0)

if __name__ == '__main__':
    app = QApplication([])
    window = TactileSchematics()
    window.show()
    sys.exit(app.exec())
