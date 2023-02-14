from classes import Tamagotchi
from random import choice

import os      # Clear the cmd line
import time


FOOD = ["Croissant", "Cake", "Manju", "Pasta", "Lobster Claw", "Risotto", "Gua bao"]




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
    elif is_sleep == False and energy == 100:         # No need to sleep
        return f"\n{object.name} is fully rested!"
    elif is_sleep == True and energy < 100:         # Keep resting
        return object.rest()
    elif is_sleep == True and object.prompt_wakeup() == True:
        object.prompt_wakeup = False
        return object.wake_up()

def energy_check(energy, object):
    # include object? Maybe if the energy is zero, invoke kill function.
    if energy < 30:
        warning("energy", object)

def hunger_check(hunger, object):
    if hunger > 60:
        object.lose_health()
        warning("hunger", object)




def warning(type, object):
    if type == "energy":
        print(f"!Careful! {object.name}'s energy levels are")
    if type == "hunger":
        print(f"!Careful! {object.name} is hungry!")


def command_menu(object):
    if object.is_resting is False and object.energy == 100:
        return input("Feed [f]  |  Do Nothing [n]\n")
    elif object.is_resting is False:
        return input("Feed [f]  |  Rest [r]  | Play [p] | Do Nothing [n]\n")
    elif object.is_resting is True:
        return input("Feed [f]  |  Wake Up [w]  |  Do Nothing [n]\n")

def food_message(object):
    print(f"{object.name} enjoyed eating {choice(FOOD)}")









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
