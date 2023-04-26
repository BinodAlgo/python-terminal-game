# Python Terminal Game - Tik Tac Toe 
game_name = "Python"
print("\n", "-"*(18+len(game_name)), "\n")
print("*"*9, "Tik-Tac-Toe", "*"*9)
print("\n", "-"*(18+len(game_name)), "\n")
# Welcome players
print("Welcome Players, Game Started !!")

# Initialize game board where players can play with eachother
def initialize_board():
  # Initiaze a game board of 3x3 matrix
  board = [[" " for i in range(3)] for j in range(3)]
  return board

# Display game board of 3x3 martix joined by | and ---
  #   |    |
  # ----------
  #   |    | 
  # ----------
  #   |    |
def display_game_board(board):
   for i in range(len(board)):
    print(" | ".join(board[i]))
    if i < 2:
      print("-"*9)

