from random import randint

# Initialize Variables
row_nums = "| 1 | 2 | 3 | 4 | 5 | 6 | 7 |"
row_divider = "+---+---+---+---+---+---+---+"
empty_row = "|   |   |   |   |   |   |   |"

# Function to print space
def output(num_lines,message="",message2="",num_lines2=""):
  for i in range(num_lines):
    print("")
  if message:
    print(message)
  if message2:
    print(message2)
  if num_lines2:
    for i in range(num_lines2):
      print("")


# Function to Display Board based on Game Status
def build_board(board):
  print(row_divider)
  row_text = "|"
  row = 5
  while row >= 0:
    for col in range(7):
      try: board_val = board[col][row]
      except IndexError:
        board_val = ""
      if  board_val == "O":
        row_text += " O |"
      elif board_val == "X":
        row_text += " X |"
      else:
        row_text += "   |"
    print(row_text)
    print(row_divider)
    row_text = "|"
    row -= 1
  print(row_nums)
  output(3)

# Function to place a piece
def place_piece(X_or_O,board,vs_cpu):
  # Collect column choice from player
  print(f'Player {X_or_O}...')
  if (vs_cpu == "Y" and X_or_O == "O"):
    column_num = randint(0,6)
    print(f'Player O chooses to place a piece in column {column_num}.')
  else:
    column_num = input("Please choose a column 1 through 7 to place a piece:   ")
  # Quit out of the game
  if str(column_num).upper() == "QUIT":
    print("Quitting game...")
    return "end_game"
  # Capture errors for invalid values
  try: 
    column_num = int(column_num)
  except ValueError:
    output(3,f'You chose an invalid column number. Player {X_or_O} it is still your turn to choose a column.',"If you'd like to quit the game type QUIT",3)
    return "invalid_move"
  # Must choose a column that exists
  if (column_num > 7 or column_num < 1):
    output(3,f'You chose an invalid column number. Player {X_or_O} it is still your turn to choose a column.',"",3)
    return "invalid_move"
  # Must be an X or an O
  elif not (X_or_O == "X" or X_or_O == "O"):
    output(3,f'There is an invalid player playing the game. Must be an X or O being placed.',"Quitting game...")
    return "end_game"
  # Column must have space
  elif len(board[column_num - 1]) >= 6:
    output(3,f'Column {column_num} is full. Player {X_or_O} it is still your turn to choose a column.',"",3)
    return "invalid_move"
  # A valid move reprints the board and advances the players turn
  else:
    board[column_num - 1].append(X_or_O)
    return "valid_move"


# Function to determine if there is a winner
def find_winner(board):
  # vertical winner
  for col in range(7):
    col_text = ''.join(board[col])
    if (col_text.count('XXXX')):
      return "X"
    elif (col_text.count('OOOO')):
      return "O"
    else:
      continue
  # horizontal winner
  for row in range(6):
    row_text = ""
    for col in range(7):
      try: val = board[col][row]
      except IndexError:
        val = "_"
      row_text += val
    if (row_text.count('XXXX')):
      return "X"
    elif (row_text.count('OOOO')):
      return "O"
    else:
      continue
  # / diagonal winner
  for col in range(4): 
    for row in range(3):
      diag_text = ""
      for i in range(4):
        try: val = board[col+i][row+i]
        except IndexError:
          val = "_"
        diag_text += val
      if (diag_text.count('XXXX')):
        return "X"
      elif (diag_text.count('OOOO')):
        return "O"
  # \ diagonal winner
  for col in range(3,7):
    for row in range(3):
      diag_text = ""
      for i in range(4):
        try: val = board[col-i][row+i]
        except IndexError:
          val = "_"
        diag_text += val
      if (diag_text.count('XXXX')):
        return "X"
      elif (diag_text.count('OOOO')):
        return "O"
  return ""

# Function to tell if board is full
def is_board_full(board):
  for col in range(7):
    if len(board[col]) < 6:
      return False
  return True

# Function to start the game
def play_game():

  # Choose 2 player or a game vs the computer
  output(3,"Welcome to Connect Four!","",3)
  vs_cpu = input("Would you like to play against the computer (Y/N)?   ")
  vs_cpu = vs_cpu.upper()
  while (vs_cpu != "Y" and vs_cpu !="N"):
    output(3)
    vs_cpu = input("Please try again. Enter Y or N:")
    vs_cpu = vs_cpu.upper()

  # Initialize game
  game_status = [[],[],[],[],[],[],[]]
  build_board(game_status)
  current_player = "X"
  winner = ""

  # Loop until there is a winner
  while ((winner == "") and not (is_board_full(game_status))):
    move_outcome = place_piece(current_player,game_status,vs_cpu)
    # Loop until there is a valid move
    while (move_outcome == "invalid_move"):
       move_outcome = place_piece(current_player,game_status,vs_cpu)
    if move_outcome == "end_game":
      output(3,"Quitting game...","",3)
      break
    else:
      output(10,f'Thank you for your move player {current_player}!',"",10)
      build_board(game_status)
      winner = find_winner(game_status)
      if (winner):
        celebrate_string = "!!"
        for i in range(10):
          celebrate_string = celebrate_string + winner + "!!"
        output(3,celebrate_string,"",3)
        print(f'PLAYER {winner} HAS WON THE GAME!!!')
        output(3,celebrate_string,"",3)
      elif is_board_full(game_status):
        output(3,"STALEMATE!!! The board is full and there is no winner. Game over.","",3)
      elif current_player == "X":
        print("Player O, it's your turn to choose a column.")
        current_player = "O"
      else:
        print("Player X, it's your turn to choose a column.")
        current_player = "X"
  
play_game()