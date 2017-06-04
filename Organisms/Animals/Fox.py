from Organisms.Animals.Animal import Animal
# from Worlds.World import NeighbourPlaceSearchMode
import Worlds.World

class Fox(Animal):
    def __init__(self, position, world):
        super().__init__(3, 7, position, world)

    def act(self):
        new_position = self.world.get_random_neighbour_position(self.position, 1,
                                                                Worlds.World.NeighbourPlaceSearchMode.EMPTY_OR_WITH_WEAK_ORGANISM)
        if new_position is None:
            return
        organism_at_new_position = self.world.get_organism(new_position)
        if organism_at_new_position is None:
            self.world.move_organism(self, new_position)
        else:
            self.handle_collision(organism_at_new_position)