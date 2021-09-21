def main():
    won = False
    #make board dicts
    board = [[],[],[]]

    for i in range(3):
        for j in range(3):
            board[i].append({str(i) + str(j): 'E'})
    #move keepertracker
    move = ['0', 'X']
    s = 0
    #gameplay loop
    while not won:

        printboard(board)

        #ask what move
        print(f'{move[s]}s turn:', end='')
        turn = input('')
        
        #update board
        update(turn, board, move[s])

        #check if win
        if check(board):
            printboard(board)
            win(move[s])
            won = True
        #update player
        if s == 0:
            s = 1
        else:
            s = 0
def printboard(board):
    for i in range(3):
        for j in range(3):
            x = list(board[i][j].values())
            print(f'{x[0]}', end='')
            if j < 2:
                print('|', end='')
        print('\n-----')

def update(turn, board, player):
    for i in range(3):
        for j in range(3):
            if turn in list(board[i][j].keys()):
                board[i][j][str(i) + str(j)] = player

def check(board):
    #ca is X cb is 0
    #check vertial wins
    for i in range(3):
        ca = cb = 0
        for j in range(3):
            if list(board[i][j].values())[0] == 'X':
                ca +=1
            elif list(board[i][j].values())[0] == '0':
                cb +=1
        if ca == 3 or cb == 3:
            return True
    #check horizonal wins
    for i in range(3):
        ca = cb = 0
        for j in range(3):
            if list(board[j][i].values())[0] == 'X':
                ca +=1
            elif list(board[j][i].values())[0] == '0':
                cb +=1
        if ca == 3 or cb == 3:
            return True
    #check diag
    ca = cb = 0
    for i in range(3):
        if board[i][i].values() == 'X':
            ca +=1
        elif board[i][i].values() == '0':
            cb +=1
        if ca == 3 or cb == 3:
            return True

def win(winner):print(f'{winner} wins!')
main()