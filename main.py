#imports
import time
import json
import pickle
import character as character
import mob_enemy as mob_enemy
import boss_enemy as boss_enemy


storage = {}
player_character = ''


#functions
def type_words(text, delay=0.3):
    for word in text.split(' '):
        print(word, end=' ', flush=True)
        time.sleep(delay)
    print()

def read_file_json(file_name):
    with open(file_name,"r") as file:
        return json.load(file)
    
def save_player_data(storage):
    with open("player_data.json","w") as file:
        return json.dump(storage,file)
    
def save_character_data(player_character):
    with open("character_data.pkl",'wb') as file:
        return pickle.dump(player_character,file)

def load_save_character():
    with open("character_data.pkl", "rb") as file:
        return pickle.load(file)

def battle_menu():
    print("What do you want to do?")
    print("1. Basic Attack")
    print("2. Use special ability")
    print("3. Use Ultimate attack")


def boss_battle(player_character,enemy):
    turn = 1
    while player_character.is_alive() and enemy.is_boss_alive():
        battle_menu()
        try:
#players turn
            choice = int(input("Pick your choice please:"))

            if choice == 1:
                print(f"Hero STS:{player_character}")
                enemy.damage_taken(player_character.attack)
                print("The hero used basic attack!")
                time.sleep(1)
            elif choice == 2:
                print(f"Hero STS:{player_character}")
                player_character.special_ability()
                time.sleep(1)
            elif choice == 3:
                print(f"Hero STS:{player_character}")
                if not player_character.can_use_special():
                    print("Unable to use ultimate now")
                else:
                    print(f"Hero STS:{player_character}")
                    player_character.special_attack(enemy)
                    time.sleep(2)
            else:
                print("Invalid choice please choose again!")
                continue
            if not enemy.is_boss_alive():
                print("Battle has ended You have won!")
                return True ,"WIN"
                
    #enemy turn
            if enemy.can_use_special():
                enemy.special_attack(player_character)

            elif turn % 2 == 0:
                enemy.special_ability() 
                    
            else:    
                player_character.damage_taken(enemy.attack)

            if not player_character.is_alive():
                print("You have lost this battle")
                return False, "LOSE"
    
            turn+=1
        except ValueError:
            print("Invalid choice plz retry..")
            continue
def mob_battle(player_character,enemy):
    turn = 1
    while player_character.is_alive() and enemy.is_mob_alive():
        battle_menu()
        try:
#players turn
            choice = int(input("Pick your choice please:"))

            if choice == 1:
                print(f"Hero STS:{player_character}")
                enemy.damage_taken(player_character.attack)
                print("The hero used basic attack!")
                time.sleep(1)
            elif choice == 2:
                print(f"Hero STS:{player_character}")
                player_character.special_ability()
                time.sleep(1)
            elif choice == 3:
                print(f"Hero STS:{player_character}")
                if not player_character.can_use_special():
                    print("Unable to use ultimate now")
                else:
                    print(f"Hero STS:{player_character}")
                    player_character.special_attack(enemy)
                    time.sleep(2)
            else:
                print("Invalid choice please choose again!")
                continue
            if not enemy.is_mob_alive():
                print("Battle has ended You have won!")
                return True ,"WIN"
                
    #enemy turn
            if turn % 2 == 0:
                enemy.special_ability()      
            else:    
                player_character.damage_taken(enemy.attack)

            if not player_character.is_alive():
                print("You have lost this battle")
                return False, "LOSE"
    
            turn+=1
        except ValueError:
            print("Invalid choice plz retry..")
            continue
def game_intro():
    intro_dialogue = read_file_json('text_resources.json')

    for key,sentences in intro_dialogue.items():
        type_words(sentences)

def player_name_setup():
    player_name = input("Enter your name hero:")

    if player_name != "":
        storage["Name"]= player_name
        save_player_data(storage)
        type_words(f"Nice to meet you {player_name}")
        type_words("Now Its time for you to get a class!")


def Player_class_setup():
    class_info = read_file_json('class_details.json')
    player_name = read_file_json('player_data.json')

    for classes_info,info in class_info['classes'].items():
        type_words (f"{info['number']}.{classes_info} {info['description']}")
 
    tries = True
    while tries:
        try:
            picked_class = int(input("Pick a class from the list above(1-4):"))
            match (picked_class):
                case 1:
                    name = player_name['Name']
                    print(name)
                    player_character = character.Swordsman(name=name,hp=120,attack=25,defence=20)
                    save_character_data(player_character)
                    print("Character created successfully!")
                    break
                case 2:
                    name = player_name['Name']
                    player_character = character.Mage(name=name,hp=80,attack=50,defence=10)
                    save_character_data(player_character)
                    print("Character created successfully!")
                    break
                case 3:
                    name = player_name['Name']
                    player_character = character.Archer(name=name,hp=80,attack=70,defence=20)
                    save_character_data(player_character)
                    print("Character created successfully!")
                    break
                case 4:
                    name = player_name['Name']
                    player_character = character.Tank(name=name,hp=200,attack=10,defence=50)
                    save_character_data(player_character)
                    print("Character created successfully!")
                    break

                case _:
                    print("Invalid choice please pick from(1-4)")
                    tries = True
                    continue

        except ValueError:
            print("Please enter a correct value! ")

def farm_mode(player_character):
    type_words("In here you can fight a goblin to gain exp!")
    type_words("A gobiln has appeared!!")
    goblin = mob_enemy.Mob_Enemy(name="goblin",hp=100,attack=20,defence=5)
    won,result = mob_battle(enemy=goblin,player_character=player_character)
    if won:
        exp = 10
        print("Hero sucessfully cleared the goblin!")
        hero_sts_upgrade(exp=exp,player_character=player_character)
        print("Hero ganied 1 level")
        save_character_data(player_character)
        print("Character save file updated sucessfully...")
        mode_selection()
    else:
        game_over()
        
def load_saved_game():
    storage = read_file_json('player_data.json')
    if ('Name' not in storage):
        game_intro()
        player_name_setup()
    else:
        print(f"Welcome back {storage['Name']}")

    try:
        player_character = load_save_character()
        print("character loaded successfully!")
    except FileNotFoundError:
        Player_class_setup()

def new_game():
    player_character = None
    storage = {}

    game_intro()
    player_name_setup()
    Player_class_setup()
    mode_selection()

def mode_selection():
    player_character = load_save_character()
    while True:
        print("======= PICK A GAME MODE=======")
        print("1. Story mode")
        print("2. Farm mode")
        print("3. Heal character")
        print("4. Exit to main menu")
        try:
            choice = int(input("Enter your choice(1-3):"))

            if choice == 1:
                story_mode()
            elif choice == 2:
                farm_mode(player_character=player_character)
            elif choice == 3:
                max_heal = 75
                if player_character.hp < max_heal:
                    player_character.hp += (max_heal - player_character.hp)
                    save_character_data(player_character=player_character)
                    print("Hero healed successfully")
                else:
                    print("Cannot heal hero now!")
            elif choice == 4:
                game_main_menu()
            else:
                print("Error pick a correct value")

        except ValueError:
            print("Enter a valid number")

def hero_sts_upgrade(exp,player_character):
    levels = exp//10
    attack = levels
    hp = 10*levels
    defence = levels

    player_character.level += levels
    player_character.attack += attack
    player_character.hp += hp
    player_character.defence += defence

def game_over():
    print("=======GAME OVER=========")
    choice_replay = input("Would you like to restart?(yes/no)").lower()
    if choice_replay == "yes":
        print("Restarting...game....")
        time.sleep(3)
        mode_selection()
    

def story_mode():
    player_character = load_save_character()
    story_dialogue = read_file_json('story_dialogues.json')
    type_words(story_dialogue['start'])
    type_words(story_dialogue['call'])
    type_words(story_dialogue['leave'])
    type_words(story_dialogue['battle'])
    mob_1 = mob_enemy.Mob_Enemy(name='dragon minnion',hp=40,attack=5,defence=5)

    won, result = mob_battle(player_character=player_character,enemy=mob_1)

    if won:
        exp = 50
        print("Hero sucessfully cleared the dragon minnion!")
        hero_sts_upgrade(exp=exp,player_character=player_character)
        print("Hero ganied 5 levels")
        save_character_data(player_character)
        print("Character save file updated sucessfully...")

    else:
        game_over()

    type_words(story_dialogue['continue'])
    type_words(story_dialogue['encounter'])
    dragon = boss_enemy.Boss_Enemy(name='dragon',hp=100,attack=15,defence=15)
    won_boss,result = boss_battle(player_character=player_character,enemy=dragon)

    if won_boss:
        exp = 100
        print("Hero sucessfully defeated the dragon!")
        hero_sts_upgrade(exp=exp,player_character=player_character)
        print("Hero ganied 10 levels")
        save_character_data(player_character)
        print("Character save file updated sucessfully...")
    else:
        game_over()
    type_words(story_dialogue['conclusion'])

def game_main_menu():
    game_running = True
    while game_running:
        print("===== WELCOME TO NEW WORLD =====")
        print("1. NEW GAME")
        print("2. CONTINUE")
        print("3. QUIT")
        print("================================")

        try:

            choice = int(input("Enter a choice(1-3):"))

            if choice == 1:      
                print("Do you want to start a new game?")
                print("Previous game data will be deleted")
                confirm = input("Enter your answer(Yes/No)").lower()

                if confirm == "yes":
                    new_game()
                elif confirm == "no":
                    print("New game was not created")
                    continue

            elif choice == 2:
                print("Loading saved data please wait..")
                time.sleep(2)
                load_saved_game()
                mode_selection()

            elif choice == 3:
                print("Exited the game successfully!")
                print("=========GOOD BYE=============")
                game_running = False
            else:
                print("Invalid choice please try again")
                continue

        except ValueError:
            print("Please enter a valid character!!")
            continue   
def main():
    game_main_menu()
main()