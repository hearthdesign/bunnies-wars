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

#        self.place_carrots()
        self.random_place_carrots()

# place carrots for pc randomly.
    def place_carrots(self, row, col):
         if (row, col) not in self.carrots and len(self.carrots) < self.num_carrots:
            self.carrots.add((row, col))
            return True
        

    def random_place_carrots(self):
        while len(self.carrots) < self.num_carrots:
            row = random.randint(0, self.size -1)
            col = random.randint(0, self.size -1)
            self.carrots.add((row, col))


    def dig(self, row: int, col: int):
        '''Digging at coordinates and check if it is carrot at this position.'''
        if not (0 <= row < self.size and 0 <= col < self.size):
            print('Oh, no! Invalid coordinates, try whithin the grid size.')
            return False
        
        if (row, col) in self.found:
            print('Already dug this spot, try another one.')
            return False
        
        self.found.add((row, col))

        if (row, col) in self.carrots:
            self.grid[row][col] = 'C'
            print("You found a carrot!")
            remaining = self.carrots_remaining()
            if remaining > 0:
                plural = "carrots" if remaining > 1 else "carrot"
                print(f"Still hiding: {remaining} {plural}")
        else:
            self.grid[row][col] = 'X'
            print('Nothing here.')
            
        return True
    

    def display(self):
        '''Display the grid and what so far has been found.'''
        print("\nField:")
        # Print column headers
        col_headers = "   " + " ".join(f"{j}" for j in range(self.size))
        # print column header
        print(col_headers)
        for i in range(self.size):
            row =[]

            for j in range(self.size):
                if (i, j) in self.found:
                    row.append(self.grid[i][j])
                else:
                    row.append('*') # Hidden tile
            # Print row number and row contents
            print(f"{i}  " + " ".join(row))
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
    print('*' * 34)
    print('***  Welcome to Bunnies Wars!  ***')
    print('*' * 34)
    # Game Instructions
    print(f'Dig to find {num_carrots} carrots in a {size}x{size} field.')
    while len(field.carrots & field.found) < num_carrots:
        field.display()
        try:      # get user imputs for coordinates
            row = int(input(f'Enter row (0 to {size - 1}): '))
            col = int(input(f'Enter column (0 to {size-1}): '))
            field.dig(row, col)
        except ValueError:
            print(f'Invalid entry, please enter only integers between 0 and {size-1}.')
    # end the game when all carrots are collected    
    print('Congratulations! You found all the carrots!')
    field.display() # print fields

#run the game
if __name__ == "__main__":
    game_loop()


