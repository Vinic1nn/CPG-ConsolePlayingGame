from abc import ABC, abstractmethod


class monster(ABC): 
    def __init__(self, level, hp, stg, dex):
        self.level = level
        self.hp = hp
        self.stg = stg
        self.dex = dex
        super().__init__()

    def atack(self, characterDex, monsterDex):
        pass

    def damage(self, dano):
        dano = dano * (self.defense / 2)
        self.hp -= dano
        if  self.hp <= 0:
            print(f"{self.type} foi derrotado")
            del self
        else: 
            print(f"{self.type} tomou {dano} e está com {self.hp} HP")

    def special (self):
        pass
   

