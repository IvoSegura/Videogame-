import random


class spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def generate_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)


"""
   def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]


def generate_spell_damage(self, i):
    mgl = self.magic[i]["dmg"] - 5
    mgh = self.magic[i]["dmg"] + 5
    return random.randrange(mgl, mgh)
    
    
    magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 12, "dmg": 120},
         {"name": "Blizzard", "cost": 10, "dmg": 160}]
"""
