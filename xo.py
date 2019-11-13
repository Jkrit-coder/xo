import os
import sys
from importlib import reload  
import colorama
from colorama import Fore, Back, Style
from termcolor import colored



def draw_board(board):
    print ("-" * 13)
    for i in range(3):
        print (Fore.BLUE +"|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-" * 13)


def take_input(player_token, board):
    valid = False
    while not valid:
        
        player_answer = input(Fore.YELLOW  +"Where to put " + player_token+"?  " )
        try:
            player_answer = int(player_answer)
        except:
            print ("Invalid input. Are you sure you entered the number? ")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ("This box is already taken")
        else:
            print ("Invalid input. Enter a number from 1 to 9 to be like. ")

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
                return board[each[0]]
    return False

def main():
    board = list(range(1,10))
    counter = 0
    win = False
    while not win:
        os.system('clear')
        draw_board(board)
        if counter % 2 == 0:
            take_input("X", board,)
        else:
            take_input("O", board)
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (Fore.MAGENTA + tmp, "You wins! ")
                win = True
                break
        if counter == 9:
            print ("Draw! ")
            break
    draw_board(board)
    
     
    
main()

again = str(input("Do you want to play again (type yes or no): "))
if again == "yes":
    main()
else:
    sys.exit(0)
    