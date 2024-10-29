from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
import sys


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        
        #Window setup
        self.setWindowTitle("Gisualizer")
        
        self.setMaximumSize(1000, 800)
        self.setMinimumSize(600, 400)

        #Button
        button = QPushButton("Press me")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self):
        print("clicked")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()