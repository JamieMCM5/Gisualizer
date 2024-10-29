from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import numpy as np
import matplotlib.pyplot as plt

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = "Gisualizer"
        self.left = 50
        self.right = 50
        self.height = 600
        self.width = 500

        self.createUI()

    def createUI(self):
        self.setGeometry(self.left, self.right, self.width, self.height)
        self.setWindowTitle(self.title)
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.addItems()

    def addItems(self):
        self.instructionsLabel = QLabel(
            "Instructions:\n"
            "- Use 'x' as the variable.\n"
            "- To square: use 'x**2'\n"
            "- To take the square root: use 'np.sqrt(x)'\n"
            "- For trigonometric functions: use 'np.sin(x)', 'np.cos(x)', etc.\n"
            "- For exponential: use 'np.exp(x)'\n"
            "- Example: '2*x**2 + np.sin(x)'"
        )
        self.grid.addWidget(self.instructionsLabel)

        self.userText = QLineEdit()
        self.userText.setPlaceholderText("Enter your function here (e.g., np.sin(x))")
        self.grid.addWidget(self.userText)

        self.plotButton = QPushButton("Plot Function")
        self.plotButton.clicked.connect(self.plotFunction)
        self.grid.addWidget(self.plotButton)

    def plotFunction(self):
        func_input = self.userText.text()
        x = np.linspace(-200, 200, 400)  # Increased range for x-axis
        try:
            # Create a safe evaluation context with numpy
            safe_dict = {'x': x, 'np': np}
            # Evaluate the function
            y = eval(func_input, {"__builtins__": None}, safe_dict)
            if np.any(np.isinf(y)) or np.any(np.isnan(y)):
                QMessageBox.critical(self, "Error", "The function evaluated to invalid values (e.g., division by zero).")
                return

            plt.figure()  # Create a new figure
            plt.plot(x, y, label=f"y = {func_input}")
            plt.scatter(0, 0, color='red', marker='o', s=100, label='Origin (0, 0)')  # Mark the origin
            plt.title(f"Plot of {func_input}")
            plt.xlabel("x")
            plt.ylabel("y")
            plt.axhline(0, color='black', lw=0.5, ls='--')  # x-axis
            plt.axvline(0, color='black', lw=0.5, ls='--')  # y-axis
            
            # Set y-axis limits to zoom in
            plt.ylim(-10, 10)  # Adjust these values to control zoom level
            plt.xlim(-10, 10)
            
            plt.grid()
            plt.legend()  # Show the legend
            plt.show()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")