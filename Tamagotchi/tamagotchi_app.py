import time
from classes import *
from functions import *

import os      # Clear the cmd line





#/==========================================================
# Constants
# MAX_AGE = 100
MAX_AGE = 2
skips = 0

# is_resting = False      #  Not working??

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
    # TODO 
    print(f"DAY {t1.age}")
    for i in range(0,3):    # Morning, Day and Night

        #/==========================================================
        # COMMANDLIST
        print(time_of_day_message(i))
        print(t1)
        print("COMMANDS")

        
        # print("Feed [f]  |  Put To Sleep [s]")
        if t1.is_resting is False:
            command = input("Feed [f]  |  Rest [r]  |  Do Nothing [n]\n")
        elif t1.is_resting is True:
            command = input("Feed [f]  |  Wake Up [w]  |  Do Nothing [n]\n")

        # print(command.lower())
        

        # TODO the resting bit
        if command == "r":
            t1.is_resting == True
            t1.rest() 
            
        if command == "w":
            t1.is_resting == False
            print(f"{t1.name} woke up. It's energy is: {t1.energy}")


        if command == "n":
            t1.neglect()
        
        # os.system("cls")




    #  END OF DAY -> get full rest + Increment Age
    
    t1.age += 1
    print(t1)

    os.system("cls")




    # print("COMMANDS = feed[f]")
    # time.sleep(5)s
    # t1.put_to_bed()

print(f"{t1} has died of old age")


    


