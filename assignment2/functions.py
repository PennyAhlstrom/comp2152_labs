# Import the random library to use for the dice later
import random
import hero
import monster

# Define two Dice
def small_dice_roll(small_dice_options):
    small_dice_options = list(range(1, 7))
    return random.choice(small_dice_options)

def big_dice_roll(big_dice_options):
    big_dice_options = list(range(1, 21))
    return random.choice(big_dice_options)

# Will the line below print when you import function.py into main.py?
# print("Inside function.py")


def use_loot(belt, health_points):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]

    print("    |    !!You see a monster in the distance! So you quickly use your first item:")
    first_item = belt.pop(0)
    if first_item in good_loot_options:
        health_points = min(20, (health_points + 2))
        print("    |    You used " + first_item + " to up your health to " + str(health_points))
    elif first_item in bad_loot_options:
        health_points = max(0, (health_points - 2))
        print("    |    You used " + first_item + " to hurt your health to " + str(health_points))
    else:
        print("    |    You used " + first_item + " but it's not helpful")
    return belt, health_points


def collect_loot(loot_options, belt):
    ascii_image3 = """                             
                     @@@@@@@@@@@                  
                @@@@@@         @@@                                   
              @@@             @@                   
               @@@@@    @@@ @@                    
                  @@@@@@@@@@@@@                   
                  @@@  @@ @@ @@@                  
                @@@    @   @@  @@@@               
              @@      @@    @@    @@@             
            @@        @@            @@@           
          @@@                         @@@         
         @@                             @@        
        @@                               @@         
         @@@                           @@         
           @@@@                    @@@@           
              @@@@@@@@@@@@@@@@@@@@@@                                                    
              """
    print(ascii_image3)
    # Created using https://www.asciiart.eu/image-to-ascii
    loot_roll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(loot_roll - 1)
    belt.append(loot)
    print("    |    Your belt: ", belt)
    return loot_options, belt


# Recursion
# You can choose to go crazy, but it will reduce your health points by 5
def inception_dream(num_dream_lvls):
    try:
        num_dream_lvls = int(num_dream_lvls)
        # Base Case
        if num_dream_lvls == 1:
            print("    |    You are in the deepest dream level now")
            print("    |", end="    ")
            input("Start to go back to real life? (Press Enter)")
            print("    |    You start to regress back through your dreams to real life.")
            return 2

        # Recursive Case
        else:
            # inception_dream(5)
            # 1 + inception_dream(4)
            # 1 + 1 + inception_dream(3)
            # 1 + 1 + 1 + inception_dream(2)
            # 1 + 1 + 1 + 1 + inception_dream(1)
            # 1 + 1 + 1 + 1 + 2
            return 1 + int(inception_dream(num_dream_lvls - 1))
    except ValueError:
        print("Invalid input. Please enter a number between 0-3.")

# Lab 06 - Question 3 and 4
def save_game(winner, hero_name="", num_stars=0, monsters_killed=0):
    with open("save.txt", "a") as file:
        if winner == "Hero":
            file.write(f"Hero {hero_name} has killed a monster and gained {num_stars} stars.\n")
        elif winner == "Monster":
            file.write("Monster has killed the hero previously\n")
        file.write(f"The number of monsters killed in total (including all past games) is now: {monsters_killed}.\n")

# Lab 06 - Question 5a
def load_game():
    try:
        with open("save.txt", "r") as file:
            print("    |    Loading from saved file ...")
            lines = file.readlines()
            if len(lines) <2:
                print("No previous game found. Starting fresh.")
                return None
            else:
                last_two_lines = lines[-2].strip() + "\n" + lines[-1].strip()
                print(last_two_lines)
                return last_two_lines
    except FileNotFoundError:
        print("No previous game found. Starting fresh.")
        return None

def load_monsters_killed():
    try:
        previous_game = load_game()
        if previous_game is None:
            return 0
        previous_monsters_killed = int(previous_game[-1].strip().split(":")[1])
        return previous_monsters_killed
    except ValueError:
        return 0

# Lab 06 - Question 5b
def adjust_combat_strength(combat_strength, last_game=None):
    # Lab Week 06 - Question 5 - Load the game
    # last_game = load_game()
    if last_game:
        if "Hero" in last_game and "gained" in last_game:
            num_stars = int(last_game.split()[-2])
            if num_stars > 3:
                print("    |    ... Increasing the monster's combat strength since you won so easily last time")
                monster.combat_strength+= 1
        elif "Monster has killed the hero" in last_game:
            combat_strength += 1
            print("    |    ... Increasing the hero's combat strength since you lost last time")
        else:
            print("    |    ... Based on your previous game, neither the hero nor the monster's combat strength will be increased")


