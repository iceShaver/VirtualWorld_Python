from Organisms.Plants.Plant import Plant


class Grass(Plant):
    def __init__(self, position, world):
        super().__init__(0, position, world)
