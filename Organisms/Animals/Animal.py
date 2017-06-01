from Organisms.Organism import Organism, ResistType
from Worlds.World import NeighbourPlaceSearchMode, Position
import copy


# TODO: Alzur - człowiek wpada na zwierzę
class Animal(Organism):
    def __init__(self, strength, initiative, position, world):
        super().__init__(strength, initiative, position, world)

    def act(self):
        new_position = self.world.get_random_position(self.position, 1, NeighbourPlaceSearchMode.ALL)
        if new_position is None:
            return
        if self.world.get_organism(new_position) is not None:
            self.handle_collision(self.world.get_organism(new_position))
            return
        self.world.move_organism(self, new_position)

    def handle_collision(self, other):
        self.world.new_message("kolizja z ", self, other)

        if self.__class__ is other.__class__:  # the same organisms -> spawn
            new_random_position = self.world.get_random_neighbour_position(self.position, 1, Position,
                                                                           NeighbourPlaceSearchMode.ONLY_EMPTY)
            if new_random_position is None:
                return

            new_organism = self.__class__(new_random_position, self.world)
            self.world.add_organism(new_organism)
            self.world.new_message("rodzi się", new_organism)
            return
        new_position = copy.deepcopy(other.position)
        resist_result = other.resist_attack(self)

        if resist_result == ResistType.KILL:
            self.world.new_message("< ", self, other)
            self.world.delete_organism(self)
            return

        if resist_result == ResistType.SURRENDER:
            self.world.new_message("< ", self, other)
            self.world.delete_organism(other)
            self.world.move_organism(self, new_position)
            return

        if resist_result == ResistType.MOVE_TO_PREVIOUS_PLACE:
            self.world.new_message("zostaje odepchnięty przez ", self, other)
            return

        if resist_result == ResistType.ESCAPE:
            self.world.new_message("wypłoszył", self, other)
            self.world.move_organism(self, new_position)
            return

        if resist_result == ResistType.INCREASE_STRENGTH:
            self.strength += 3
            self.world.new_message("> ", self, other)
            self.world.delete_organism(other)
            self.world.new_message("siła rośnie do " + self.strength, self)
            self.world.move_organism(self, new_position)
            return

        if resist_result == ResistType.MOVE_AROUND_ME:
            new_random_position = self.world.get_random_neighbour_position(other.position, 1,
                                                                           NeighbourPlaceSearchMode.ONLY_EMPTY)
            if new_random_position is not None:
                self.world.move_organism(self, new_random_position)
