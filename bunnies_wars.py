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
        self.grid: list[list[str]] = [['*' for _ in range(size)] for _ in range(size)]
        self.size: int = size # sizes of a squared grid (x*x)
        self.num_carrots: int = num_carrots #hidden carrots (int)

        self.carrots: set[tuple[int, int]] = set()
        self.found: set[tuple[int, int]] = set()

        self.place_carrots()


# place carrots for pc randomly.
    def place_carrots(self):
        while len(self.carrots) < self.num_carrots:
            x = random.randint(0, self.size -1)
            y = random.randint(0, self.size -1)
            self.carrots.add((x, y))


    def dig(self, x: int, y: int):
        '''Digging at coordinates (x, y) and check if it is carrot at this position.'''
        if not (0 <= x < self.size and 0 <= y < self.size):
            print('Oh, no! Invalid coordinates, try whithin the grid size.')
            return False
        
        if (x, y) in self.found:
            print('Already dug this spot, try another one.')
            return False
        
        self.found.add((x, y))

        if (x, y) in self.carrots:
            self.grid[x][y] = 'C'
            print("You found a carrot!")
        else:
            self.grid[x][y] = 'X'
            print('Nothing here.')
        return True
    

    def display(self):
        '''Display the grid and what so far has been found.'''
        print("\nField:")
        for i in range(self.size):
            row =[]
            for j in range(self.size):
                if (i, j) in self.found:
                    row.append(self.grid[i][j])
                else:
                    row.append('*')
            print(' '.join(row))
        print()

    def carrots_remaining(self):
        '''Returns the amount of carrots to be found.'''
        return len(self.carrots - self.found)    

# Game loop
def game_loop():
    size: int = 5
    num_carrots: int = 6
    field = Field(size, num_carrots)
    player_name()
    # Game Introduction and description
    print('As often in life is the case, "The grass on the other side of the fence is greener". In this case, is the field of your opponent, the PC-Bunny, greener.')
    print('Try to find all the carrots that have been planted by the PC-Bunny: enter the coordinates (x, y) to check each position ...in the mean time, the PC-Bunny had a similar idea and is digging the carrots you planted.')
    print('The game ends when all the carrots are found. Try to find them all! (...before the PC-Bunny') 
    print('Good Luck!\n')
    # Game Title
    print('*' * 50)
    print('*** Welcome to Bunnies Wars! ***')
    print('*' * 50)
    # Game Instructions
    print(f'Dig to find {num_carrots} carrots in a {size}x{size} field.')
    while len(field.carrots & field.found) < num_carrots:
        field.display()
        try:      # get user imputs for coordinates
            x = int(input(f'Enter row (0 to {size - 1}): '))
            y = int(input(f'Enter column (0 to {size-1}): '))
            field.dig(x, y)
        except ValueError:
            print(f'Invalid entry, please enter only integers between 0 and {size-1}.')
    # end the game when all carrots are collected    
    print('Congratulations! You found all the carrots!')
    field.display() # print fields

#run the game
if __name__ == "__main__":
    game_loop()


