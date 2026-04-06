import os
from chr_stats import Hero, Enemy
import weapons

#Hero and Enemy setup
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

#Combat loop
#Used to calculate damage dealt
hero_hp_old = None
enemy_hp_old = None

print("You've encountered an enemy!")

while True:
    #os.system("cls")

    #Prints out Hero and Enemy hp before combat starts
    print(f"Hero: {hero.hp} hp")
    print(f"Enemy: {enemy.hp} hp")
    print("")

    user_input = input("Action: ").lower()

    #Pressing 'Enter' to attack
    if user_input == "":
        hero_hp_old = hero.hp
        enemy_hp_old = enemy.hp

        #Calls attack method from Chr_stats class so that Hero attacks Enemy and vice versa
        hero.attack(hero, enemy)
        enemy.attack(enemy, hero)

        #Prints damage dealt
        print(f"{hero.name} dealt {enemy_hp_old - enemy.hp} damage to {enemy.name}")
        print(f"{enemy.name} dealt {hero_hp_old - hero.hp} damage to {hero.name}")
        print("")
    #Run away from battle
    elif user_input == "run":
        break
    #Error message if typed invalid action
    else:
        print("Invalid input, try again!")
        print("")

    #Prints victory, tie, or failure message depending on which party has 0 hp
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