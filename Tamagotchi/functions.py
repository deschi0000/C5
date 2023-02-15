from classes import Tamagotchi
from random import choice

import os      # Clear the cmd line
import time


FOOD = ["Croissant", "Cake", "Manju", "Pasta", "Lobster Claw", "Risotto", "Gua bao"]
MAX_AGE = 10
AWAKE_COMMANDS = []
ASLEEP_COMMANDS = []


def create_tamagotchi():
    '''
    This will create a tamagotchi object
    '''

    name = ""
    while len(name) == 0:
        
        name = input("What would you like to call your pet?: ")
        if len(name.strip()) == 0:
            print("Please enter some values")       
            name = ""
      
        return Tamagotchi(name)
    
def time_of_day_message(num):
    if num == 0:
        return "Good Morning!\n"
    elif num == 1:
        return "Lunchtime!\n"
    else:
        return "Eveningtime\n"

def press_enter():
    # enter_pressed = False
    userinput = input("Press Enter to Continue")
    if userinput == "":
        os.system("cls")
        # enter_pressed = True



def rest_check(object, is_sleep, energy):

    if is_sleep == True and energy == 100:                # Fully rested, wake up
        return object.wake_up()
    elif is_sleep == False and energy == 100:             # No need to sleep
        return f"\n{object.name} is fully rested!"
    elif is_sleep == True and energy < 100:               # Keep resting
        return object.rest()
    elif is_sleep == True and object.prompt_wakeup() == True:
        object.prompt_wakeup = False
        return object.wake_up()

#/==========================================================
# Checks Energy / Hunger / Age

def energy_check(energy, object):
    # include object? Maybe if the energy is zero, invoke kill function.
    if energy < 15:
        warning("extreme_energy", object)
    elif energy < 30:
        warning("energy", object)


def hunger_check(hunger, object):
    if hunger > 75:
        object.lose_health()
        warning("extreme_hunger", object)
    elif hunger > 45:
        object.lose_health()
        warning("hunger", object)


def age_check(age, object):
    if age == MAX_AGE:
        object.is_alive = False
        print(f"\n{object.name} has died of old age")
        print("              ")
        print("              ")
        print("              ")
        print("              ")


def stomach_check(stomach, object):
    if object.just_pooed == True:
        object.is_holding == 0
    elif object.just_pooed == False and object.holding > 5:
        print(f"{object.name} Pooed!")
        object.poo()
    else:
        object.holding += 1



#/==========================================================



def warning(type, object):
    if type == "energy":
        print(f"{object.name}'s is getting tired!")
    if type == "extreme_energy":
        print(f"!Careful! {object.name}'s is getting extremely tired!")
    if type == "hunger" and object.is_resting == False:
        print(f"{object.name} is hungry!")        
    if type == "extreme_hunger" and object.is_resting == False:
        print(f"!Careful! {object.name} is getting really hungry!")


def command_menu(object):
    if object.is_resting is False and object.energy == 100:
        return input("Feed [f]  |  Do Nothing [n]\n")
    elif object.is_resting is False and object.just_pooed == True:
        return input("Feed [f]  |  Rest [r]  | Play [p] | Poo(u) | Do Nothing [n]\n")
    elif object.is_resting is False:
        return input("Feed [f]  |  Rest [r]  | Play [p] | Poo(u) | Clean [c] | Do Nothing [n]\n")

    elif object.is_resting is True:
        return input("Feed [f]  |  Wake Up [w]  |  Do Nothing [n]\n")

def food_message(object):
    print(f"{object.name} enjoyed eating {choice(FOOD)}")


def final_stats(max_age, is_alive, object):
    if max_age == 2:
        print(f"{object.name} has died of old age")
    if is_alive == False:
        print(f"{object.name} has died of neglect")
        







def intro_logo():
        print("Welcome To:")
        print(" ______   ____  ___ ___   ____   ____   ___   ______   __  __ __  ____ ")
        print("|      | /    ||   |   | /    | /    | /   \ |      | /  ]|  |  ||    |")
        print("|      ||  o  || _   _ ||  o  ||   __||     ||      |/  / |  |  | |  | ")
        print("|_|  |_||     ||  \_/  ||     ||  |  ||  O  ||_|  |_/  /  |  _  | |  |")
        print("  |  |  |  _  ||   |   ||  _  ||  |_ ||     |  |  |/   \_ |  |  | |  |")
        print("  |  |  |  |  ||   |   ||  |  ||     ||     |  |  |\     ||  |  | |  |")
        print("  |__|  |__|__||___|___||__|__||___,_| \___/   |__| \____||__|__||____|")
        print("  (By Dave)")
        time.sleep(5)
        os.system("cls")




