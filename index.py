import random
grid = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
def display_board():
    print('-' * 5)
    for row in grid:
        print('|'.join(row))
        print('-' * 5)

def player_move(a):
    print("players turn")
    row_num=int(input("enter row number"))
    column_num=int(input("enter column number"))
    grid[row_num-1][column_num-1]= a

def computer_move(b):
    row_num=random.randint(1,3)
    column_num=random.randint(1,3)
    if grid[row_num-1][column_num-1]==' ':
        grid[row_num-1][column_num-1]=b
    else:
        return computer_move(computer_icon)

def winner_available():
    if grid[0][0]==grid[0][1]==grid[0][2] and grid[0][0]!=' ':
        return True
    elif grid[1][0]==grid[1][1]==grid[1][2] and grid[1][0]!=' ':
        return True
    elif grid[2][0]==grid[2][1]==grid[2][2] and grid[2][0]!=' ':
        return True
    elif grid[0][0]==grid[1][0]==grid[2][0] and grid[0][0]!=' ':
        return True
    elif grid[0][1]==grid[1][1]==grid[2][1] and grid[0][1]!=' ':
        return True
    elif grid[0][2]==grid[1][2]==grid[2][2] and grid[0][2]!=' ':
        return True
    elif grid[0][0]==grid[1][1]==grid[2][2] and grid[0][0]!=' ':
        return True
    elif grid[0][2]==grid[1][1]==grid[2][0] and grid[0][2]!=' ':
        return True
    else:
        return False

def check_winner():
    display_board()
    if grid[0][0]==grid[0][1]==grid[0][2] and grid[0][0]==player_icon:
        print("player won")
    elif grid[0][0]==grid[0][1]==grid[0][2] and grid[0][0]==computer_icon:
        print("computer won")

    elif grid[1][0]==grid[1][1]==grid[1][2] and grid[1][0]==player_icon:
        print("player won")
    elif grid[1][0]==grid[1][1]==grid[1][2] and grid[1][0]==computer_icon:
        print("computer won")

    elif grid[2][0]==grid[2][1]==grid[2][2] and grid[2][0]==player_icon:
        print("player won")
    elif grid[2][0]==grid[2][1]==grid[2][2] and grid[2][0]==computer_icon:
        print("computer won")

    elif grid[0][0]==grid[1][0]==grid[2][0] and grid[0][0]==player_icon:
        print("player won")
    elif grid[0][0]==grid[1][0]==grid[2][0] and grid[0][0]==computer_icon:
        print("computer won")

    elif grid[0][1]==grid[1][1]==grid[2][1] and grid[0][1]==player_icon:
        print("player won")
    elif grid[0][1]==grid[1][1]==grid[2][1] and grid[0][1]==computer_icon:
        print("computer won")


    elif grid[0][2]==grid[1][2]==grid[2][2] and grid[0][2]==player_icon:
        print("player won")
    elif grid[0][2]==grid[1][2]==grid[2][2] and grid[0][2]==computer_icon:
        print("computer won")

    elif grid[0][0]==grid[1][1]==grid[2][2] and grid[0][0]==player_icon:
        print("player won")
    elif grid[0][0]==grid[1][1]==grid[2][2] and grid[0][0]==computer_icon:
        print("computer won")

    elif grid[0][2]==grid[1][1]==grid[2][0] and grid[0][2]==player_icon:
        print("player won")
    elif grid[0][2]==grid[1][1]==grid[2][0] and grid[0][2]==computer_icon:
        print("computer won")


if random.randint(1,2)==1:
    player_icon='X'
    computer_icon='O'
else:
    player_icon='O'
    computer_icon='X'

print("player icon is "+player_icon)
print("computer icon is "+computer_icon)

if random.randint(1,2)==1:
    for i in range(1,5):
        display_board()
        player_move(player_icon)
        if winner_available():
            check_winner()
            break
        display_board()
        computer_move(computer_icon)
        if winner_available():
            check_winner()
            break
    if not winner_available():
        display_board()
        player_move(player_icon)
        display_board()
        if winner_available():
            check_winner()
        else:
            print("its a tie")
else:
    for i in range(1,5):
        display_board()
        computer_move(computer_icon)
        if winner_available():
            check_winner()
            break
        display_board()
        player_move(player_icon)
        if winner_available():
            check_winner()
            break
    if not winner_available():
        display_board()
        computer_move(computer_icon)
        display_board()
        if winner_available():
            check_winner()
        else:
            print("its a tie")