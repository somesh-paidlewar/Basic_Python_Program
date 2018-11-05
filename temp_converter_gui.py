#Temp_Converter.py
#Temperature converter using a simple Graphical User Interface

from graphics import *

win = GraphWin("Temperature Converter",400,300)			#Set the Window and the Co-ordinate System
win.setCoords(0.0,0.0,3.0,4.0)

#Draw the interface
Text(Point(1,3), 'Temperature in Degree Celcius : ').draw(win)
Text(Point(1,1), 'Temperature in Degree Fahreneit : ').draw(win)
inputText = Entry(Point(2.25,3),5)
inputText.setText("")
inputText.draw(win)

outputText = Text(Point(2.25,1), "-")
outputText.draw(win)

button = Text(Point(1.5,2.0),'Convert It')
button.draw(win)

Rectangle(Point(1,1.5),Point(2,2.5)).draw(win)
input = inputText.getText()
# Wait for a mouse click
while True:
	p = win.getMouse()
	x = p.getX()
	y = p.getY()
	if 1 <= x and 2>=x and 1.5<=y and 2.5>= y:
		break

#Convert input
celcius = float(inputText.getText())
fahreneit = (9.0/5.0) * celcius + 32

# display output and change button
outputText.setText(round(fahreneit,2))
button.setText('Quit')

# Wait for mouse click and quit
while True:
	p = win.getMouse()
	x = p.getX()
	y = p.getY()
	if 1 <= x and 2>=x and 1.5<=y and 2.5>= y:
		break
win.close()

