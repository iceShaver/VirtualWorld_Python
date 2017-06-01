from Organisms.Animals.Animal import Animal


class Wolf(Animal):
    def __init__(self, position, world):
        super().__init__(9, 5, position, world)