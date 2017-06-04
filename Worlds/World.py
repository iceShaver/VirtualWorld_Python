from enum import Enum
import copy
import Organisms.Animals.Antelope
import Organisms.Animals.Turtle
import Organisms.Animals.Sheep
import Organisms.Animals.Fox
import Organisms.Animals.Human
import Organisms.Animals.Wolf
import Organisms.Plants.Dandelion
import Organisms.Plants.DeadlyNightshade
import Organisms.Plants.Grass
import Organisms.Plants.Guarana
import Organisms.Plants.HeracleumSosnowskyi
import Utilites.Field
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
    def __init__(self, name, width, height, main_window):
        self.main_window = main_window
        self.organisms_priority_list = []
        self.fields = [[Utilites.Field.Field(main_window) for i in range(height)] for i in range(width)]
        self.width = width
        self.height = height
        self.name = name
        self.reporter = Reporter()
        self.randomize_organisms()

    def randomize_organisms(self):
        self.add_organism(Organisms.Animals.Antelope.Antelope(self.get_random_empty_position(), self))
        self.add_organism(Organisms.Animals.CyberSheep.CyberSheep(self.get_random_empty_position(), self))
        self.add_organism(Organisms.Animals.Fox.Fox(self.get_random_empty_position(), self))
        self.add_organism(Organisms.Animals.Human.Human(self.get_random_empty_position(), self))
        self.add_organism(Organisms.Animals.Sheep.Sheep(self.get_random_empty_position(), self))
        self.add_organism(Organisms.Animals.Turtle.Turtle(self.get_random_empty_position(), self))
        self.add_organism(Organisms.Animals.Wolf.Wolf(self.get_random_empty_position(), self))
        self.add_organism(Organisms.Plants.Dandelion.Dandelion(self.get_random_empty_position(), self))
        self.add_organism(Organisms.Plants.DeadlyNightshade.DeadlyNightshade(self.get_random_empty_position(), self))
        self.add_organism(Organisms.Plants.HeracleumSosnowskyi.HeracleumSosnowskyi(self.get_random_empty_position(), self))
        self.add_organism(Organisms.Plants.Guarana.Guarana(self.get_random_empty_position(), self))
        self.add_organism(Organisms.Plants.Grass.Grass(self.get_random_empty_position(), self))

    def add_organism(self, organism):
        self.organisms_priority_list.append(organism)
        self.organisms_priority_list.sort()
        self.fields[organism.position.x][organism.position.y].add_organism(organism)
        pass

    def delete_organism(self, organism):
        self.fields[organism.position.x][organism.position.y].remove_organism()
        self.organisms_priority_list.remove(organism)
        pass

    def move_organism(self, organism, position):
        old_position = copy.deepcopy(organism.position)
        organism.position = copy.deepcopy(position)
        self.fields[position.x][position.y].add_organism(organism)
        self.fields[old_position.x][old_position.y].remove_organism()

    def get_organism(self, position):
        return self.fields[position.x][position.y].organism

    def new_message(self, message, main_organism=None, other_organism=None):
        self.reporter.new_message(message, main_organism, other_organism)

    def play_round(self):
        for organism in self.organisms_priority_list:
            organism.act()

    def get_random_empty_position(self):
        while True:
            rand_x = random.randint(0, self.width - 1)
            rand_y = random.randint(0, self.height - 1)
            position = Position(rand_x, rand_y)
            if self.get_organism(position) is None:
                return position

    def get_random_neighbour_position(self, position, search_range, search_mode):
        positions = self.get_all_neighbour_positions(position, search_range, search_mode)
        if len(positions) == 0:
            return None
        if len(positions) == 1:
            return positions[0]
        return positions[random.randint(0, len(positions) - 1)]

    def get_all_neighbour_positions(self, position, search_range, search_mode):
        rect = Rect(position.x - search_range,
                    position.x + search_range,
                    position.y - search_range,
                    position.y + search_range)

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
                    where_can_move.append(Position(tmp_position.x, tmp_position.y))
                if tmp_position.x >= rect.right:
                    if tmp_position.y > rect.bottom:
                        if self.get_organism(tmp_position) is None:
                            where_can_move.append(Position(tmp_position.x, tmp_position.y))
                        break
                    tmp_position.y += 1
                    tmp_position.x = rect.left
                else:
                    tmp_position.x += 1
            elif search_mode == NeighbourPlaceSearchMode.ALL:
                if not (tmp_position.x == position.x and tmp_position.y == position.y) and not (
                            tmp_position == position):
                    where_can_move.append(Position(tmp_position.x, tmp_position.y))
                if tmp_position.x >= rect.right:
                    if tmp_position.y >= rect.bottom:
                        if not (tmp_position.x == position.x and tmp_position.y == position.y) and not (
                                    tmp_position == position):
                            where_can_move.append(Position(tmp_position.x, tmp_position.y))
                        break
                    tmp_position.y += 1
                    tmp_position.x = rect.left
                else:
                    tmp_position.x += 1
            elif search_mode == NeighbourPlaceSearchMode.EMPTY_OR_WITH_WEAK_ORGANISM:
                if self.get_organism(tmp_position) is None:
                    where_can_move.append(Position(tmp_position.x, tmp_position.y))
                elif self.get_organism(position).strength >= self.get_organism(tmp_position).strength and not (
                            tmp_position == position):
                    where_can_move.append(Position(tmp_position.x, tmp_position.y))
                if tmp_position.x >= rect.right:
                    if tmp_position.y >= rect.bottom:
                        if self.get_organism(tmp_position) is None:
                            where_can_move.append(Position(tmp_position.x, tmp_position.y))
                        elif self.get_organism(position).strength >= self.get_organism(tmp_position).strength and not (
                                    tmp_position == position):
                            where_can_move.append(Position(tmp_position.x, tmp_position.y))
                        break
                    tmp_position.y += 1
                    tmp_position.x = rect.left
                else:
                    tmp_position.x += 1
        return where_can_move
