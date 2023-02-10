import time
from classes import *
from functions import *

import os      # Clear the cmd line
import time    # Show messages this way?


#/==========================================================

MAX_AGE = 10
skips = 0
is_resting = False

#/==========================================================
# INTRO / CREATION

print("Welcome to Tamagotchi")
print("Hey Guy, Let's create your new Friend!")

t1 = create_tamagotchi()
print("Congratulations on your new pet!")
print(t1)

press_enter()


#/==========================================================



while t1.age < MAX_AGE:

    # TODO prompt for commands...
    # TODO after commands, lower food, raise poop, start neglect counter

    print(f"DAY {t1.age}")
    for i in range(0,3):    # Morning, Day and Night

        # if i > 0:
        #     os.system("cls")

        #/==========================================================
        # COMMANDLIST
        print(time_of_day_message(i))
        print(t1)
        print("COMMANDS")

        #TODO error handling for incorrect input

        if t1.is_resting is False:
            command = input("Feed [f]  |  Rest [r]  |  Do Nothing [n]\n")
        elif t1.is_resting is True:
            command = input("Feed [f]  |  Wake Up [w]  |  Do Nothing [n]\n")


        #TODO Perhaps move all these checks into their own functions?

        if is_resting == True:
            t1.rest()                   # Continue Resting

        if is_resting == True and t1.energy == 100:     # if energy is 100 and resting, it has to wake up
            is_resting = False                          # energy and not resting, might just of ate a snack?
            t1.wake_up()                                



        if command == "r":              # Rest
            
            is_resting = True
            t1.rest() 
            
        if command == "w":              # Wake up
            
            is_resting = False
            t1.wake_up()


        if command == "n":
            t1.neglect()
        
        
        os.system("cls")



    #  END OF DAY -> get full rest + Increment Age
    
    t1.age += 1
    print(t1)

    os.system("cls")




    # print("COMMANDS = feed[f]")
    # time.sleep(5)s
    # t1.put_to_bed()

print(f"{t1} has died of old age")


    


