from Organisms.Animals.Animal import Animal

# TODO: implement CyberSheep moving way (to the closest HeracleumSosnowskyi)
import Organisms.Plants.HeracleumSosnowskyi
import Worlds.World


class CyberSheep(Animal):
    def __init__(self, position, world):
        super().__init__(11, 4, position, world)

    def act(self):
        heracleum_sosnowskyis = [organism for organism in self.world.organisms_priority_list if
                                 isinstance(organism, Organisms.Plants.HeracleumSosnowskyi.HeracleumSosnowskyi)]
        if len(heracleum_sosnowskyis) == 0:
            super(CyberSheep, self).act()
            return
        closest = None
        if len(heracleum_sosnowskyis) == 1:
            closest = heracleum_sosnowskyis[0]
        else:
            min_distance = self.world.calculate_distance(self, heracleum_sosnowskyis[0])
            closest = heracleum_sosnowskyis[0]
            for heracleum_sosnowskyi in heracleum_sosnowskyis:
                tmp_dist = self.world.calculate_distance(self, heracleum_sosnowskyi)
                if tmp_dist < min_distance:
                    min_distance = tmp_dist
                    closest = heracleum_sosnowskyi

        new_position = Worlds.World.Position(self.position.x, self.position.y)

        if closest.position.x > self.position.x:
            new_position.x = self.position.x + 1
        elif closest.position.x < self.position.x:
            new_position.x = self.position.x - 1

        if closest.position.y > self.position.y:
            new_position.y = self.position.y + 1
        elif closest.position.y < self.position.y:
            new_position.y = self.position.y - 1

        if self.world.check_if_position_is_valid(new_position):
            if self.world.get_organism(new_position) is None:
                self.world.move_organism(self, new_position)
            else:
                self.handle_collision(self.world.get_organism(new_position))
