from Organisms.Animals.Animal import Animal
from Organisms.Animals.CyberSheep import CyberSheep
from Organisms.Organism import ResistType
from Organisms.Plants.Plant import Plant
from Worlds.World import NeighbourPlaceSearchMode


class HeracleumSosnowskyi(Plant):
    def __init__(self, strength, position, world):
        super().__init__(strength, position, world)

    def resist_attack(self, other):
        if isinstance(other, CyberSheep):
            return ResistType.SURRENDER
        return ResistType.KILL

    def act(self):
        super().act()
        neighbour_organism_positions = self.world.get_all_neighbour_positions(self.position, 1,
                                                                              NeighbourPlaceSearchMode.ALL)
        for position in neighbour_organism_positions:
            neighbour_organism = self.world.get_organism(position)
            if neighbour_organism is not None:
                if isinstance(neighbour_organism, Animal) and not isinstance(CyberSheep):
                    self.world.new_message("zabija ", self, neighbour_organism)
                    self.world.delete_organism(neighbour_organism)
