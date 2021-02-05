#Global Variables

#game board

board=["-","-","-",
      "-","-","-",
       "-","-","-"]

#game still goin
game_still_going=True

#who win or tie
winner =None
#whos turn isinstance
current_player="X"

def display_board():
  print(board[0]+" | "+board[1]+" | "+board[2])
  print(board[3]+" | "+board[4]+" | "+board[5])
  print(board[6]+" | "+board[7]+" | "+board[8])

def play_game():
  #display initial board
  display_board()
  while game_still_going:

    handle_turn(current_player)
    check_if_game_over()
    flip_player()
  #game has ended
  if winner=="X" or winner=="O":
    print(winner + " won.")
  elif winner==None:
    print("Tie.")


def handle_turn(player):
  print(player +"'s turn.'")
  position=input("Choose a position from 1-9:")
  valid=False
  while not valid:
    while position not in ["1","2","3","4","5","6","8","9"]:
      position=input("Invalid Output. Choose a position from 1-9:")
    

    #in to SyntaxWarning
    position=int(position)-1

    if board[position] == "-":
      valid=True
    else:
      print("You can't go there.Go again")

  board[position]=player
  display_board()


def check_if_game_over():
  check_for_winner()
  check_if_tie()


def check_rows():
  
  global game_still_going
  #check if any of the rows have all the same value and not the (-)
  row_1=board[0]==board[1]==board[2] !="-"
  row_2=board[3]==board[4]==board[5] !="-"
  row_3=board[6]==board[7]==board[8] !="-"
  #if any rows does have a match,flag there is a win
  if row_1 or row_2 or row_3:
    game_still_going=False
  #return the winner is (X or O)
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return

def check_cols():
  global game_still_going

  #check if any of the rows have all the same value and not the (-)
  col_1=board[0]==board[3]==board[6] !="-"
  col_2=board[1]==board[4]==board[7] !="-"
  col_3=board[2]==board[5]==board[8] !="-"
  #if any cols does have a match,flag there is a win
  if col_1 or col_2 or col_3:
    game_still_going=False
  #return the winner is (X or O)
  if col_1:
    return board[0]
  elif col_2:
    return board[1]
  elif col_3:
    return board[2]
  return

def check_diags():
  global game_still_going

    #check if any of the rows have all the same value and not the (-)
  diag_1=board[0]==board[4]==board[8] !="-"
  diag_2=board[6]==board[4]==board[2] !="-"
  #if any diags does have a match,flag there is a win
  if diag_1 or  diag_2:
    game_still_going=False
  #return the winner is (X or O)
  if diag_1:
    return board[0]
  elif diag_2:
    return board[6]
 
  return

def check_for_winner():
  #set up global variable
  global winner
# # check rows
  row_winner=check_rows()
# # check colums
  cols_winner=check_cols()
# # check diagonals
  diags_winner=check_diags()
  if row_winner:
    winner=row_winner
  elif cols_winner:
    winner=cols_winner
  elif diags_winner:
    winner=diags_winner
  else:
    winner=None
  return

def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going=False
  return

def flip_player():
  global current_player
  #if current player is X change it to O
  if current_player=="X":
    current_player="O"
  elif current_player=="O":
    current_player="X"
  return






play_game()



