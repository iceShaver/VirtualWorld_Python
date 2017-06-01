import random

from Organisms.Organism import Organism
from Worlds.World import NeighbourPlaceSearchMode


class Plant(Organism):
    def __init__(self, strength, position, world):
        super().__init__(strength, 0, position, world)

    def act(self):
        if random.uniform(0, 1) < 0.01:
            self.sow()

    def _sow(self):
        new_position =self.world.get_random_neighbour_position(self.position, 1, NeighbourPlaceSearchMode.ONLY_EMPTY)
        if new_position is None:
            return
        self.world.add_organism(self.__class__(new_position, self.world))