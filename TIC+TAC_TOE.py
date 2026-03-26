board = [' ' for _ in range(9)]

def print_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
        if i < 6:
            print('---------')
    print()


def is_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_draw():
    return ' ' not in board

# Minimax Algorithm
def minimax(is_maximizing):
    if is_winner('O'):
        return 1
    elif is_winner('X'):
        return -1
    elif is_draw():
        return 0

    if is_maximizing:
        best_score = -100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = 100
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -100
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def play_game():
    print("Tic Tac Toe Game (You = X, AI = O)")
    print_board()

    while True:
        # Player Move
        pos = int(input("Enter position (1-9): ")) - 1
        if board[pos] == ' ':
            board[pos] = 'X'
        else:
            print("Invalid move!")
            continue

        print_board()

        if is_winner('X'):
            print("You Win! 🎉")
            break
        elif is_draw():
            print("Draw!")
            break

        # AI Move
        ai_move = best_move()
        board[ai_move] = 'O'
        print("AI Move:")
        print_board()

        if is_winner('O'):
            print("AI Wins! 🤖")
            break
        elif is_draw():
            print("Draw!")
            break

play_game()