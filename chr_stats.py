import weapons
import battle_dmg
''' Will implement later
class Chr_stats:
    def __init__(self, 
                 name: str,
                 lvl: int,
                 xp: int,
                 hp: int,
                 mp: int,
                 armr: int,
                 invn,
                 skills,
                 buffs,
                 debuffs
                 ) -> None:
        self.name = name
        self.lvl = lvl
        self.xp = xp
        self.hp = hp
        self.hp_max = hp
        self.mp = mp
        self.mp_max = mp
        self.armr = armr
        self.invn = invn
        self.skills = skills
        self.buffs = buffs
        self.debuffs = debuffs

        self.weapons = weapons.fists

    def attack(self, target) -> None:
        target.hp -= self.weapons.damage
        target.hp = max(target.hp, 0)

    def skills(self) -> None:
        crit_chance_skill = {"level": 0,
        "multiplier": 0
        }
        sword_skill = {"level": 0,
        "multiplier": 0
        }
        club_skill = {"level": 0,
        "multiplier": 0
        }
        hammer_skill = {"level": 0,
        "multiplier": 0
        }
        axe_skill = {"level": 0,
        "multiplier": 0
        }
        spear_skill = {"level": 0,
        "multiplier": 0
        }
        polearm_skill = {"level": 0,
        "multiplier": 0
        }
        ranged_skill = {"level": 0,
        "multiplier": 0
        }

invn
skills
buffs
debuffs
'''
class Chr_stats:
    def __init__(self, 
                 name: str,
                 lvl: int,
                 hp: int,
                 armr:int
                 ) -> None:
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.hp_max = hp
        self.armr = armr

        self.weapons = weapons.fists
    
    def attack(self, source, target) -> None:
        #target.hp -= self.weapons.damage
        target.hp -= battle_dmg.dmg_calc(source.lvl, self.weapons.damage, self.weapons.speed, target.lvl, target.armr)
        target.hp = max(target.hp, 0)

class Hero(Chr_stats):
    def __init__(self,
                 name: str,
                 lvl: int,
                 hp: int,
                 armr: int
                 ) -> None:
        super().__init__(name=name, lvl=lvl, hp=hp, armr=armr)

        self.default_weapons = self.weapons

    def equip(self, weapons) -> None:
        self.weapons = weapons
        print(f"{self.name} equipped a(n) {self.weapons.name}!")

    def drop(self) -> None:
        print(f"{self.name} dropped the {self.weapon.name}!")
        self.weapons = self.default_weapons

class Enemy(Chr_stats):
    def __init__(self,
                 name: str,
                 lvl: int,
                 hp: int,
                 armr: int,
                 weapons,
                 ) -> None:
        super().__init__(name=name, lvl=lvl, hp=hp, armr=armr)
        self.weapons = weapons