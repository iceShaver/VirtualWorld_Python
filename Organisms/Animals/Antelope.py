import random

from PyQt5.QtGui import QIcon

from Organisms.Animals.Animal import Animal
from Organisms.Organism import ResistType
import Worlds.World
import Worlds.World
class Antelope(Animal):
    # icon = QIcon('Antelope.png')
    def __init__(self, position, world):
        super().__init__(4, 4, position, world)

    def act(self):
        new_position = self.world.get_random_neighbour_position(self.position, 2, Worlds.World.NeighbourPlaceSearchMode.ALL)
        if new_position is None:
            return

        organism_at_new_position = self.world.get_organism(new_position)

        if organism_at_new_position is None:
            self.world.move_organism(self, new_position)
        else:
            self.handle_collision(organism_at_new_position)

    def resist_attack(self, other):
        if random.uniform(0, 1) < 0.5:
            new_position = self.world.get_random_neighbour_position(self.position, 2, Worlds.World.NeighbourPlaceSearchMode.ONLY_EMPTY)
            if new_position is not None:
                self.world.move_organism(self, new_position)
                return ResistType.ESCAPE
        return super().resist_attack(other)
