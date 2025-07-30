import random


# input player name print welcome message
def player_name():
    name = input('Enter your name: ').strip()
    if not name:
        name = 'Bunny One'
    print(f'\n Welcome {name} to the Bunnies Wars game!\n')
    return name


# Class Field (self, size, num_carrots).
class Field:
    def __init__(self, size: int, num_carrots: int):
        self.grid: list[list[str]] = [
            ['🍀'for _ in range(size)]for _ in range(size)
            ]
        self.size: int = size  # sizes of a squared grid (x*x)
        self.num_carrots: int = num_carrots  # hidden carrots (int)
        self.carrots: set[tuple[int, int]] = set()
        self.found: set[tuple[int, int]] = set()
        self.random_place_carrots()

    # ensures no duplicates to random_place_carrots 
    def no_repeat_carrots(self, row, col):
        if (
            (row, col) not in self.carrots and
                len(self.carrots) < self.num_carrots
        ):
            self.carrots.add((row, col))
            return True
        return False
    
    '''Randomly place carrots on the field.'''
    def random_place_carrots(self):
        while len(self.carrots) < self.num_carrots:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            self.no_repeat_carrots((row, col))

    '''Digging at coordinates'''
    def dig(self, row: int, col: int, silent = False):
        if not (
            0 <= row < self.size and 0 <= col < self.size
        ):
            print('Oh, no! Invalid coordinates,\n try whithin the grid size.')
            return False
        # Check if the position was already dug
        if (row, col) in self.found:
            print('Already dug this spot,\n try another one.')
            return False
        # Mark the position if the carrot is found
        self.found.add((row, col))
        if (row, col) in self.carrots:
            self.grid[row][col] = '🥕'
            if not silent:
                print("You found a carrot!")
                # message with remaining carrots adjusting case for plural
                remaining = self.carrots_remaining()
                if remaining > 0:
                    plural = "carrots" if remaining > 1 else "carrot"
                    print(f"Still hiding: {remaining} {plural}")
            return True
        else:
            # Mark the position as dug
            self.grid[row][col] = '🕳️ '
            print('Nothing here.')
        return False

    '''Display the field with discovered tiles'''
    def display(self):
        print("\nField:")
        # define and print column headers
        col_headers = "   " + " ".join(f" {j}"
                                       for j in range(self.size))
        print((col_headers)+"\n")
        # print each row with an index number
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if (i, j) in self.found:
                    row.append(self.grid[i][j])
                else:
                    row.append('🍀')  # Hiding tile
            # Print row number and row contents
            print(f"{i}  " + " ".join(row))
        print()
        
    '''Amount of carrots to be found.'''
    def carrots_remaining(self):
        return len(self.carrots - self.found)

# Game class that handles full game logic
class Game:
    def __init__(self):
        # Size and carrot count options
        self.size_options = {1: (4, 4), 2: (6, 9), 3: (8, 15)}


    # Set the size of the field and the number of carrots
    def setup_game(self):
        print("Choose field size:\n1. 4x4\n2. 6x6\n3. 8x8")
        while True:
            try:
                choice = int(input("Enter choice (1-3): "))
                if choice in self.size_options:
                    self.size, self.num_carrots = self.size_options[choice]
                    break
            except ValueError:
                pass
            print("Invalid choice. Please enter 1, 2, or 3.")

    # Game loop Function
    def game_loop(self):
        self.setup_game()
        # Carrots hidden by PC (player digs here)
        self.your_field = Field(self.size, self.num_carrots)
        # Carrots hidden by player (PC digs here)
        self.pc_field = Field(self.size, self.num_carrots)
        player_score = 0
        pc_score = 0
        name = player_name()

        # Game Introduction and description
        print('The grass is always greener on the other side...')
        print('Try to dig up all the carrots hidden by the PC-Bunny!')
        print('Meanwhile, the PC-Bunny is digging up your carrots...')
        print('First to find all carrots wins!\n')
        print('Good Luck!\n')
        # Game Title
        print('*' * 38)
        print('*****  Welcome to Bunnies Wars!  *****')
        print(f'🐰🐰🐰 * {name} * vs * PC-Bunny * 🐰🐰🐰')
        print('*' * 38)
        # Game Instructions
        print(f'Dig to find {self.num_carrots} carrots in a\n'
              f'{self.size}x{self.size} field.')
        # Game loop until all the carrots are found
        while player_score < self.num_carrots and pc_score < self.num_carrots:
            # --- Player Turn ---
            self.your_field.display()
            try:      # get user imputs for coordinates
                row = int(input("Your turn! Enter row: "))
                col = int(input("Enter column: "))
                if self.your_field.dig(row, col):
                    if (row, col) in self.your_field.carrots:
                        player_score += 1
            except ValueError:
                print(f'Invalid entry, please enter only integers\n'
                      f'between 0 and {self.size-1}.')

            # --- PC Turn ---
            print("PC-Bunny is digging...")

            while True:
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - 1)
                if (row, col) not in self.pc_field.found:
                    break
            if self.pc_field.dig(row, col):
                # if (row, col) in pc_field.carrots:
                pc_score += 1
                self.pc_field.grid[row][col] = '🥕'
                print("PC-Bunny found a carrot!\n")
            else:
                self.pc_field.grid[row][col] = '🕳️ '
                print("PC-Bunny found nothing.\n")

            # --- Score Update ---
            print(f"Scores — You: {player_score}  |  PC Bunny: {pc_score}")

        # --- Game Over ---
        print("\nGame Over!")
        if player_score == self.num_carrots:
            print('⭐'*23)
            print(f"\n⭐⭐⭐  {name}, you won the Bunny War!   ⭐⭐⭐")
            print('⭐'*23)
        else:
            print('💀'*25)
            print('💀  The PC Bunny won... Better luck next time!  💀')
            print('💀'*25)

        print("🐰 Your field:")
        self.pc_field.display()
        print("👾 PC-Bunny's field:")
        self.your_field.display()


# Run the game
if __name__ == "__main__":
    game = Game()
    game.game_loop()
