import random
import Worlds.World
import Organisms.Organism
import Organisms.Animals.Animal
import Worlds.World


class Turtle(Organisms.Animals.Animal.Animal):
    def __init__(self, position, world):
        super().__init__(2, 1, position, world)

    def act(self):
        if random.uniform(0, 1) < 0.25:
            new_position = self.world.get_random_neighbour_position(self.position, 1,
                                                                    Worlds.World.NeighbourPlaceSearchMode.ALL)
            if new_position is None:
                return
            organism_at_new_position = self.world.get_organism(new_position)
            if organism_at_new_position is None:
                self.world.move_organism(self, new_position)
            else:
                self.handle_collision(organism_at_new_position)

    def resist_attack(self, other):
        if other.strength < 5:
            return Organisms.Organism.ResistType.MOVE_TO_PREVIOUS_PLACE
        return Organisms.Organism.ResistType.SURRENDER
