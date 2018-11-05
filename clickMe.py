#Mouse Click Co-ordinates
from graphics import *
import time

win = GraphWin('Click Me!',600,600)
win.setCoords(0.0,0.0,6.0,6.0)


for i in range (3):
	p = win.getMouse()
	print(' You clicked at :',p.getX,p.getY)

time.sleep(10)
win.close()
