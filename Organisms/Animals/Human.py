from Organisms.Animals.Animal import Animal


class Human(Animal):
    def __init__(self, position, world):
        super().__init__(5, 4, position, world)
