from pet import Pet

def main():
    # Create a new pet instance
    pet_name = input("Enter your pet's name: ")
    my_pet = Pet(pet_name)

    # Simulate pet activities
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()

    # Get and show the current status of the pet
    my_pet.get_status()

    # Train the pet
    my_pet.train("roll over")
    my_pet.train("play dead")

    # Show the pet's tricks
    my_pet.show_tricks()

if __name__ == "__main__":
    main()
