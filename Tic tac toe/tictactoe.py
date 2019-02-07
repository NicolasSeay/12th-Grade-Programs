# Tic Tac Toe

import random
import os
import sys

def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def whoGoesFirst():
    firstplay = random.randrange(0,2)
    if firstplay == 0:
        print "Computer goes first and is represented by X"
        getComputerMove(board)
    else:
        print "You go first and are represented by O"
        getPlayerMove(board)
    # Randomly choose the player who goes first.
    # Computer is always X
    # User is always O
   
def playAgain():
    decision = raw_input("Play again? (y/n)")
    if decision == 'y':
        return True
        print "PLAYING AGAIN"
    else:
        return False
    # This function returns True if the player wants to play again, otherwise it returns False.
    
def makeMove(board, letter, move):
    value = 0

def isWinner(bo, le):
    boardcounter = 0
    for i in range(9):
        if board[i+1] != ' ':
            boardcounter+=1
    if le == 'O':
        if (board[1]=='O' and board[2]=='O' and board[3]=='O'):
            print "You have won!"
            return 1
        elif (board[4]=='O' and board[5]=='O' and board[6]=='O'):
            print "You have won!"
            return 1
        elif (board[7]=='O' and board[8]=='O' and board[9]=='O'):
            print "You have won!"
            return 1
        elif (board[1]=='O' and board[4]=='O' and board[7]=='O'):
            print "You have won!"
            return 1
        elif (board[2]=='O' and board[5]=='O' and board[8]=='O'):
            print "You have won!"
            return 1
            #playAgain()
        elif (board[3]=='O' and board[6]=='O' and board[9]=='O'):
            print "You have won!"
            return 1
        elif (board[1]=='O' and board[5]=='O' and board[9]=='O'):
            print "You have won!"
            return 1
        elif (board[7]=='O' and board[5]=='O' and board[3]=='O'):
            print "You have won!"
            return 1
        elif boardcounter == 9:
            print "It's a tie."
            return 1
        else:
            getComputerMove(board)

    elif le == 'X':
        if (board[1]=='X' and board[2]=='X' and board[3]=='X'):
            print "You have lost :("
            return 1
        elif (board[4]=='X' and board[5]=='X' and board[6]=='X'):
            print "You have lost :("
            return 1
        elif (board[7]=='X' and board[8]=='X' and board[9]=='X'):
            print "You have lost :("
            return 1
        elif (board[1]=='X' and board[4]=='X' and board[7]=='X'):
            print "You have lost :("
            return 1
        elif (board[2]=='X' and board[5]=='X' and board[8]=='X'):
            print "You have lost :("
            return 1
        elif (board[3]=='X' and board[6]=='X' and board[9]=='X'):
            print "You have lost :("
            return 1
        elif (board[1]=='X' and board[5]=='X' and board[9]=='X'):
            print "You have lost :("
            return 1
        elif (board[7]=='X' and board[5]=='X' and board[3]=='X'):
            print "You have lost :("
            return 1
        elif boardcounter == 9:
            print "It's a tie."
            return 1
        else:
            getPlayerMove(board)
    
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.

def checkWinMove(board):    #123, 456, 789, 147, 258, 369, 159, 753
    winmove1 = [1,2,3]
    winmove2 = [4,5,6]
    winmove3 = [7,8,9]
    winmove4 = [1,4,7]
    winmove5 = [2,5,8]
    winmove6 = [3,6,9]
    winmove7 = [1,5,9]
    winmove8 = [7,5,3]
    wintotal = [winmove1, winmove2, winmove3, winmove4, winmove5, winmove6, winmove7, winmove8]
    Xcounter = 0
    Ocounter = 0
    assignpos = 0
    for i in range(8):
        for a in range(3):
            if board[wintotal[i][a]] == 'X':
                Xcounter += 1
            if board[wintotal[i][a]] == 'O':
                Ocounter += 1
        if Xcounter == 2 and Ocounter == 0:
            for b in range(3):
                if board[wintotal[i][b]] == ' ':
                    assignpos = wintotal[i][b]

        Xcounter = 0
        Ocounter = 0
            #set board[] space, must be in wintotal[i] numbers (1, 2 or 3 for example)
    return assignpos


def checkBlockMove(board):
    blockmove1 = [1,2,3]
    blockmove2 = [4,5,6]
    blockmove3 = [7,8,9]
    blockmove4 = [1,4,7]
    blockmove5 = [2,5,8]
    blockmove6 = [3,6,9]
    blockmove7 = [1,5,9]
    blockmove8 = [7,5,3]
    blocktotal = [blockmove1, blockmove2, blockmove3, blockmove4, blockmove5, blockmove6, blockmove7, blockmove8]
    Xcounter = 0
    Ocounter = 0
    assignpos = 0
    for i in range(8):
        for a in range(3):
            if board[blocktotal[i][a]] == 'X':
                Xcounter += 1
            if board[blocktotal[i][a]] == 'O':
                Ocounter += 1
        if Xcounter == 0 and Ocounter == 2:
            for b in range(3):
                if board[blocktotal[i][b]] == ' ':
                    assignpos = blocktotal[i][b]

        Xcounter = 0
        Ocounter = 0
            #set board[] space, must be in wintotal[i] numbers (1, 2 or 3 for example)
    return assignpos




def getPlayerMove(board):
    playermove = int(raw_input("Player move: "))
    board[playermove] = 'O'
    drawBoard(board)
    print ""
    if isWinner(board, 'O') == 0:
        getComputerMove(board)
    #isWinner(board, 'O')
    #getComputerMove(board)
    # Let the player type in his move.
   
def chooseRandomMoveFromList(board, movesList):
    value = 0
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    
def getComputerMove(board):
    compmove = 0
    
    if difficulty == '1':
        compmove = random.randrange(1, 10)
        while board[compmove] != ' ':
            compmove = random.randrange(1, 10)  #1-9

    elif difficulty == '2':
        x = checkWinMove(board)
        if x != 0:  #WINMOVE
            compmove = x
        else:       #RANDOM based off TIERS
            if board[5] == ' ':
                board[5] = 'X'
            elif (board[1]==' ' or board[3]==' ' or board[7]==' ' or board[9]==' '):
                compmove = random.randrange(1, 10)
                #for i in range(4):
                #    if ((board[compmove] == ' ') and (compmove == 1 or compmove == 3 or compmove == 7 or compmove == 9)):
                #        break
                #    else:
                #        compmove = random.randrange(1, 10)
                if board[1] == ' ':
                    compmove = 1
                elif board[3] == ' ':
                    compmove = 3
                elif board[7] == ' ':
                    compmove = 7
                elif board[9] == ' ':
                    compmove = 9
            else:
                compmove = random.randrange(1, 10)
                while board[compmove] != ' ':
                    compmove = random.randrange(1, 10)  #1-9
                    
    elif difficulty == '3':
        x = checkWinMove(board)
        y = checkBlockMove(board)
        if x != 0:      #WINMOVE
            compmove = x
            
        elif y != 0:    #BLOCKMOVE
            compmove = y
            
        else:           #RANDOM based off TIERS
            if board[5] == ' ':
                board[5] = 'X'
            elif (board[1]==' ' or board[3]==' ' or board[7]==' ' or board[9]==' '):
                compmove = random.randrange(1, 10)
                if board[1] == ' ':
                    compmove = 1
                elif board[3] == ' ':
                    compmove = 3
                elif board[7] == ' ':
                    compmove = 7
                elif board[9] == ' ':
                    compmove = 9
            else:
                compmove = random.randrange(1, 10)
                while board[compmove] != ' ':
                    compmove = random.randrange(1, 10)  #1-9
    
    board[compmove] = 'X'
    drawBoard(board)
    print ""
    if isWinner(board, 'X') == 0:
        getPlayerMove(board)
    # Given a board and the computer's letter, determine where to move and return that move.
    
    
#main
playagain = True
while playagain:
    difficulty = raw_input("Choose difficulty (1, 2, 3)")
    board = ['KeepEmpty', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    drawBoard(board)
    print ""
    whoGoesFirst()
    playagain = playAgain()

