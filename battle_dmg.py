import chr_stats
import weapons
'''
this module will calculate damage during battle by taking into consideration weapon, level, buffs, debuffs,
etc. and pass result on to battle.py
'''
#weapon_damage = weapons.Weapon
#weapon_speed = weapons.Weapon

'''
will implement later
def dmg_calc(attacker_lvl, attacker_weapon_dmg, attacker_weapon_spd, attacker_armr, attacker_skills, attacker_buff, attacker_debuff,
             defender_lvl, defender_weapon_dmg, defender_weapon_spd, defender_armr, defender_skills, defender_buff, defender_debuff):
'''

def dmg_calc(attacker_lvl, attacker_weapon_dmg, attacker_weapon_spd,
             defender_lvl, defender_armr):
    dmg_calc_atk = (attacker_weapon_dmg * attacker_weapon_spd) + (attacker_lvl - defender_lvl)

    dmg_calc_def = defender_armr

    dmg_calc_final = dmg_calc_atk - dmg_calc_def
    if dmg_calc_final <= 0:
        dmg_calc_final = 0

    #print(dmg_calc_final) #used to see final damage calc

    return dmg_calc_final

'''
damage calc must take into account:
level difference between attacker and defender (e.g. player lower level than opponent deals less damage)
crit chance
dodge chance
weapon damage
weapon speed
character skills
character buffs
character debuffs
'''