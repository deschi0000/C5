import time
from classes import *
from functions import *

import os      # Clear the cmd line
import time    # Show messages this way?


#/==========================================================

# MAX_AGE = 10
skips = 0
is_resting = False
just_pooed = False
command_keys = ["f", "r", "w", "p", "n"]

#/==========================================================
# INTRO / CREATION

# print("Welcome to Tamagotchi")
# intro_logo()
# print("Hey Guy, Let's create your new Friend!")
# t1 = create_tamagotchi()
t1 = Tamagotchi("DK")
print("Congratulations on your new pet!")
print(t1)

press_enter()


#/==========================================================



# while t1.age < MAX_AGE:
while t1.is_alive:

    # TODO prompt for commands...
    # TODO after commands, lower food, raise poop, start neglect counter

    # print(f"DAY {t1.age}")
    for i in range(0,3):    # Morning, Day and Night


        #/==========================================================
        # COMMANDLIST
        print(f"DAY {t1.age}")
        print(time_of_day_message(i))
        print("==================================")

        print(t1)
        print("COMMANDS")



       
        
        command = command_menu(t1)
        os.system("cls")                # Do we like clearing the menu? less confusing?

        if command == "f":
            t1.feed()
            food_message(t1)


        if command == "r":                           # Rest
            if t1.energy == 100:
                print(f"{t1.name} is fully rested!")
            else:
                is_resting = True
                rest_check(t1, is_resting, t1.energy) 
            
        if command == "w":                           # Wake up
            
            is_resting = False
            t1.wake_up()

        if command == "p":                          # Play
            t1.play()
            print(f"{t1.name} is having fun playing!")

        if command == "u":                          #Poo
            t1.poo()
            t1.just_pooed = True
            print(f"{t1.name} feels relieved!")

            # prompt to clean up?

        if command == "c":
            t1.clean()



        if command == "n" or command == "":         # Do Nothing
            rest_check(t1, is_resting, t1.energy)
            if is_resting is False:
                t1.neglect()
        


        #/==========================================================
        # CHECKS!
        energy_check(t1.energy, t1)
        hunger_check(t1.hunger, t1)
        age_check(t1.age, t1)
        stomach_check(t1.stomach, t1)

        # os.system("cls")
        press_enter()


    #  END OF DAY -> get full rest + Increment Age
    
    print(f"END OF DAY {t1.age}")
    print(f"This is {t1.name}'s Stats for today")
    print("==================================")
    print(t1)
    print("==================================")
    t1.age += 1

    # os.system("cls")
    press_enter()




    # print("COMMANDS = feed[f]")
    # time.sleep(5)s
    # t1.put_to_bed()

# print(f"{t1} has died of old age")


    





'''
Check rest






'''
