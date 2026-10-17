# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 10:31:09 2025

@author: ROPAFADZOCHELSEAMUDA
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 10:31:09 2025

@author: ROPAFADZOCHELSEAMUDA
"""

import random

# The  board game_ display of the rows and columns  
class Board:
    def __init__(self):
        #creating my 3 x 3 grid fill with empty spaces
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def display(self):
#Displaying my game board with labels and borders do that users know where to move        
        print("\n     1     2     3")
        print("   +-----+-----+-----+")
        rows = ['A', 'B', 'C'] #Using leters for rows
        for i in range(3):
            row_display = f" {rows[i]} |"
            for j in range(3):
                cell_value = self.grid[i][j]
                row_display += f"  {cell_value}  |"
            print(row_display)
            print("   +-----+-----+-----+")
        print()  # Blank line for spacing

    def make_move(self, position, symbol):
        mapping = {'A': 0, 'B': 1, 'C': 2}
        try:
            row = mapping.get(position[0].upper(), -1)
            col = int(position[1]) - 1
        except (KeyError, ValueError, IndexError):
            return False

    #Ensure we dont move outside the board
        if row not in range(3) or col not in range(3):
            return False

#only  allows moves into empty blocks 
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def is_full(self): #Checks if every single spot is taken on the board
        return all(cell != " " for row in self.grid for cell in row)

    def check_winner(self, symbol):
        g = self.grid
        
        # Look for three in a row - horizontally or vertically
        for i in range(3):
            if all(g[i][j] == symbol for j in range(3)) or all(g[j][i] == symbol for j in range(3)):
                return True
            
        # Check diagonals
        if g[0][0] == g[1][1] == g[2][2] == symbol or g[0][2] == g[1][1] == g[2][0] == symbol:
            return True
        return False

    def reset(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]


# Represents each player in the game
class Player:
    def __init__(self, name, symbol, is_computer=False):
        self.name = name
        self.symbol = symbol
        self.is_computer = is_computer


# Game class - handles everything from setup to game play
class Game:
    def __init__(self):
        self.board = Board()
        self.scores = {"X": 0, "O": 0, "Draw": 0}

    def setup(self):
 # Welcome players and let them choose game mode       
        print("=== Welcome to Tic Tac Toe ===")
        print("Select game mode:")
        print("1. Player vs Player")
        print("2. Player vs Computer")
        choice = input("Enter 1 or 2: ")
# Get player 1's name - they'll be 'X'
        p1_name = input("Enter Player 1 name: ")
        player1 = Player(p1_name, "X")

# Create player 2 based on the chosen game mode
        if choice == "1":
            p2_name = input("Enter Player 2 name: ")
            player2 = Player(p2_name, "O")
        else:
            player2 = Player("Computer", "O", True)# Create a computer opponent

        return player1, player2

    def computer_move(self):
        g = self.board.grid
      # a list of all available spots  
        possible_moves = [(r, c) for r in range(3) for c in range(3) if g[r][c] == " "]

# Helper function to test if a move would create a winning line
        def try_move(symbol):
            for r, c in possible_moves:
                g[r][c] = symbol
                if self.board.check_winner(symbol):
                    g[r][c] = " "
                    return (r, c)
                g[r][c] = " "
            return None

        # Try to win or block
        for sym in ["O", "X"]:
            move = try_move(sym)
            if move:
                return move # Found a winning or blocking move!

        # Take center
        if g[1][1] == " ":
            return (1, 1)

        # Take corners
        for (r, c) in [(0, 0), (0, 2), (2, 0), (2, 2)]:
            if g[r][c] == " ":
                return (r, c)

        # Random move- picking any available block 
        return random.choice(possible_moves)

    def play_round(self):
        player1, player2 = self.setup()
        current = player1#Player 1 goes first 
        self.board.display()

#Main game loop which keeps going uuntil someone wins or board is full 
        while True:
            print(f"\n{current.name}'s turn ({current.symbol})")
            #Handles computers turn
            if current.is_computer:
                r, c = self.computer_move()
                self.board.grid[r][c] = current.symbol
            #Handle users turn    
            else:
                move = input(f"Enter position (e.g., A1): ").upper()
                if not self.board.make_move(move, current.symbol):
                    print("Invalid move, try again.")
                    continue #Let them try again

            self.board.display()#Shows the updated board 
            
            # Check if the current player just won
            if self.board.check_winner(current.symbol):
                print(f"\n{current.name} wins!")
                self.scores[current.symbol] += 1
                break

     #Checks if board it full(draw)
            if self.board.is_full():
                print("\nIt's a draw!")
                self.scores["Draw"] += 1
                break

            # Switch to the other player
            current = player2 if current == player1 else player1

#Show the scoreboard after each game 
        print("\nScoreboard:")
        print(f"X Wins: {self.scores['X']} | O Wins: {self.scores['O']} | Draws: {self.scores['Draw']}")
        print("-" * 35)

    def play(self):
        #The main game loop - alllows playing multiple rounds
        while True:
            self.play_round()
            again = input("Play again? (y/n): ").lower()
            if again != "y":
                print("\nThanks for playing!")
                break
            self.board.reset() #Clear the board for the next game 


# Run Game
if __name__ == "__main__":
    game = Game()
    game.play()
