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

    # Check if player has cross win from top left to bottom right
  cross_line_test1 = board[0][0] == board[1][1] == board[2][2] != " "
  # Check if player has cross win from top right to bottom left.
  cross_line_test2 = board[0][2] == board[1][1] == board[2][0] != " "
  if cross_line_test1 or cross_line_test2:
    return board[1][1]

  # Check for match draw
  if all(board[i][j] != " " for i in range(3) for j in range(3)):
    return "Draw"
  return None

  
