#Click and add a text message at that point
from graphics import *
import time
win = GraphWin('Click and type',600,600)
win.setCoords(0.0,0.0,10.0,10.0)
message = Text(Point(5,1),'Click somewhere and Type')
message.draw(win)
time.sleep(5)
for i in range(3):
	p = win.getMouse()
	p.draw(win)
	txt = win.getKey()
	text_print= Text(p,txt)
	text_print.draw(win)

message.setText('Click anywhere to quit')
win.getMouse()



