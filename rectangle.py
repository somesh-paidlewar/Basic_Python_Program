
#Example to use graphics module to draw a rectangle
from graphics import *
import time

win = GraphWin('Rectangle',600,600)			#Window with Title

win.setCoords(0.0,0.0,10.0,10.0)			#Setting up the Co-ordintate system

rect = Rectangle(Point(1,1), Point(2,5))
rect.setFill('green')
rect.setWidth(4)
rect.draw(win)

#time.sleep(10)								#Time for user to see output
win.getMouse()
win.close()


