from model.Entity import Entity

class Fighter(Entity):
    def __init__(self, x, y, health, mana, health_regen, mana_regen, move_points, max_health, max_mana):
        super().__init__(x, y, health, mana, health_regen, mana_regen, move_points, max_health, max_mana)
        # self.skills_id = ["Sword of Titan", "Dragon Slash", "Knee Cutter", "Trickery Sword"]
        self.skills_id = ["Sword"]
