from enum import Enum

from PyQt5.QtCore import Qt

from Organisms.Animals.Animal import Animal
import Worlds.World
from Organisms.Organism import ResistType


class MoveDirection(Enum):
    NONE = 0
    UP_LEFT = 1
    UP = 2
    UP_RIGHT = 3
    LEFT = 4
    RIGHT = 5
    DOWN_LEFT = 6
    DOWN = 7
    DOWN_RIGHT = 8


class Human(Animal):
    def __init__(self, position, world):
        super().__init__(5, 4, position, world)
        self.move_direction = MoveDirection.NONE
        self.alzurs_shield_activated = False
        self.counter = 5

    def handle_input(self, e):
        key = e.key()
        if key == Qt.Key_1:
            self.move_direction = MoveDirection.DOWN_LEFT
        elif key == Qt.Key_2:
            self.move_direction = MoveDirection.DOWN
        elif key == Qt.Key_3:
            self.move_direction = MoveDirection.DOWN_RIGHT
        elif key == Qt.Key_4:
            self.move_direction = MoveDirection.LEFT
        elif key == Qt.Key_5:
            self.move_direction = MoveDirection.NONE
        elif key == Qt.Key_6:
            self.move_direction = MoveDirection.RIGHT
        elif key == Qt.Key_7:
            self.move_direction = MoveDirection.UP_LEFT
        elif key == Qt.Key_8:
            self.move_direction = MoveDirection.UP
        elif key == Qt.Key_9:
            self.move_direction = MoveDirection.UP_RIGHT
        elif key == Qt.Key_S:
            self.alzurs_shield_input_handle()

    def alzurs_shield_input_handle(self):
        if self.alzurs_shield_activated:
            return
        if self.counter >= 5:  # activate alzurs shield
            self.world.new_message('tarcza alzura aktywowana ',self)
            self.alzurs_shield_activated = True
            self.counter = 0

    def act(self):
        self.counter += 1
        if self.alzurs_shield_activated:
            if self.counter >= 5:
                self.world.new_message('tarcza alzura zdezaktywowana ', self)
                self.alzurs_shield_activated = False
                self.counter = 0
        new_position = Worlds.World.Position(self.position.x, self.position.y)
        if self.move_direction == MoveDirection.NONE:
            pass
        elif self.move_direction == MoveDirection.UP_LEFT:
            new_position.x -= 1
            new_position.y -= 1
        elif self.move_direction == MoveDirection.UP:
            new_position.y -= 1
        elif self.move_direction == MoveDirection.UP_RIGHT:
            new_position.x += 1
            new_position.y -= 1
        elif self.move_direction == MoveDirection.LEFT:
            new_position.x -= 1
        elif self.move_direction == MoveDirection.RIGHT:
            new_position.x += 1
        elif self.move_direction == MoveDirection.DOWN_LEFT:
            new_position.x -= 1
            new_position.y += 1
        elif self.move_direction == MoveDirection.DOWN:
            new_position.y += 1
        elif self.move_direction == MoveDirection.DOWN_RIGHT:
            new_position.x += 1
            new_position.y += 1

        if new_position == self.position:
            return
        if not self.world.check_if_position_is_valid(new_position):
            return

        if self.world.get_organism(new_position) is not None:
            self.handle_collision(self.world.get_organism(new_position))
            return
        self.world.move_organism(self, new_position)

    def handle_collision(self, other):
        super().handle_collision(other)

    def resist_attack(self, other):
        if self.alzurs_shield_activated:
            return ResistType.MOVE_AROUND_ME
        else:
            super(Human, self).resist_attack(other)
