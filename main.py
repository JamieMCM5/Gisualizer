import sys
from PyQt6.QtWidgets import *
from Gisualizer import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gisualizer = MainWindow()
    gisualizer.show()
    sys.exit(app.exec())