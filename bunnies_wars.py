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


    def dig(self, x: int, y: int):
        '''Digging at coordinates (x, y) and check if it is carrot at this position.'''
        if not (0 <= x < self.size and 0 <= y < self.size):
            print("Oh, no! Invalid coordinates, try whithin the grid size.")
            return False
        
        if (x, y) in self.found:
            print("Already dug this spot, try another one.")
            return False
        
        self.found.add((x, y))

        if (x, y) in self.carrots:
            self.grid[x][y] = 'C'
            print("You found a carrot!")
        else:
            self.grid[x][y] = 'X'
            print("Nothing here.")
        return True
    

    def display(self):
        '''Display the grid and what so far has been found.'''
        print("\nField:")
        for i in range(self.size):
            row =[]
            for j in range(self.size):
                if (i, j) in self.founds:
                    row.append(self.grid[i][j])
                else:
                    row.append('*')
            print(' '.join(row))
        print()

    def carrots_remaining(self):
        '''Returns the amount of carrots to be found.'''
        return len(self.carrots - self.founds)    

# begin game loop 
# dig to collect carrots in turns (player 1, PC)
# check results,
#  track scores 
# print fields
# end the game when all carrots are collected
