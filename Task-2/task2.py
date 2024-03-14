import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_available_moves(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]

def get_player_move():
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if 0 <= row < 3 and 0 <= col < 3:
                return row, col
            else:
                print("Invalid input. Row and column must be between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_computer_move(board):
    available_moves = get_available_moves(board)
    return random.choice(available_moves)

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = random.choice(players)

    print("Welcome to Tic-Tac-Toe!")

    while True:
        print_board(board)

        if current_player == "X":
            row, col = get_player_move()
        else:
            print("Computer's turn:")
            row, col = get_computer_move(board)
        
        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                if current_player == "X":
                    print("Congratulations! You win!")
                else:
                    print("Computer wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Cell already taken. Try again.")

if __name__ == "__main__":
    play_tic_tac_toe()
