from Organisms.Organism import ResistType
from Organisms.Plants.Plant import Plant


class Guarana(Plant):
    def __init__(self, position, world):
        super().__init__(0, position, world)

    def resist_attack(self, other):
        return ResistType.INCREASE_STRENGTH
