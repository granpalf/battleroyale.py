import numpy as np

class Entity():
    def __init__(self, x, y, health, mana, health_regen, mana_regen, move_points, max_health, max_mana):
        # (x,y) coordinates in grid
        self.x = x
        self.y = y
        self.health = health
        self.mana = mana
        self.mana_regen = mana_regen
        self.health_regen = health_regen
        self.move_points = move_points
        self.max_mana = max_mana
        self.max_health = max_health


    def dist2(entity):
        return (self.x - entity.x) * (self.x - entity.x) + (self.y - entity.y) * (self.y - entity.y)

    def dist(entity):
        return abs(self.x - entity.x) + (self.y - entity.y)

    def regeneration():
        self.mana = max(self.max_mana, self.mana + self.mana_regen)
        self.health = max(self.max_health, self.health + self.health_regen)

    def move(cell):
        self.x = cell[0]
        self.y = cell[1]
