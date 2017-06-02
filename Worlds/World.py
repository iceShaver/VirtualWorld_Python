from enum import Enum
import copy
from Organisms.Organism import Organism
from Utilites.Reporter import Reporter
import random

class NeighbourPlaceSearchMode(Enum):
    ALL = 0
    ONLY_EMPTY = 1
    EMPTY_OR_WITH_WEAK_ORGANISM = 2


class Rect:
    def __init__(self, left, right, top, bottom):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class World:
    def __init__(self, main_window, width, height):
        self.main_window = main_window
        self.organisms_priority_list = []
        self.organism_array = [[None for i in range(width)] for i in range(height)]
        self.width = width
        self.height = height
        self.randomize_organisms()
        self.read_organisms_images()
        self.reporter = Reporter()

    def randomize_organisms(self):
        pass

    def add_organism(self, organism):
        self.organisms_priority_list.append(organism)
        self.organisms_priority_list.sort()
        self.organism_array[organism.position.x][organism.position.y] = organism
        pass

    def delete_organism(self, organism):
        self.organism_array[organism.x][organism.y] = None
        self.organisms_priority_list.remove(organism)
        pass

    def move_organism(self, organism, position):
        old_position = copy.deepcopy(organism.position)
        organism.position = copy.deepcopy(position)
        self.organism_array[position.x][position.y] = organism
        self.organism_array[old_position.x][old_position.y] = None

    def get_organism(self, position):
        return self.organism_array[position.x][position.y]
        pass

    def new_message(self, message, main_organism=None, other_organism=None):
        self.reporter.new_message(message, main_organism, other_organism)

    def get_random_neighbour_position(self, position, search_range, search_mode):
        positions = self.get_all_neighbour_positions(position, search_range, search_mode)
        if len(positions) == 0:
            return None
        if len(positions) ==1:
            return positions[0]
        return positions[random.randint(0, len(positions)-1)]


    def get_all_neighbour_positions(self, position, search_range, search_mode):
        rect = Rect()
        rect.left = position.x - search_range
        rect.right = position.x + search_range
        rect.top = position.y - search_range
        rect.bottom = position.y + search_range

        while rect.left < 0:
            rect.left += 1
        while rect.top < 0:
            rect.top += 1
        while rect.right > self.width - 1:
            rect.right -= 1
        while rect.bottom > self.height - 1:
            rect.bottom -= 1

        tmp_position = Position(rect.left, rect.top)
        where_can_move = []

        while True:
            if search_mode == NeighbourPlaceSearchMode.ONLY_EMPTY:
                if self.get_organism(tmp_position) is None:
                    where_can_move.append(copy.deepcopy(tmp_position))
                if tmp_position.x >= rect.right:
                    if tmp_position.y > rect.bottom:
                        if self.get_organism(tmp_position) is None:
                            where_can_move.append(copy.deepcopy(tmp_position))
                        break
                    tmp_position.y = +1
                    tmp_position.x = rect.left
                else:
                    tmp_position.x += 1
            elif search_mode == NeighbourPlaceSearchMode.ALL:
                if not (tmp_position.x == position.x and tmp_position.y == position.y) and not (
                            tmp_position == position):
                    where_can_move.append(copy.deepcopy(tmp_position))
                if tmp_position.x >= rect.right:
                    if tmp_position.y >= rect.bottom:
                        if not (tmp_position.x == position.x and tmp_position.y == position.y) and not (
                                    tmp_position == position):
                            where_can_move.append(copy.deepcopy(tmp_position))
                        break
                    tmp_position.y += 1
                    tmp_position.x = rect.left
                else:
                    tmp_position.x += 1
            elif search_mode == NeighbourPlaceSearchMode.EMPTY_OR_WITH_WEAK_ORGANISM:
                if self.get_organism(tmp_position) is None:
                    where_can_move.append(copy.deepcopy(tmp_position))
                elif self.get_organism(position).strength >= self.get_organism(tmp_position).strength and not (
                            tmp_position == position):
                    where_can_move.append(copy.deepcopy(tmp_position))
                if tmp_position.x >= rect.right:
                    if tmp_position.y >= rect.bottom:
                        if self.get_organism(tmp_position) is None:
                            where_can_move.append(copy.deepcopy(tmp_position))
                        elif self.get_organism(position).strength >= self.get_organism(tmp_position).strength and not (
                                    tmp_position == position):
                            where_can_move.append(copy.deepcopy(tmp_position))
                        break
                    tmp_position.y += 1
                    tmp_position.x = rect.left
                else:
                    tmp_position.x += 1
        return where_can_move
