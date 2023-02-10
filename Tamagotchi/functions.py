from classes import Tamagotchi

import os      # Clear the cmd line


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
    enter_pressed = False
    userinput = input("Press Enter to Continue Buddeh")
    if userinput == "":
        os.system("cls")
        enter_pressed = True

