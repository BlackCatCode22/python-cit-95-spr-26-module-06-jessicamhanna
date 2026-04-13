# lifecycle.py
# Demonstrates the object lifecycle using a constructor (__init__) and destructor (__del__)

class PartyAnimal:
    # Constructor: called when the object is created
    def __init__(self):
        self.x = 0  # Initialize party count to zero
        print('I am constructed')

    # Method: increments the party count and prints the current value
    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

    # Destructor: called automatically when the object is destroyed or goes out of scope
    def __del__(self):
        print('I am destructed', self.x)

# Create an instance of PartyAnimal — triggers __init__
an = PartyAnimal()
an.party()
an.party()

# Reassigning 'an' to an integer destroys the PartyAnimal object — triggers __del__
an = 42
print('an contains', an)