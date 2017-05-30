from enum import Enum

class ResistType(Enum):
    SURRENDER = 0
    MOVE_TO_PREVIOUS_PLACE = 1
    KILL = 2
    ESCAPE = 3
    INCREASE_STRENGTH = 4
    MOVE_AROUND_ME = 5




class Organism:
    def __init__(self, strength, age, initiative, x, y, world):
        self.strength = strength
        self.age = age
        self.initiative = initiative
        self.x = x
        self.y = y
        self.world = world

    def __cmp__(self, other):
        if self.initiative == other.initiative:
            return self.age > other.age
        return self.initiative > other.initiative

    def act(self):  # abstract
        pass

    def handle_collision(self, other):   # abstract
        pass

    def resist_attack(self, other):
        if self.strength > other.strength:
            return ResistType.KILL
        return ResistType.SURRENDER


    def __str__(self):
        return self.__class__.__name__ + ' '+\
            '('+self.x+','+self.y+') '+self.strength+' '+\
            self.initiative + self.age

