from random import randint

class Board:
    def __init__(self, size=5):
        self.size = size
        self.grid = [['O' for _ in range(size)] for _ in range(size)]
        self.ships = []

    def place_ship(self, ship):
        self.ships.append(ship)

    def print_board(self):
        for row in self.grid:
            print(" ".join(row))

    def update(self, x, y, status):
        self.grid[y][x] = status

    def display(self):
        for row in self.grid:
            print(" ".join(row))


class Ship:
    def __init__(self, length):
        self.length = length
        self.position = (0, 0)  # Initial position, can be randomized later
        self.orientation = 'h'  # 'h' for horizontal, 'v' for vertical

    def place(self, x, y, orientation):
        self.position = (x, y)
        self.orientation = orientation

    def hit(self, x, y):
        ship_x, ship_y = self.position
        if self.orientation == 'h':
            return ship_x <= x < ship_x + self.length and ship_y == y
        elif self.orientation == 'v':
            return ship_y <= y < ship_y + self.length and ship_x == x

    def reduce_length(self):
        self.length -= 1


class BattleshipGame:
    def __init__(self):
        self.board = Board()
        self.player_ship = Ship(3)  # Length of the ship
        self.enemy_ship = Ship(3)   # Length of the enemy ship
        self.place_ships()

    def place_ships(self):
        # Place player ship
        print("Placing your ship...")
        self.place_ship(self.player_ship)

        # Place enemy ship
        print("Placing enemy ship...")
        self.place_ship(self.enemy_ship)

    def place_ship(self, ship):
        # Randomly place ship on the board
        x = randint(0, self.board.size - 1)
        y = randint(0, self.board.size - 1)
        orientation = 'h' if randint(0, 1) == 0 else 'v'
        ship.place(x, y, orientation)
        self.board.place_ship(ship)

    def player_turn(self, x, y):
        if self.enemy_ship.hit(x, y):
            print("You hit the enemy ship!")
            self.enemy_ship.reduce_length()
            self.board.update(x, y, 'X')  # Mark hit on the board
        else:
            print("You missed!")
            self.board.update(x, y, '-')  # Mark miss on the board

    def enemy_turn(self):
        # Simulate enemy's turn, randomly selecting coordinates
        x = randint(0, self.board.size - 1)
        y = randint(0, self.board.size - 1)
        if self.player_ship.hit(x, y):
            print("Enemy hit your ship!")
            self.player_ship.reduce_length()
            self.board.update(x, y, 'X')  # Mark hit on the board
        else:
            print("Enemy missed!")
            self.board.update(x, y, '-')  # Mark miss on the board

    def play(self):
        print("Let's play Battleship!")
        while True:
            print("\nYour board:")
            self.board.display()
            print("\nEnter coordinates to attack (x, y):")
            x = int(input("Enter x coordinate: "))
            y = int(input("Enter y coordinate: "))
            self.player_turn(x, y)

            # Check if player won
            if self.enemy_ship.length == 0:
                print("Congratulations! You sank the enemy ship. You win!")
                break

            # Enemy's turn
            self.enemy_turn()

            # Check if enemy won
            if self.player_ship.length == 0:
                print("Oh no! The enemy sank your ship. You lose!")
                break

# Start the game
if __name__ == "__main__":
    game = BattleshipGame()
    game.play()
