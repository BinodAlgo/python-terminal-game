import random 

# Python Terminal Game - Tik Tac Toe 
game_name = "Python"
print("\n", "-"*(18+len(game_name)), "\n")
print("*"*9, "Tik-Tac-Toe", "*"*9)
print("\n", "-"*(18+len(game_name)), "\n")

# Create a game menu 
def game_menu():
  while True:
    print("Welcome to Tic-tac-toe!")
    print("1. Start a new game")
    print("2. View game rules")
    print("3. Exit")
    choice = input("Please enter your choice (1/2/3): ")
    if choice == "1":
      main()
    elif choice == "2":
      display_game_rules()

    elif choice == "3":
      print("Thanks for playing! Goodbye !!")
      break
    else:
      print("Invalid choice. Please enter your valid choice (1/2/3)")

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

# Display game rules 
def display_game_rules():
  print("\nTic-tac-toe Game Rules:")
  print("1. The game is played on a 3x3 grid.")
  print("2. Player 1 is 'X', and Player 2 is 'O'.")
  print("3. Players take turns placing their symbol on an empty cell.")
  print("4. The first player to get 3 of their symbols in a row (horizontally, vertically, or diagonally) wins.")
  print("5. If the grid is filled completely and no player has 3 symbols in a row, the game ends in a draw.\n")


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


# Create an AI opponent for single-player mode:
# Add a function to get a single AI move
def ai_move(board):
  empty_cell = [(i,j) for i in range(3) for j in range(3) if board[i][j] == " "]
  return random.choice(empty_cell)

# Take input from players
def take_player_input(player, board):
  # Run infinite loop unless player give invalid input
  while True:
    row, col = map(int, input(
        f"Player {player} ({'X' if player==1 else 'O'}), enter row and column(1-3) separated by space: ").split())
    try:

      # Check if rows and columns are within the empty board cell
      if 1 <= row <= 3 and 1 <= col <= 3 and board[row-1][col-1] == " ":
        # rows and cols must be zero index so subtract 1 from row & col
        return row-1, col-1
      else:
        raise ValueError("Invalid input. Please enter number between 1 and 3 for row and column.")

    except ValueError as e:
        print(e)


# Update game board
def update_board(player, board, row, col):
  board[row][col] = 'X' if player == 1 else 'O'


# Main game loop
def main():
  # Player 1
  player = 1
  board = initialize_board()
  ai_opponent = False
  opponent_choice = input("Choose your opponent: (1: Human, 2: AI): ")
  if opponent_choice == "2":
    ai_opponent = True
  while True:
    # Display the game board inside the infinite loop
   display_game_board(board)
   # Take row and column number
   if not ai_opponent or player == 1:  
    row, col = take_player_input(player, board)

   else:
    row,col = ai_move(board)
    print(f"AI Player {player} chose {row+1},{col+1}")
    
   # Update game board
   update_board(player, board, row, col)

   # Check the result for winner
   result = check_winner(board)

   if result is not None:
     display_game_board(board)
     if result == "Draw":
       print("It's a draw.")
     else:
       print(f"Player {player} wins!")

      # Break out of the loop
     break

    # Switch between player 1 and player 2
   player = 3 - player


if __name__ == "__main__":
  # Start the game here
  game_menu()

