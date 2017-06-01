from Organisms.Plants.Plant import Plant


class Dandelion(Plant):
    def __init__(self, position, world):
        super().__init__(0, position, world)

    def act(self):
        for i in range(3):
            super().act()
