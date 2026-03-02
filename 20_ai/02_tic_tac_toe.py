def greet():
    # greet the user with a good morning message
    print("Good morning! Welcome to Tic Tac Toe!")
    print("Player 1 is X")
    print("Player 2 is O")
    print("Let's start the game!")

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)     

def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current = 0
    while True:
        print_board(board)
        print(f"Player {players[current]}'s turn.")
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
        except ValueError:
            print("Invalid input. Please enter numbers 1-3.")
            continue
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            board[row][col] = players[current]
            if check_win(board, players[current]):
                print_board(board)
                print(f"Player {players[current]} wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            current = 1 - current
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    tic_tac_toe()

