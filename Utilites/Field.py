from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton, QSizePolicy, QStyle

from Organisms.Animals.Antelope import Antelope


class Field(QPushButton):
    def __init__(self, parent):
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.setFixedSize(50, 50)
        # self.setStyleSheet('background-color: #fff;'
        #                   'border: 1px solid #000')
        # self.setStyleSheet('padding: 0px')
        self.organism = None

    def add_organism(self, organism):
        self.organism = organism
        # self.setIconSize(QSize().expandedTo(self.size()))
        self.setIcon(organism.icon)

    def remove_organism(self):
        self.organism = None
        self.setIcon(QIcon())
