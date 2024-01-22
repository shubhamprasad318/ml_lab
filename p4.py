import os

def draw(board):
    [print(' ' + '|'.join(board[i:i+3])) for i in range(6, -1, -3)]

def take_input(board, spaces, turn):
    while True:
        try:
            pos = int(input(f"{turn}'s turn: Pick position 1-9: "))
            if 1 <= pos <= 9 and board[pos - 1] == ' ':
                break
        except ValueError:
            pass
        print("Enter a valid position.")
    
    spaces -= 1
    board[pos - 1] = turn
    return board, spaces, 'O' if turn == 'X' else 'X'

def check_win(board):
    for i in range(0, 3):
        if board[i] != ' ' and board[i] == board[i+1] == board[i+2]:
            return board[i]
        if board[i] != ' ' and board[i] == board[i+3] == board[i+6]:
            return board[i]
    if board[0] != ' ' and board[0] == board[4] == board[8]:
        return board[0]
    return 0

def main():
    board, spaces, turn = [' ']*9, 9, 'X'
    
    while spaces:
        draw(board)
        board, spaces, turn = take_input(board, spaces, turn)
        os.system('cls' if os.name == 'nt' else 'clear')
        draw(board)
        
        winner = check_win(board)
        if winner:
            print(f'{winner} wins!')
            break
        elif not spaces:
            print("It's a draw!")

if __name__ == "__main__":
    main()
