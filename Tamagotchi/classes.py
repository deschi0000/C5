
import time


class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.age = 1
        self.asleep = False
        self.hunger = 55
        # self.energy = 75
        self.energy = 40
        self.health = 100
        self.happiness = 90
        self.is_resting = False
        self.prompt_wakeup = False
        self.is_sick = False

        '''
        * Capable of being fed
        * Capable of being put to bed
        * Capable of going to sleep on its own, 
             losing health from hunger 
             and pooping on its own without prompting
        * Capable of aging from birth through to death
        * Capable of getting sick   ---> overfeeding / not cleaning / neglect
                    
        '''

    def put_to_bed(self):

        if self.energy + 35 < 100:
            self.energy += 35
        else:
            self.energy = 100

    def __str__(self):
        return f"\nName:{self.name}\nAge: {self.age}\nEnergy: {self.energy}\nHunger: {self.hunger}\nHealth: {self.health}\nHappiness: {self.happiness}\n"

    def intro(self):
        return f"\n{self.name}. It is {self.age} years old.\n"

    def happiness_check(self):
        # TODO
        return 0

    def neglect(self):
        self.happiness -= 5

    def lose_health(self):
        if self.health > 0:
            self.health -= 5
        else:
            self.health = 0

    def play(self):
        self.energy -= 5
        print(
            f"Wow that was a great rest! {self.name}'s energy: {self.energy}")

    def rest(self):

        self.is_resting = True          # Set the resting state to true
        if self.energy + 5 < 100:       # Hunger cannot go below 0 and rest/energy cannot go above 100
            self.energy += 5
        else:
            self.energy = 100
            self.prompt_wakeup = True

        if self.hunger + 2 < 100:       # Get hungrier, longer you sleep
            self.hunger += 2
        else:
            self.hunger = 100

        if self.happiness + 2 < 100:
            self.happiness += 2
        else:
            self.happiness = 100

        if self.health + 7 < 100:
            self.health += 7
        else:
            self.health = 100
        

        print(f"{self.name} is resting.")



    def play(self):

        if self.energy - 5 > 0:       
            self.energy -= 5
        else:
            self.energy = 0          # Tamagotchi dies?? 

        if self.hunger + 3 < 100:       
            self.hunger += 3
        else:
            self.hunger = 100

        if self.happiness + 5 < 100:
            self.happiness += 5
        else:
            self.happiness = 100


    def wake_up(self):
        self.is_resting = False
        print(f"{self.name} Woke up! Energy: {self.energy}")




    def feed(self):
        if self.hunger - 15 > 0:
            self.hunger -= 15
        else:
            self.hunger = 0

        if self.energy < 100:
            self.energy += 5
        else:
            self.energy = 100

        if self.health < 100:
            self.health += 7
        else:
            self.health = 100




