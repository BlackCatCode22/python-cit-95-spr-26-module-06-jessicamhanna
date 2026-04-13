# inheritance.py
# Demonstrates inheritance: extending a parent class to create a child class
# that inherits all parent capabilities and adds its own

# Parent class
class PartyAnimal:
    # Constructor: accepts a name and initializes the party count
    def __init__(self, nam):
        self.x = 0        # Party count
        self.name = nam   # Store the name passed in
        print(self.name, "constructed")

    # Method: increments the party count and prints it
    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

# Child class: inherits from PartyAnimal and adds football-specific behavior
class FootballFan(PartyAnimal):
    # Constructor: calls the parent constructor, then adds a points tracker
    def __init__(self, nam):
        super().__init__(nam)  # Call PartyAnimal's __init__ to reuse its setup
        self.points = 0        # Additional attribute unique to FootballFan

    # New method specific to FootballFan
    def touchdown(self):
        self.points = self.points + 7  # Add 7 points for a touchdown
        self.party()                   # Reuse the inherited party() method
        print(self.name, "points", self.points)

# Create a PartyAnimal instance and call party()
s = PartyAnimal("Sally")
s.party()

# Create a FootballFan instance (child class) and call both inherited and new methods
j = FootballFan("Jim")
j.party()       # Inherited from PartyAnimal
j.touchdown()   # Defined in FootballFan