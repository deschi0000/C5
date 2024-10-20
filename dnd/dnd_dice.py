import random

''' 
INPUT>>>
    3d6
    4d12
    1d10
    5d4

    The first number, the number of dice to roll, can be any integer between 1 and 100, inclusive.

    The second number, the number of sides of the dice, can be any integer between 2 and 100, inclusive.
    Output:
    You should output the sum of all the rolls of that specified die, each on their own line. so if your input is "3d6", the output should look something like

    14

    Just a single number, you rolled 3 6-sided dice, and they added up to 14.   

'''
    
def dnd_dice_generator():
    print("Welcome to DND Dice ")

    # ask the user for an array of die
    dnd_die_arr = get_dice()

    # calculate the sum of the die
    # total_sum_rolled = get_sum(dnd_die_arr)
    
    # calculate and display the sums of the die
    get_sum(dnd_die_arr)

    # # display roll result:
    # print(f"The result of your rolls: {total_sum_rolled}")


def get_dice():

    dnd_die = []
    add_another_dice = True


    while add_another_dice is True:
        # error checking for die side amounts < 100
        try:
            current_dice = input ("Please enter a dnd die (i.e. 3d6): ")
            sides = int(current_dice.split("d")[1])
            
            if sides > 100:
                raise Exception
            
            dnd_die.append(current_dice)
            want_to_continue = input("Would you like add another? (y/n) ")

            if want_to_continue.lower() == "n":
                add_another_dice = False
        except:
            print("Die sides may not exceed 100")
            
        
    return dnd_die


def get_sum(dnd_die):

    # iterate through the array and calculate the roll of each die
    for i, e in enumerate(dnd_die):
        total_sum = 0
        # temp amount to hold each die roll value
        die_roll_amount = 0

        # extract the values
        index_arr = e.split("d")
        number_of_die = int(index_arr[0])
        number_of_sides = int(index_arr[1])

        # iterate through the array
        for j in range(0, number_of_die):
            die_roll_amount = random.randint(0, number_of_sides)
            total_sum += die_roll_amount

            # debug statements
            # print(index_arr)
            # print(f"number: {number_of_die}")
            # print(f"sides: {number_of_sides}")
            # print(f"die roll amount: {die_roll_amount}\n")

        print(f"{dnd_die[i]} = {total_sum}")


    return total_sum

if __name__ == "__main__":
    dnd_dice_generator()
