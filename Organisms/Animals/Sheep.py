from Organisms.Animals.Animal import Animal


class Sheep(Animal):
    def __init__(self, position, world):
        super().__init__(4, 4, position, world)