class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Default hunger level (0 = full, 10 = very hungry)
        self.energy = 5  # Default energy level (0 = tired, 10 = fully rested)
        self.happiness = 5  # Default happiness level (0 = sad, 10 = very happy)
        self.tricks = []  # List to store learned tricks

    def eat(self):
        # Decrease hunger by 3 but not below 0, and increase happiness by 1
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating...")

    def sleep(self):
        # Increase energy by 5 but not above 10
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping...")

    def play(self):
        # Decrease energy by 2, increase happiness by 2, and increase hunger by 1
        if self.energy >= 2:
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} is playing...")
        else:
            print(f"{self.name} is too tired to play.")

    def get_status(self):
        # Print the current state of the pet
        print(f"{self.name}'s current status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Tricks: {self.tricks}")

    def train(self, trick):
        # Adds a new trick to the list of learned tricks
        self.tricks.append(trick)
        print(f"{self.name} has learned a new trick: {trick}")

    def show_tricks(self):
        # Prints all the tricks learned by the pet
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

