import os
import platform
from pathlib import Path
import json
import ast

counter_chr_creation = 1
chr_stats = [
    0,#Vitality
    0,#Strength
    0,#Intelligence
    0,#Dexterity
    10#Available attribute points
]

def dist_att_points(total_points, current_points, desired_points):
    current_points = current_points + desired_points
    total_points = total_points - desired_points
    return current_points, total_points

def if_att_points_below_zero(total_points, current_points, desired_points):
    print("")
    print("Attribute points cannot fall below 0!")
    input("Press 'Enter' to continue")
    current_points = current_points - desired_points
    total_points = total_points + desired_points
    return current_points, total_points

def check_dist_points(remain_points):
    print("")
    print("Not enough points! Assign remaining points to selected attribute?")
    while True:
        usr_input = input("Enter: ")
        if usr_input == "yes" or usr_input == "y":
            return remain_points
        elif usr_input == "no" or usr_input == "n":
            return int(0)
        else:
            print("Invalid option, try again!")

def mod_chr_stats(chr_file, stats):
    with open(chr_file, 'w', encoding='utf-8') as file:
        json.dump(stats, file, ensure_ascii=False)

def exec_points_dist(total_points, current_points, desired_points):
    if desired_points > total_points:
        desired_points = check_dist_points(total_points)
    current_points, total_points = dist_att_points(total_points, current_points, desired_points)
    if current_points < 0:
        current_points, total_points = if_att_points_below_zero(total_points, current_points, desired_points)
    return current_points, total_points

def print_stats(chr_stats):
    print(f"Vitality: {chr_stats[0]}")
    print(f"Strength: {chr_stats[1]}")
    print(f"Intelligence: {chr_stats[2]}")
    print(f"Dexterity: {chr_stats[3]}")

def create(counter_chr_creation, chr_stats):
    file_dir = Path(__file__).parent.resolve()
    dir_slash = ""
    if platform.system().lower() == "windows":
        dir_slash = "\\" 
    else:
        dir_slash = "/" #For linux et al. systems
    save_file_dir = Path(f"{file_dir}{dir_slash}saves")
    save_file_count = sum(1 for save_file in save_file_dir.iterdir() if save_file.is_file())
    counter_chr_creation = counter_chr_creation + save_file_count
    file = f"chr_stats_{counter_chr_creation}.txt"
    file_abs_path = f"{file_dir}{dir_slash}saves{dir_slash}{file}"
    mod_chr_stats(file_abs_path, chr_stats)
    
    while chr_stats[4] > 0:
        os.system("cls")
        
        print("---------------------")
        print(f"Remaining points: {chr_stats[4]}")
        print("---------------------")
        print_stats(chr_stats)
        print("")
        print("Allocate attribute points")
        print("---------------------")
        choose_attribute = input("Choose an attribute: ").lower().strip()
        dist_points = None
        while dist_points is None:
            try:
                dist_points = int(input("How many points?: ").lower().strip())
            except ValueError:
                print("Integer values only. Try again!")
        
        if choose_attribute == "vitality" or choose_attribute == "vital" or choose_attribute == "vita" or choose_attribute == "vtlty" or choose_attribute == "vit" or choose_attribute == "v":
            chr_stats[0], chr_stats[4] = exec_points_dist(chr_stats[4], chr_stats[0], dist_points)
            mod_chr_stats(file_abs_path, chr_stats)
        
        elif choose_attribute == "strength" or choose_attribute == "strngth" or choose_attribute == "str" or choose_attribute == "s":
            chr_stats[1], chr_stats[4] = exec_points_dist(chr_stats[4], chr_stats[1], dist_points)
            mod_chr_stats(file_abs_path, chr_stats)
        
        elif choose_attribute == "intelligence" or choose_attribute == "intell" or choose_attribute == "intel" or choose_attribute == "int" or choose_attribute == "i":
            chr_stats[2], chr_stats[4] = exec_points_dist(chr_stats[4], chr_stats[2], dist_points)
            mod_chr_stats(file_abs_path, chr_stats)
        
        elif choose_attribute == "dexterity" or choose_attribute == "dxtrty" or choose_attribute == "dex" or choose_attribute == "d":
            chr_stats[3], chr_stats[4] = exec_points_dist(chr_stats[4], chr_stats[3], dist_points)
            mod_chr_stats(file_abs_path, chr_stats)
        
        else:
            print("")
            print("Invalid option, try again!")
            input("Press 'Enter' to continue")
    
    print("")
    print("---------------------")
    print("Final Character Stats")
    print("---------------------")
    print_stats(chr_stats)
    input("Press 'Enter' to continue")

def start():
    create(counter_chr_creation, chr_stats)

#start() #For standalone testing purposes only