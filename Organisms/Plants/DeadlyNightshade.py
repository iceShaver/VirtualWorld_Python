from Organisms.Organism import ResistType
from Organisms.Plants.Plant import Plant


class DeadlyNightshade(Plant):
    def __init__(self,position, world):
        super().__init__(99, position, world)

    def resist_attack(self, other):
        return ResistType.KILL
