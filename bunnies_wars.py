import random

# input player name print welcome message

def player_name():
    name= input('Enter your name: ').strip()
    if not name:
        name= 'Bunny One'
        print(f'\n Welcome {name} to the Bunnies Wars game!\n')
        return name

# Class Field (self, size, num_carrots).
# create 2 field for user and computer with a given size and number of carrots.
class Field:
    '''Initialize the field with a grid and place carrots.'''
    def __init__(self, size: int, num_carrots: int):
        self.grid: set[tuple[int, int]] = [['*'] for _ in range(size)]
        self.size: int = size # size (int) of the grid (x*x)
        self.num_carrots: int = num_carrots #hidden carrots (int)

        self.carrots: set[tuple[int, int]] = set()
        self.found: set[tuple[int, int]] = set()

        self.place_carrots()

# place carrots for pc randomly.
    def place_carrots(self):
        while len(self.carrots) < self.num_carrots:
            x = random.randint(0, self.size -1)
            y = random.randint(0, self size -1)
            self.carrots.add((x, y))

    




# begin game loop 
# dig to collect carrots in turns (player 1, PC)
# check results,
#  track scores 
# print fields
# end the game when all carrots are collected
