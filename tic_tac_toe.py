# Tic Tac Toe

board = [' ' for _ in range(9)] 


def print_board():
    """Prints the tic tac toe game"""
    for i in range(3):
        for j in range(3):
            print(board[i*3 + j], end=" ")
        print()


def is_winner(player, board):
    """Conditions to win the game"""
    win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6))
    for condition in win_conditions:
        if board[condition[0]] == player and board[condition[1]] == player and board[condition[2]] == player:
            return True
    return False


def is_board_full(board):
    """Checks if all the squares on the board are filled"""
    for space in board:
        if space == ' ':
            return False
    return True


def player_move(player):
    """Gets the player's move and validates it"""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if 1 <= move <= 9 and board[move - 1] == ' ':
                return move - 1
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


def main():
    """Runs the game"""
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board()
        move = player_move(current_player)
        board[move] = current_player

        if is_winner(current_player, board):
            print_board()
            print(f"Player {current_player} wins!")
            game_over = True
        elif is_board_full(board):
            print_board()
            print("It's a tie!")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'

    print("Thanks for playing!")


if __name__ == "__main__":
    main()