from PyQt5.QtWidgets import QWidget
from Windows import MainWindow


class AboutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(800, 600)
        self.setWindowTitle('About - Virtual world')
        self.setWindowIcon(MainWindow.MainWindow.main_icon)
        self.show()
