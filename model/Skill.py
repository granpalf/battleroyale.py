class Skill():
    def __init__(self, caster_cell, mana_cost, skill_id, cooldown, skill_range):
        self.caster_cell = caster_cell
        self.mana_cost = mana_cost
        self.cooldown = cooldown
        self.skill_id = skill_id
        self.skill_range = skill_range


    def showRange():
        """ TODO : Change function when there are obstacles
            Returns list of cells reachable with this skill
        """
        reachable_cells = []
        for i in range(self.move_points):
            for j in range(self.move_points):
                reachable_cells.append((i+self.caster_cell[0], j+self.caster_cell[1]))
        return reachable_cells

    
