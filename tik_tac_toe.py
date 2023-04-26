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


# Check the winner of the game
def check_winner(board):
  for i in range(len(board)):
    # Check if player has horizontal win
    horizontal_line_test = board[i][0] == board[i][1] == board[i][2] != " "
    # Check if player has vertical win
    vertical_line_test = board[0][i] == board[1][i] == board[2][i] != " "
    if horizontal_line_test or vertical_line_test:
      return board[i][i]
