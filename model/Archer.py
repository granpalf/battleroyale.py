from model.Entity import Entity

class Archer(Entity):
    def __init__(self, x, y, health, mana, health_regen, mana_regen, move_points, max_health, max_mana):
        super().__init__(x, y, health, mana, health_regen, mana_regen, move_points, max_health, max_mana)
        # self.skills_id = ["Arrow Volley", "Rapid Fire", "Poison Arrow", "Web Arrow"]
        self.skills_id = ["Arrow"]
