#Tic-Tac-Toe Screen
from graphics import *
import time
win = GraphWin()

#set co-ordinate system

win.setCoords(0.0,0.0,3.0,3.0)

#draw lines using the new co-ordinate system

Line(Point(1,0),Point(1,3)).draw(win)	#Vertical Lines
Line(Point(2,0),Point(2,3)).draw(win)

Line(Point(0,1),Point(3,1)).draw(win)	#Horizontal Lines
Line(Point(0,2),Point(3,2)).draw(win)

time.sleep(10)
#input("Press <Enter> key to exit")
win.close()
