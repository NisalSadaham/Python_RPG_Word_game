class Boss_Enemy:
    def __init__(self,name,hp,attack,defence,level = 30, dragon_power = 0):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.level = level
        self.dragon_power = dragon_power

    def special_ability(self):
        self.attack += 10
        self.defence += 10
        print(f"{self.name} used self buff up")

    def is_boss_alive(self):
        return self.hp > 0
    
    def damage_taken(self,amount):
        damage = max(amount - self.defence,1)
        self.hp -= damage
        print(f"{self.name} has taken {damage}")

    def can_use_special(self):
        return self.dragon_power >= 30

    def special_attack(self):
        self.attack += 20
        print(f"{self.name} used dragon breath!")
        self.dragon_power = 0
