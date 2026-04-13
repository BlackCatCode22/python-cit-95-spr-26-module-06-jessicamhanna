# sampleClass.py
# Demonstrates the basic creation of a class (template) and an object (instance of the class)

class PartyAnimal:
    # Constructor: runs automatically when an object is created
    def __init__(self):
        self.x = 0  # Instance variable to track party count

    # Method: a function that belongs to the class
    def party(self):
        self.x = self.x + 1  # Increment the party count
        print("So far", self.x)

# Create an instance (object) of the PartyAnimal class
an = PartyAnimal()

# Call the party method three times on the object
an.party()
an.party()
an.party()