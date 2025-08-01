from random import randint

board = []
for n in range(0,9):
    board.append(f' ')

example_board = []
for n in range(0,9):
    example_board.append(f'{n}')

def AI():
    ai_user = randint(0,8)
    check = True
    while check:
        if board[ai_user] != " ":
            ai_user = randint(0,8)
        else:
            board[ai_user] = 'O'
            check = False

def show_example():
 print('-------')
 for n in range(0,3):
    print(f'|{example_board[n]}|{example_board[n+3]}|{example_board[n+6]}|')
    print('-------')

def show_board():
    print('-------')
    for n in range(0,3):
        print(f'|{board[n]}|{board[n+3]}|{board[n+6]}|')
        print('-------')

def checking(side,ai):
    if side == board[0] and side == board[1] and side == board[2] or side == board[3] and side == board[4] and side == board[5] or side == board[6] and side == board[7] and side == board[8]:
        if ai:
           print(f"Game is over! AI WON")
           return True
        else:
            print(f"Game is over! {side} WON")
            return True
    
    if side == board[0] and side == board[3] and side == board[6] or side == board[1] and side == board[4] and side == board[7] or side == board[2] and side == board[5] and side == board[8]:
        if ai:
           print(f"Game is over! AI WON")
           return True
        else:
            print(f"Game is over! {side} WON")
            return True
    
    if side == board[0] and side == board[4] and side == board[8] or side == board[2] and side == board[4] and side == board[6]:
        if ai:
           print(f"Game is over! AI WON")
           return True
        else:
            print(f"Game is over! {side} WON")
            return True
       

def player_x():
    user = int(input())
    check = True
    while check:
        try:
            if board[user] != " ":
                print("this place is already taken! Choose again")
                user = int(input())
            else:
                board[user] = 'X'
                check = False
        except IndexError:
            print("Choose between 0 and 8")
            user = int(input())

def player_o():
    user = int(input())
    check = True
    while check:
        try:
            if board[user] != " ":
                print("this place is already taken! Choose again")
                user = int(input())
            else:
                board[user] = 'O'
                check = False
        except IndexError:
            print("Choose between 0 and 8")
            user = int(input())

print("WELCOME TO TIC TAC TOE!")
print("BELOW YOU CAN SEE HOW TABLE NUMBERS ARE PLACED:")

show_example()

def ai_settings():
    ai_q = input("Do you want to play against AI? Type Y for yes, or N for no\n")
    check = True
    while check:
        if ai_q.upper() == 'Y':
            print("AI ENABLED")
            check = False
            return True
        elif ai_q.upper() == 'N':
            print("AI DISABLED")
            check = False
            return False
        else:
            print("ERROR, TRY AGAIN")
            ai_q = input("Do you want to play against AI? Type Y for yes, or N for no\n")
    
ai_on = ai_settings()

print("now let's start the game")
game = True
n = 0
while game:
    if n%2 == 0:
        n=n+1
        print("X is choosing now:")
        player_x()
        show_board()
        if checking('X',ai=False):
            game = False
        elif n == 9:
                game = False
                print("Game is over! Nobody won")
    else:
        n=n+1
        if ai_on:
            print("AI chose")
            AI()
            if checking('O',ai=True):
                game = False
            elif n == 9:
                game = False
                print("Game is over! Nobody won")
        else:
            print("O is choosing now:")
            player_o()
            if checking('O',ai=False):
                game = False
        show_board()
    