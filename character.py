from abc import ABC,abstractmethod

class Character(ABC):
    def __init__(self,name,hp,attack,defence,level = 1):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.level = level

    def is_alive(self):
        return self.hp > 0
    @abstractmethod
    def special_ability(self):
        pass
    @abstractmethod
    def can_use_special(self):
        pass
     
    def damage_taken (self,amount):
        damage = max(amount - self.defence,1)
        self.hp -= damage

        print(f"{self.name} has taken {damage}")
    def __str__(self):
         return f"NAME:{self.name} | LEVEL:{self.level} | HP:{self.hp} | ATTACK:{self.attack} | DEFENCE:{self.defence}"

class Swordsman(Character):
     def __init__(self, name, hp, attack, defence, level=1 ,charge = 0):
          super().__init__(name, hp, attack, defence, level)
          self.charge = charge
     def special_ability(self):
          self.charge += 10
          print(f"{self.name} gained charge!")

     def can_use_special(self):
        return self.charge >= 30

     def special_attack(self,target):
          damage = (self.attack * (50/100 * self.charge))
          print(f"{self.name} used high ground slash!")
          target.damage_taken(damage)
          self.charge = 0
   
class Mage(Character):
     def __init__(self, name, hp, attack, defence, mana=0, level=1):
           super().__init__(name, hp, attack, defence, level)
           self.mana = mana
     def special_ability(self):
           self.mana += 10
           print(f"{self.name} increased mana!")

     def can_use_special(self):
          return self.mana >= 30
     
     def special_attack(self,target):
          damage = (self.attack * (20/100 * self.mana))
          print(f"{self.name} used Ice spear!")
          target.damage_taken(damage)
          self.mana = 0

class Archer(Character):
       def __init__(self, name, hp, attack, defence, level=1 , stealth = 0):
            super().__init__(name, hp, attack, defence, level)
            self.stealth = stealth
       def special_ability(self):
            self.stealth += 10
            print(f"{self.name} vanished into the shadows!")
       def can_use_special(self):
            return self.stealth >= 30
       def special_attack(self,target):
            damage =  (self.attack * (35/100 * self.stealth))
            print(f"{self.name} used stealth attack!")
            target.damage_taken(damage)
            self.stealth = 0     
 
class Tank(Character):
       def __init__(self, name, hp, attack, defence, level=1, rage = 0 ):
            super().__init__(name, hp, attack, defence, level)
            self.rage = rage
       def special_ability(self):
            self.rage += 10
            print(f"{self.name} has gain rage!")
       def can_use_special(self):
            return self.rage >= 30
       def special_attack(self,target):
            damage =  (self.attack * (25/100 * self.rage))
            print(f"{self.name} used rampage!")
            target.damage_taken(damage)
            self.rage = 0
                 
     