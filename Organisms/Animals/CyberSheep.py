from Organisms.Animals.Animal import Animal


# TODO: implement CyberSheep moving way (to the closest HeracleumSosnowskyi)

class CyberSheep(Animal):
    def __init__(self, position, world):
        super().__init__(11, 4, position, world)
