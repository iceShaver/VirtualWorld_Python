from enum import Enum

from Organisms.Organism import Organism
from Utilites.Reporter import Reporter


class NeighbourPlaceSearchMode(Enum):
    ALL = 0
    ONLY_EMPTY = 1
    EMPTY_OR_WITH_WEAK_ORGANISM = 2


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class World:
    def __init__(self, main_window, width, height):
        self.main_window = main_window
        self.organisms_priority_list = []
        self.organism_array = [[Organism for i in range(width)]for i in range(height)]
        self.width = width
        self.height = height
        self.randomize_organisms()
        self.read_organisms_images()
        self.reporter = Reporter()

    def randomize_organisms(self):
        pass

    def add_organism(self):
        pass

    def delete_organism(self):
        pass

    def move_organism(self):
        pass

    def get_organism(self):
        pass

    def new_message(self, message, main_organism=None, other_organism=None):
        self.reporter.new_message(message, main_organism, other_organism)

    def get_random_position(self, search_range, search_mode):
        pass

    def get_random_neighbour_position(self, position, search_range, search_mode):
        pass

    def get_all_neighbour_positions(self, position, search_range, search_mode):
        pass


