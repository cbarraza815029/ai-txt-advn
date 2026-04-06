class Weapon:
    def __init__(self,
                 name: str,
                 weapon_type: str,
                 enchanted: bool,
                 damage: int,
                 speed: float,
                 weight: int,
                 value: int
                 ) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.enchanted = enchanted
        self.damage = damage
        self.speed = speed
        self.weight = weight
        self.value = value

'''
name = name of weapon
weapon_type = the type of weapon
enchanted = whether a weapon is enchanted (True or False)
damage = how much damage a weapon does
speed = how fast a weapon does damage (0 = slowest, 1 = fastest)
weight = how much a weapon weighs
value = how much a weapon is worth (1 copper, 1 silver [100 copper], 1 gold [100 silver, 10,000 copper])
'''

#----------------------------------------------
#           Fists (i.e. no weapon)
#----------------------------------------------
fists = Weapon(name = "Fists",
               weapon_type = "blunt",
               enchanted = False,
               damage = 1,
               speed = 1.0,
               weight = 0,
               value = 0)

#----------------------------------------------
#                   Blade
#----------------------------------------------
small_axe  = Weapon(name =  "Small Axe",
                    weapon_type =  "blade",
                    enchanted =  False,
                    damage =  3,
                    speed =  0.9,
                    weight =  1,
                    value =  3)

dagger = Weapon(name =  "Dagger",
                weapon_type =  "blade",
                enchanted =  False,
                damage =  3,
                speed =  1,
                weight =  1,
                value =  3)

short_sword = Weapon(name =  "Short Sword",
                     weapon_type =  "blade",
                     enchanted =  False,
                     damage =  5,
                     speed =  0.8,
                     weight =  2,
                     value =  5)

long_sword = Weapon(name =  "Long Sword",
                    weapon_type =  "blade",
                    enchanted =  False,
                    damage =  7,
                    speed =  0.7,
                    weight =  3,
                    value =  10)

great_sword = Weapon(name =  "Great Sword",
                     weapon_type =  "blade",
                     enchanted =  False,
                     damage =  10,
                     speed =  0.6,
                     weight =  5,
                     value =  20)

claymore = Weapon(name =  "Claymore",
                  weapon_type =  "blade",
                  enchanted =  False,
                  damage =  25,
                  speed =  0.5,
                  weight =  10,
                  value =  50)

sabre = Weapon(name =  "Sabre",
               weapon_type =  "blade",
               enchanted =  False,
               damage =  12,
               speed =  0.7,
               weight =  3,
               value =  25)

falchion = Weapon(name =  "Falchion",
                  weapon_type =  "blade",
                  enchanted =  False,
                  damage =  15,
                  speed =  0.7,
                  weight =  4,
                  value =  0)

rapier = Weapon(name =  "Rapier",
                weapon_type =  "blade",
                enchanted =  False,
                damage =  10,
                speed =  0.8,
                weight =  2,
                value =  30)

''' Will implement later
#----------------------------------------------
#                   Polearm
#----------------------------------------------
spear = Weapon(name =  "Spear",
               weapon_type =  "polearm",
               enchanted =  False,
               damage =  1,
               speed =  float,
               weight =  0,
               value =  0)

lance = Weapon(name =  "Lance",
               weapon_type =  "polearm",
               enchanted =  False,
               damage =  1,
               speed =  float,
               weight =  0,
               value =  0)

pitchfork = Weapon(name =  "Pitchfork",
               weapon_type =  "polearm",
               enchanted =  False,
               damage =  1,
               speed =  float,
               weight =  0,
               value =  0)

poleaxe = Weapon(name =  "Poleaxe",
               weapon_type =  "polearm",
               enchanted =  False,
               damage =  1,
               speed =  float,
               weight =  0,
               value =  0)

halberd = Weapon(name =  "Halberd",
               weapon_type =  "polearm",
               enchanted =  False,
               damage =  1,
               speed =  float,
               weight =  0,
               value =  0)

glaive = Weapon(name =  "Glaive",
               weapon_type =  "polearm",
               enchanted =  False,
               damage =  1,
               speed =  float,
               weight =  0,
               value =  0)

battle_axe = Weapon(name =  "Battle Axe",
               weapon_type =  "polearm",
               enchanted =  False,
               damage =  1,
               speed =  float,
               weight =  0,
               value =  0)

#----------------------------------------------
#                   Blunt
#----------------------------------------------
club = Weapon(name =  "Club",
               weapon_type =  "blunt",
               enchanted =  False,
               damage =  1,
               speed =  float,
               weight =  0,
               value =  0)

cudgel = Weapon(name =  "Cudgel",
               weapon_type =  "blunt",
               enchanted =  False,
               damage =  1,
               speed =  float,
               weight =  0,
               value =  0)

morning_star = Weapon(name =  "Morning Star",
               weapon_type =  "blunt",
               enchanted =  False,
               damage =  1,
               speed =  float,
               weight =  0,
               value =  0)

mace = Weapon(name =  "Mace",
               weapon_type =  "blunt",
               enchanted =  False,
               damage =  1,
               speed =  float,
               weight =  0,
               value =  0)

maul = Weapon(name =  "Maul",
               weapon_type =  "blunt",
               enchanted =  False,
               damage =  1,
               speed =  float,
               weight =  0,
               value =  0)

hammer = Weapon(name =  "Hammer",
               weapon_type =  "blunt",
               enchanted =  False,
               damage =  1,
               speed =  float,
               weight =  0,
               value =  0)

war_hammer = Weapon(name =  "War Hammer",
               weapon_type =  "blunt",
               enchanted =  False,
               damage =  1,
               speed =  float,
               weight =  0,
               value =  0)

short_staff = Weapon(name =  "Short Staff",
               weapon_type =  "blunt",
               enchanted =  False,
               damage =  1,
               speed =  float,
               weight =  0,
               value =  0)

long_staff = Weapon(name =  "Long Staff",
               weapon_type =  "blunt",
               enchanted =  False,
               damage =  1,
               speed =  float,
               weight =  0,
               value =  0)

#----------------------------------------------
#                   Ranged
#----------------------------------------------
short_bow = Weapon(name =  "Short Bow",
               weapon_type =  "ranged",
               enchanted =  False,
               damage =  1,
               speed =  float,
               weight =  0,
               value =  0)

long_bow = Weapon(name =  "Long Bow",
               weapon_type =  "ranged",
               enchanted =  False,
               damage =  1,
               speed =  float,
               weight =  0,
               value =  0)

crossbow = Weapon(name =  "Crossbow",
               weapon_type =  "ranged",
               enchanted =  False,
               damage =  1,
               speed =  float,
               weight =  0,
               value =  0)

arbalest = Weapon(name =  "Arbalest",
               weapon_type =  "ranged",
               enchanted =  False,
               damage =  1,
               speed =  float,
               weight =  0,
               value =  0)
'''