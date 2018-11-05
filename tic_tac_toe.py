#Tic-Tac-Toe Game
import os
Board = {"topL" : " ", "topM" : " ", "topR" : " ",
         "midL" : " ", "midM" : " ", "midR" : " ",
         "lowL" : " ", "lowM" : " ", "lowR" : " ",}
def printboard(Board):
    print(Board["topL"] + "|" + Board["topM"] + "|" + Board["topR"])
    print("-+-+-")
    print(Board["midL"] + "|" + Board["midM"] + "|" + Board["midR"])
    print("-+-+-")
    print(Board["lowL"] + "|" + Board["lowM"] + "|" + Board["lowR"])
printboard(Board)
turn = "X"
count = 0
flag = 0
while count < 10:
    if flag != 1:
        print("Turn for " + turn + ". Move on which space?(Type \'Quit\' to exit game)")
        move = input()

        if move == 'Quit' or move == 'quit':
            break
            
        if Board[move] == " ":
            count = count + 1
            Board[move] = turn
            if turn == "X":
                turn = "0"
            else:
                turn = "X"
        printboard(Board)
        if (Board['topL']== Board['topM']==Board['topR']== "X") or (Board['midL']==Board['midM']==Board['midR']=="X") or (Board['lowL']==Board['lowM']==Board['lowR']=="X") or (Board['topL']==Board['midL']==Board['lowL']=="X") or (Board['topM']==Board['midM']==Board['lowM']=="X") or (Board['topR']==Board['midR']==Board['lowR'] =="X") or (Board['topL']==Board['midM']==Board['lowR']=="X") or (Board['topR']==Board['midM']==Board['lowL']=="X"):
            flag = 1
            print("Game Over!!! \'X\' Wins")
            break
        if (Board['topL']== Board['topM']==Board['topR']== "0") or (Board['midL']==Board['midM']==Board['midR']=="0") or (Board['lowL']==Board['lowM']==Board['lowR']=="0") or (Board['topL']==Board['midL']==Board['lowL']=="0") or (Board['topM']==Board['midM']==Board['lowM']=="0") or (Board['topR']==Board['midR']==Board['lowR'] =="0") or (Board['topL']==Board['midM']==Board['lowR']=="0") or (Board['topR']==Board['midM']==Board['lowL']=="0"):
            flag = 1
            print("Game Over!!! \'0\' Wins")
            break