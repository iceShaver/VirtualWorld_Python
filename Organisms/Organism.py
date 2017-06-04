from enum import Enum

from PyQt5.QtGui import QIcon


class ResistType(Enum):
    SURRENDER = 0
    MOVE_TO_PREVIOUS_PLACE = 1
    KILL = 2
    ESCAPE = 3
    INCREASE_STRENGTH = 4
    MOVE_AROUND_ME = 5


class Organism:
    def __init__(self, strength, initiative, position, world):
        self.strength = strength
        self.age = 0
        self.initiative = initiative
        self.position = position
        self.world = world
        self.world.new_message("pojawia się", self)
        self.icon = world.main_window.icons[self.__class__.__name__]

    def __cmp__(self, other):
        if self.initiative == other.initiative:
            return self.age > other.age
        return self.initiative > other.initiative

    def __lt__(self, other):
        if self.initiative == other.initiative:
            return self.age < other.age
        return  self.initiative < other.initiative

    def __eq__(self, other):
        return self.position == other.position

    def act(self):  # abstract
        pass

    def handle_collision(self, other):  # abstract
        pass

    def resist_attack(self, other):
        if self.strength > other.strength:
            return ResistType.KILL
        return ResistType.SURRENDER


    def __str__(self):
        return self.__class__.__name__ + ' ' + \
               '(' + str(self.position.x) + ',' + str(self.position.y) + ') ' + str(self.strength) + ' ' + \
               str(self.initiative) + str(self.age)
