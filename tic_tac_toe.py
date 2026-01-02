# Tic Tac Toe Game using Python

board = [' ' for i in range(9)]

def show_instructions():
    print("Welcome to Tic Tac Toe")
    print("Positions are as follows:")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")
    print()

def display_board():
    print()
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
    print()

def player_move(player):
    while True:
        try:
            position = int(input(f"Player {player}, enter position (1-9): "))
            if position < 1 or position > 9:
                print("Invalid position. Choose between 1 and 9.")
            elif board[position - 1] != ' ':
                print("Position already filled. Try another.")
            else:
                board[position - 1] = player
                break
        except ValueError:
            print("Please enter a valid number.")

def check_winner(player):
    winning_combinations = [
        (0,1,2), (3,4,5), (6,7,8),   # rows
        (0,3,6), (1,4,7), (2,5,8),   # columns
        (0,4,8), (2,4,6)             # diagonals
    ]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def check_draw():
    for space in board:
        if space == ' ':
            return False
    return True

def switch_player(current):
    if current == 'X':
        return 'O'
    else:
        return 'X'

def start_game():
    current_player = 'X'
    show_instructions()

    while True:
        display_board()
        player_move(current_player)

        if check_winner(current_player):
            display_board()
            print(f"🎉 Player {current_player} wins the game!")
            break

        if check_draw():
            display_board()
            print("🤝 The game is a draw!")
            break

        current_player = switch_player(current_player)

# Start the game
start_game()
