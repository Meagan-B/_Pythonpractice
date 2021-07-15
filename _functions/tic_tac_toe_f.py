# tic-tac-toe re-write
#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#
import random
import numpy
#----••••••••----••••••••----••••••••----#
# game board

def board_print(b):
    print(b[:3])
    print(b[3:6])
    print(b[6:])
    
#board_print(board)
#----••••••••----••••••••----••••••••----#
# player select

def char_select():
    usr_char = input('would you like X or O ?\n>>> ').capitalize()
    (h, c) = '',''
    
    if usr_char != 'X' and usr_char != 'O':
        (h, c) = ('X','O')
        print('INCORRECT character input\nyou have been automatically assigned X')
        
    if usr_char == 'X' :
        (h, c) = ('X','O')
    else :
        (h, c) = ('O','X')
     
    return (h, c) 
      
human, comp = char_select()
print('PLAYER: {0}\nCOMP: {1}'.format(human, comp))       
#----••••••••----••••••••----••••••••----#
# character replacement

def char_replace(arr, find, replace):
    #print('ORIGINAL array: {0}\nfind: {1}\nreplacement: {2}'.format(arr, find, replace))
    for cnt in range(arr.count(find)):
        arr[find - 1] = replace
        #print('MODIFIED array: {0}'.format(arr))
        board_print(arr)
#----••••••••----••••••••----••••••••----#
# win check

def win_chk(h, c) :
    wins = [(1,2,3),(1,5,9),(1,4,7),(2,5,8),(3,6,9),(3,5,7),(4,5,6),(7,8,9)]
    ply = [int(m) for m in ply]
    print(ply)
    
    for l in wins :
        l = set(l)
        p = set(p)
        if l == p :
            print('win')

#def win_chk(,)    
#----••••••••----••••••••----••••••••----#
#computer play
            ######START HERE#######
def random_set_buildr() :
    rand_select = [random.randint(1, 9) for i in range(10)]
    print(rand_select)
# ----

random_set_buildr()
#----••••••••----••••••••----••••••••----#
# game play

def play(h, c) :
    ply_count = 0
    ply_track = []
    
    board = [i for i in range(1,10)]
    board_print(board)
    
    while ply_count < 3 :
        move = input('make your move, input digit from 1-9\n>>> ')
        
        x = move.isnumeric()
        if x is True :
            
            move = int(move)
            
            for i in board :
                if move == i :
                    char_replace(board, move, h)
                
                elif move != i : continue    
                
                else :
                    print('invalid play')
                    continue
                
        else:
            print('INCORRECT character input\n')
            continue        
    
play(human, comp)    

#---->>>>>>>>>>>>-------->>>>>>>>>>>>----#


### tic-tac-toe ORIGINAL, https://hackr.io/blog/python-projects ###
#import random
import sys
#board=[i for i in range(0,9)]
#player, computer = '',''
###Corners, Center and Others, respectively
#moves=((1,7,3,9),(5,),(2,4,6,8))
##Winner combinations
#winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
##Table
tab=range(1,10)
def print_board():
    x=1
    for i in board:
        end = ' | '
        if x%3 == 0:
            end = ' \n'
            if i != 1: end+='---------\n';
        char=' '
        if i in ('X','O'): char=i;
        x+=1
        print(char,end=end)
        
def select_char():
    chars=('X','O')
    if random.randint(0,1) == 0:
        return chars[::-1]
    return chars

def can_move(brd, player, move):
    if move in tab and brd[move-1] == move-1:
        return True
    return False

def can_win(brd, player, move):
    places=[]
    x=0
    for i in brd:
        if i == player: places.append(x);
        x+=1
    win=True
    for tup in winners:
        win=True
        for ix in tup:
            if brd[ix] != player:
                win=False
                break
        if win == True:
            break
    return win

def make_move(brd, player, move, undo=False):
    if can_move(brd, player, move):
        brd[move-1] = player
        win=can_win(brd, player, move)
        if undo:
            brd[move-1] = move-1
        return (True, win)
    return (False, False)

##AI goes here
def computer_move():
    move=-1
##If I can win, others do not matter.
    for i in range(1,10):
        if make_move(board, computer, i, True)[1]:
            move=i
            break
    if move == -1:
##If player can win, block him.
        for i in range(1,10):
            if make_move(board, player, i, True)[1]:
                move=i
                break
    if move == -1:
##Otherwise, try to take one of desired places.
        for tup in moves:
            for mv in tup:
                if move == -1 and can_move(board, computer, mv):
                    move=mv
                    break
    return make_move(board, computer, move)

def space_exist():
    return board.count('X') + board.count('O') != 9

player, computer = select_char()
print('Player is [%s] and computer is [%s]' % (player, computer))
result='%%% Deuce ! %%%'

while space_exist():
    print_board()
    print('#Make your move ! [1-9] : ', end='')
    move = int(input())
    moved, won = make_move(board, player, move)
    if not moved:
        print(' >> Invalid number ! Try again !')
        continue

    if won:
        result='*** Congratulations ! You won ! ***'
        break
    elif computer_move()[1]:
        result='=== You lose ! =='
        break;
print_board()
print(result)