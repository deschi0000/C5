class Tamagotchi:
    def __init__(self, name):
        self.name = name
        self.age = 1
        self.asleep = False
        self.energy = 75
        self.health = 100
        self.happiness = 90
        self.hunger = 10
        self.is_resting = False

        '''
        * Capable of being fed
        * Capable of being put to bed
        * Capable of going to sleep on its own, 
             losing health from hunger 
             and pooping on its own without prompting
        * Capable of aging from birth through to death
                    
        '''

    def put_to_bed(self):

        if self.energy + 35 < 100:
            self.energy += 35
        else:
            self.energy = 100

    def __str__(self):
        return f"\nName:{self.name}\nAge: {self.age}\nEnergy: {self.energy}\nHealth: {self.health}\nHappiness: {self.happiness}\n"

    def intro(self):
        return f"\n{self.name}. It is {self.age} years old.\n"

    def happiness_check(self):
        # TODO
        return 0

    def neglect(self):
        self.happiness -= 5

    def play(self):
        self.energy -= 5
        print(
            f"Wow that was a great rest! {self.name}'s energy: {self.energy}")

    def rest(self):

        # if self.asleep:
        #     print(f"{self.name} already sleeping!")
        # else:
        #     self.asleep = True
        #     print("Your Pet is now sleeping")

        if self.is_resting == True:

            if self.energy + 5 < 100:       # Hunger cannot go below 0 and rest/energy cannot go above 100
                self.energy += 5
            else:
                self.energy = 100

            if self.hunger + 2 < 100:
                self.hunger += 2
            else:
                self.hunger = 100

            print(f"{self.name} is resting. It's energy is: {self.energy}")

        elif self.is_resting == False:
            print(
                f"Wow that was a great rest! {self.name}'s energy: {self.energy}")

    def feed(self):
        # HUNGER CANNOT GO BELOW O
        return 0
