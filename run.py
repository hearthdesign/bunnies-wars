import random


# input player name print welcome message
def player_name():
    name = input('Enter your name:\n').strip()
    if not name:
        name = 'Bunny One'
    print(f'\n Welcome {name} to the Bunnies Wars game!\n')
    return name


# Class Field (self, size, num_carrots).
class Field:
    def __init__(self, size: int, num_carrots: int):
        self.grid: list[list[str]] = [
            ['🍀 'for _ in range(size)]for _ in range(size)
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
            self.no_repeat_carrots(row, col)

    '''Digging at coordinates'''
    def dig(self, row: int, col: int, silent=False):
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
            self.grid[row][col] = '🥕 '
            if not silent:
                print("You found a carrot!\n")
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
        # print("Your Field: ")
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
                    row.append('🍀 ')  # Hiding tile
            # Print row number and row contents
            print(f"{i}  " + " ".join(row))
        print()

    '''Amount of carrots to be found.'''
    def carrots_remaining(self):
        return len(self.carrots - self.found)


# Game class that handles full game logic
class Game:
    def __init__(self):
        # Size and carrot count options (size and num of carrots)
        self.size_options = {1: (4, 4), 2: (6, 9), 3: (8, 15)}
        self.your_field = None  # Player's field
        self.pc_field = None  # PC's field

    # Player sets the size of the field and (established) the number of carrots
    def setup_game(self):
        print("Choose field size:\n1. 4x4\n2. 6x6\n3. 8x8")
        while True:
            try:
                choice = int(input("Enter choice (1-3):\n"))
                if choice in self.size_options:
                    return self.size_options[choice]  # Return selected option
            except ValueError:
                pass
            print("Invalid choice. Please enter 1, 2, or 3.")

    # Game Introduction, rules and welcome message
    def print_intro(self, name, size, num_carrots):
        print('The grass is always greener on the other side...')
        print('Try to dig up all the carrots hidden by the PC-Bunny!')
        print('Meanwhile, the PC-Bunny is digging up your carrots...')
        print('First to find all carrots wins!\n')
        print('Good Luck!\n')
        # Game Title
        print('🐰' * 36)
        print('🐰🐰*** Welcome to Bunnies Wars! ***🐰🐰')
        print('🐰🐰🐰🐰 * {} * vs * PC-Bunny * 🐰🐰🐰🐰'.format(name))
        print('🐰' * 36)
        # Game Instructions
        print(f'\nDig to find {num_carrots} carrots in a\n'
              f'{size}x{size} field.\n')

    # --- Player Turn ---
    def player_turn(self, field):
        print("🐰 Your Field: 🐰")
        field.display()
        try:
            row = int(input("Your turn! Enter row:\n"))
            col = int(input("Enter column:\n"))
            return 1 if field.dig(row, col) else 0  # Return score increment
        except ValueError:
            print(f'Invalid entry, please enter only integers between 0 and'
                  f'{field.size - 1}.')
            return 0

    # PC's digging turn
    def pc_turn(self, field):
        print("\nPC-Bunny is digging...")
        while True:
            row = random.randint(0, field.size - 1)
            col = random.randint(0, field.size - 1)
            if (row, col) not in field.found:
                break  # Ensure PC doesn’t dig same spot
        found = field.dig(row, col, silent=True)
        print("\n👾 PC-Bunny Field: 👾")
        field.display()
        if found:
            print("PC-Bunny found a carrot!\n")
            return 1
        else:
            print("PC-Bunny found nothing.\n")
            return 0

    # Show current scores
    def print_scores(self, player_score, pc_score):
        print(f"Scores — You: {player_score} | PC Bunny: {pc_score}\n")

    # --- Game Over and winner message---
    def print_game_result(self, name, player_score, pc_score, num_carrots):
        print("\nGame Over!")
        if player_score == num_carrots:
            print('⭐'*42)
            print(f"⭐⭐⭐  {name}, you won the Bunny War!   ⭐⭐⭐")
            print('⭐'*42)
            print()
        else:
            print('💀'*48)
            print('💀  The PC Bunny won... Better luck next time!  💀')
            print('💀'*48)
            print()

    def reveal_fields(self, your_field, pc_field):
        print("👾 PC-Bunny's field: 👾")
        pc_field.display()
        print("🐰 Your Field: 🐰")
        your_field.display()

    # Game loop (main logic)
    def game_loop(self):
        size, num_carrots = self.setup_game()
        name = player_name()
        self.print_intro(name, size, num_carrots)
        # Carrots hidden (random funtion) "by the PC" (player digs here)
        your_field = Field(size, num_carrots)
        # Carrots hidden (random funtion) "by player" (PC digs here)
        pc_field = Field(size, num_carrots)
        player_score = 0
        pc_score = 0
        # Continue game until one finds all carrots
        while player_score < num_carrots and pc_score < num_carrots:
            player_score += self.player_turn(your_field)
            pc_score += self.pc_turn(pc_field)
            self.print_scores(player_score, pc_score)

        # Final messages
        self.print_game_result(name, player_score, pc_score, num_carrots)
        self.reveal_fields(your_field, pc_field)


# Run the game
if __name__ == "__main__":
    Game().game_loop()
