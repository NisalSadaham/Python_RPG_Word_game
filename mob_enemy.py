class Mob_Enemy:
    def __init__(self,name,hp,attack,defence,level = 5):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.level = level

    def special_ability(self):
        self.attack += 1
        print(f"{self.name} used attack up")

    def is_mob_alive(self):
        return self.hp > 0
    
    def damage_taken(self,amount):
        damage = max(amount - self.defence,1)
        self.hp -= damage
