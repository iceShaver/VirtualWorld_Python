from Organisms.Organism import Organism
from Worlds.World import NeighbourPlaceSearchMode, Position


class Animal(Organism):
    def __init__(self, strength, age, initiative, x, y, world):
        super().__init__(strength, age, initiative, x, y, world)

    def act(self):
        new_position = self.world.get_random_position(position,1, NeighbourPlaceSearchMode.ALL)
        if new_position == None:
            return
        if(self.world.get_organism(new_position)!=None):
            self.handle_collision(self.world.get_organism(new_position))
            return
        self.world.move_organism(self, new_position)

    def handle_collision(self, other):
        new_position = Position(other.position.x, other.position.y)
