#To draw a Triangle with three points as input with mouse

from graphics import *

win = GraphWin('Make a Triangle',600,600)
win.setCoords(0.0,0.0,10.0,10.0)
message = Text(Point(5,0.5), 'Click any three points to draw a Triangle')
message.draw(win)

#Get and draw three vertices of the Triangle

p1 = win.getMouse()
p1.draw(win)

p2 = win.getMouse()
p2.draw(win)

p3 = win.getMouse()
p3.draw(win)

#Use the polygon tool to make the triangle

triangle = Polygon(p1,p2,p3)
triangle.setFill('peachpuff')
triangle.setOutline('cyan')
triangle.setWidth(3)
triangle.draw(win)

#Ask user to quit by clicking anywhere else

message.setText('Click anywhere to quit')
win.getMouse()
