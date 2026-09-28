def initialize_board():
    """3x3 ka empty grid initialize karta hai hyphen (-) ke saath."""
    return [['-' for _ in range(3)] for _ in range(3)]

def display_board(board):
    """Board ki current state display karta hai."""
    print()
    for row in board:
        print(" ".join(row))
    print()

def check_win(board, player):
    """Rows, columns aur diagonals check karta hai win ke liye."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

def check_draw(board):
    """Check karta hai ki board pura bhar gaya hai ya nahi."""
    for row in board:
        if '-' in row:
            return False
    return True

def player_move(board, player):
    """Player se row aur column input leta hai."""
    while True:
        try:
            move = input(f"Player {player}, enter your move as 'row,col' (0-2, e.g., 0,1): ")
            row_str, col_str = move.strip().split(',')
            row, col = int(row_str), int(col_str)

            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == '-':
                    board[row][col] = player
                    break
                else:
                    print("Ye spot pehle se occupied hai! Doosra spot choose karo.")
            else:
                print("Index 0, 1 ya 2 hi hona chahiye! Dobara try karo.")
        except ValueError:
            print("Invalid format! Please input aise do: row,col (example: 1,2)")

def play_tic_tac_toe():
    """Main game loop."""
    board = initialize_board()
    current_player = 'X'

    print("=== Tic-Tac-Toe Game Start ===")

    while True:
        display_board(board)
        player_move(board, current_player)

        # Win check
        if check_win(board, current_player):
            display_board(board)
            print(f"Badhai ho! Player {current_player} jeet gaya!\n")
            break

        # Draw check
        if check_draw(board):
            display_board(board)
            print("Khel khatam! Match Draw ho gaya!\n")
            break

        # Turn badlo: agar X tha toh O, nahi toh X
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_tic_tac_toe() 