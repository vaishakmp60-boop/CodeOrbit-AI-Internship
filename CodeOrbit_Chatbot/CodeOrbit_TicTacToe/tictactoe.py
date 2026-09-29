import random
import time

def print_board(board):
    # Displays the Tic-Tac-Toe board clearly after every move
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, player):
    # Detects win conditions across rows, columns, and diagonals
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def check_draw(board):
    # Detects draw condition if no empty spaces remain
    return " " not in board

def get_available_moves(board):
    return [i for i, spot in enumerate(board) if spot == " "]

def computer_move(board):
    available_moves = get_available_moves(board)
    
    # Simple AI Rule 1: Check if the computer can win on this turn
    for move in available_moves:
        board[move] = "O"
        if check_win(board, "O"):
            return # Keep the winning move
        board[move] = " " # Undo if it doesn't result in a win
        
    # Simple AI Rule 2: Check if the player might win on their next turn, and block them
    for move in available_moves:
        board[move] = "X"
        if check_win(board, "X"):
            board[move] = "O" # Overwrite with O to block
            return
        board[move] = " " # Undo
        
    # Simple AI Rule 3: If no immediate win or block, pick a random available spot
    move = random.choice(available_moves)
    board[move] = "O"

def play_game():
    print("Welcome to Tic-Tac-Toe! You are 'X' and the Computer is 'O'.")
    print("Positions are numbered 0-8, from left to right, top to bottom.")
    
    # Initialize an empty board
    board = [" "] * 9
    
    # Show reference board so the user knows which numbers correspond to which spaces
    reference = [str(i) for i in range(9)]
    print("Reference Board:")
    print_board(reference)

    while True:
        # User's turn
        try:
            player_pos = int(input("Enter your move (0-8): "))
            if player_pos < 0 or player_pos > 8 or board[player_pos] != " ":
                print("Invalid move. That spot is either taken or out of range. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number between 0 and 8.")
            continue

        # Apply user move
        board[player_pos] = "X"
        print_board(board)

        # Check user win/draw
        if check_win(board, "X"):
            print("Congratulations! You beat the AI!")
            break
        if check_draw(board):
            print("It's a draw! Well played.")
            break

        # Computer's turn
        print("Computer is thinking...")
        time.sleep(1) # Adds a slight delay so it feels like the AI is "thinking"
        computer_move(board)
        print_board(board)

        # Check computer win/draw
        if check_win(board, "O"):
            print("Computer wins! Better luck next time.")
            break
        if check_draw(board):
            print("It's a draw! Well played.")
            break

if __name__ == "__main__":
    play_game()