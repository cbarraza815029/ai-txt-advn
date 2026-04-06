# ------------ imports ------------
import os
from chr_stats import Hero, Enemy
import weapons

# ------------ setup ------------
hero = Hero(name="Hero",
            lvl=20,
            hp=100,
            armr=0)
hero.equip(weapons.short_sword)
enemy = Enemy(name="Enemy",
              lvl=10,
              hp=100,
              armr=10,
              weapons=weapons.claymore)

# ------------ combat loop ------------
hero_hp_old = None
enemy_hp_old = None
print("You've encountered an enemy!")

while True:
    #os.system("cls")

    print(f"Hero: {hero.hp} hp")
    print(f"Enemy: {enemy.hp} hp")
    print("")

    user_input = input("Action: ").lower()

    if user_input == "":
        hero_hp_old = hero.hp
        enemy_hp_old = enemy.hp

        hero.attack(hero, enemy)
        enemy.attack(enemy, hero)

        print(f"{hero.name} dealt {enemy_hp_old - enemy.hp} damage to {enemy.name}")
        print(f"{enemy.name} dealt {hero_hp_old - hero.hp} damage to {hero.name}")
        print("")
    elif user_input == "run":
        break
    else:
        print("Invalid input, try again!")
        print("")

    if hero.hp <= 0 or enemy.hp <= 0:
        #os.system("cls")
        print(f"Hero: {hero.hp} hp")
        print(f"Enemy: {enemy.hp} hp")
        print("")
        if hero.hp > enemy.hp:
            print("Congrats, you won!")
        elif hero.hp == enemy.hp:
            print("Strange, you died with your enemy!")
        else:
            print("Sorry, you lost!")
        break