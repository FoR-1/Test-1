board = list(range(1,10))
wins_line= [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(7,5,3)]
def draw_board ():
    print("--------")
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3])
    print("--------")

def error_input(players):
    while True:
        value = input("Where to put:" +players)
        if not (value in '123456789'):
            print("Error. Repeat")
            continue
        value = int(value)
        if str(board[value-1]) in 'XO':
            print("Busy")
            continue
        board[value-1]=players
        break

def wins():
    for each in wins_line:
        if (board[each[0]-1])==(board[each[1]-1])==(board[each[2]-1]):
            return board[each[1]-1]
    else:
         return False


def main():
    counter = 0
    while True:
        draw_board()
        if counter % 2 == 0:
            error_input('X')
        else:
            error_input('O')
        if counter >3:
            winner = wins()
            if winner:
                draw_board()
                print(winner, "-WINNER)")
                break
        counter +=1
        if counter>8:
            draw_board()
            print("DRAW!")
            break

main()
