from PyQt5.QtWidgets import QPushButton, QSizePolicy


class Field(QPushButton):
    def __init__(self, parent):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.setFixedSize(50, 50)
        self.setStyleSheet('background-color: #fff;'
                           'border: 1px solid #000')
        self.organism = None

    def add_organism(self):
        pass

    def remove_organism(self):
        pass
