from enum import Enum

from Utilites.Reporter import Reporter


class NeighbourPlaceSearchMode(Enum):
    ALL = 0
    ONLY_EMPTY = 1
    EMPTY_OR_WITH_WEAK_ORGANISM = 2

class Position:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class World:
    def __init__(self, main_window):
        self.main_window = main_window
        self.organisms = []
        self.randomize_organisms()
        self.read_organisms_images()
        self.reporter = Reporter()

    def randmize_organisms(self):
        pass

    def add_organism(self):
        pass

    def delete_organism(self):
        pass

    def move_organism(self):
        pass
