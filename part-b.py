def create_board():
    board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
    ]
    return board

def display_board(board):
    for row in board:
        print("|".join(row))
        print("-----")

def get_player_move(player):
    row = int(input("Enter a row number: "))
    column = int(input("Enter a column number: "))

def is_valid_move(board, row, column):
    if column < 0 or column > 2:
        return False
    if board[row][column] != " ":
        return False

def make_move(board, row, column, player):
    board[row][column] = player

def check_rows(board, player):
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True

def check_columns(board, player):
    for column in board:
        if column[0] == player and column [1] == player and column[2] == player:
            return True

def check_diagonals(board, player):
    if (board[0][0] == player and
        board[1][1] == player and
        board[2][2] == player):
        return True
    if (board[0][2] == player and
        board[1][1] == player and
        board[2][0] == player):
        return True

def check_draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False

def check_winner(board, player):
    return(check_rows(board, player), check_columns(board, player))
    display_board(board)
    print("Player ", player, " is the winner")

def switch_player(player):
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"

def play_game():
    while True:
        board = create_board(board)
        row, column = get_player_move(player)
        if not is_valid_move(board, row, column):
            print("Invalid move please try again")
            continue
        make_move(board, row, column, player)
        if check_winner(board, player):
            display_board(board)
            print("Player: ", player)
            break
        if check_draw(board):
            display_board(board)
            print("Draw")
            break
        player = switch_player(player)

def main():
    print("Welcome to Tic-Tac-Toe")
    play_game()

main()