import sys
import psutil

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import QTimer

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class CPUVisualizer(QMainWindow):

    def __init__(self):
        super().__init__()

        # Set up the GUI layout
        self.mainWidget = QWidget(self)
        self.setCentralWidget(self.mainWidget)
        layout = QVBoxLayout(self.mainWidget)

        # Label to display CPU info
        self.label = QLabel(self)
        layout.addWidget(self.label)

        # Set up the matplotlib canvas
        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.ax = self.canvas.figure.subplots()
        layout.addWidget(self.canvas)

        # Set the timer to update the plot
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_figure)
        self.timer.start(1000)  # Update every second

        self.setWindowTitle("CPU Stats Visualizer")
        self.setGeometry(100, 100, 600, 400)
        self.show()

    def update_figure(self):
        # Get CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)
        self.label.setText(f"CPU Usage: {cpu_percent}%")

        # Update the plot
        self.ax.clear()
        self.ax.bar(['CPU'], [cpu_percent], color='blue')
        self.ax.set_ylim(0, 100)
        self.ax.set_ylabel("Usage (%)")
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CPUVisualizer()
    sys.exit(app.exec_())
