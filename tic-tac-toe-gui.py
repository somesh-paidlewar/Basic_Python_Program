#Tic Tac Toe using simple GUI 
from graphics import *

# seting the graphics window for the game

win = GraphWin('Tic Tac Toe',800,800)	
win.setCoords(0.0,0.0,8.0,8.0)

# draw lines for the game board

Line(Point(1,3),Point(7,3)).draw(win)		# horizontal lines
Line(Point(1,5),Point(7,5)).draw(win)

Line(Point(3,7),Point(3,1)).draw(win)		# vetical lines
Line(Point(5,7),Point(5,1)).draw(win)

# board dictionary to keep track of the moves by the player

Board = {"topL" : " ", "topM" : " ", "topR" : " ",
	 	 "midL" : " ", "midM" : " ", "midR" : " ",
	 	 "lowL" : " ", "lowM" : " ", "lowR" : " ",}


count = 0		# initailizing variables 
turn = 'X'
flag = 0

#def draw_X(p1,p2,p3,p4):		#draws X in the given box
	#line1 = Line(p1,p2)
	#line2 = Line(p3,p4)
	#line1.setOutline('red')
	#line2.setOutline('red')
	#line1.draw(win)
	#line2.draw(win)

#def draw_O(centre, radius):		# draws O in the given box
	#my_circle = Circle(centre, radius)
	#my_circle.setOutline('blue')
	#my_circle.draw(win)

message = Text(Point(3,0.5),'Turn for '+ turn + ' Click on your move')
message.draw(win)

while count < 9:

	if flag != 1: 				# no player has won

		message.setText('Turn for '+ turn + ' Click on your move')
		
		click = win.getMouse()

		X = click.getX()
		y = click.getY()

		if (1<= X <= 3)  and (5 <= y <= 7):
			move = 'topL'
		if (3<= X <= 5)  and (5 <= y <= 7):
			move = 'topM'
		if (5<= X <= 7)  and (5 <= y <= 7):
			move = 'topR'
		if (1<= X <= 3)  and (3 <= y <= 5):
			move = 'midL'
		if (3<= X <= 5)  and (3 <= y <= 5):
			move = 'midM'
		if (5<= X <= 7)  and (3 <= y <= 5):
			move = 'midR'
		if (1<= X <= 3)  and (1 <= y <= 3):
			move = 'lowL'
		if (3<= X <= 5)  and (1 <= y <= 3):
			move = 'lowM'
		if (5<= X <= 7)  and (1 <= y <= 3):
			move = 'lowR'

	
		if Board[move] == " ":
			count = count + 1
			Board[move]=turn
			
			if turn =='X' and move == 'topL':
				p1 = Point(1.25,5.25)
				p2 = Point(2.75,6.75)
				p3 = Point(1.25,6.75)
				p4 = Point(2.75,5.25)
				line1 = Line(p1,p2)
				line2 = Line(p3,p4)
				line1.setOutline('red')
				line2.setOutline('red')
				line1.setWidth(3)
				line2.setWidth(3)
				line1.draw(win)
				line2.draw(win)

				#draw_X(p1,p2,p3,p4)
			if turn == '0' and move == 'topL' :
				centre = Point(2,6)
				my_circle = Circle(centre, 0.75)
				my_circle.setOutline('blue')
				my_circle.setWidth(3)
				my_circle.draw(win)

				#draw_O(centre,1.25)

			if turn == 'X' and move == 'topM':
				p1 = Point(3.25,5.25)
				p2 = Point(4.75,6.75)
				p3 = Point(3.25,6.75)
				p4 = Point(4.75,5.25)
				line1 = Line(p1,p2)
				line2 = Line(p3,p4)
				line1.setOutline('red')
				line2.setOutline('red')
				line1.setWidth(3)
				line2.setWidth(3)

				line1.draw(win)
				line2.draw(win)

				#draw_X(p1,p2,p3,p4)
			if turn == '0' and move == 'topM' :
				centre = Point(4,6)
				my_circle = Circle(centre, 0.75)
				my_circle.setOutline('blue')
				my_circle.setWidth(3)
				my_circle.draw(win)

				#draw_O(centre,1.25)
			
			if turn == 'X' and move == 'topR':
				p1 = Point(5.25,5.25)
				p2 = Point(6.75,6.75)
				p3 = Point(5.25,6.75)
				p4 = Point(6.75,5.25)
				line1 = Line(p1,p2)
				line2 = Line(p3,p4)
				line1.setOutline('red')
				line2.setOutline('red')
				line1.setWidth(3)
				line2.setWidth(3)

				line1.draw(win)
				line2.draw(win)

				#draw_X(p1,p2,p3,p4)
			if turn == '0' and move == 'topR' :
				centre = Point(6,6)
				my_circle = Circle(centre, 0.75)
				my_circle.setOutline('blue')
				my_circle.setWidth(3)
				my_circle.draw(win)

				#draw_O(centre,1.25)

			if turn == 'X' and move == 'midL':
				p1 = Point(1.25,3.25)
				p2 = Point(2.75,4.75)
				p3 = Point(1.25,4.75)
				p4 = Point(2.75,3.25)
				line1 = Line(p1,p2)
				line2 = Line(p3,p4)
				line1.setOutline('red')
				line2.setOutline('red')
				line1.setWidth(3)
				line2.setWidth(3)

				line1.draw(win)
				line2.draw(win)

				#draw_X(p1,p2,p3,p4)
			if turn == '0' and move == 'midL' :
				centre = Point(2,4)
				my_circle = Circle(centre, 0.75)
				my_circle.setOutline('blue')
				my_circle.setWidth(3)
				my_circle.draw(win)

				#draw_O(centre,1.25)

			if turn == 'X' and move == 'midM':
				p1 = Point(3.25,3.25)
				p2 = Point(4.75,4.75)
				p3 = Point(3.25,4.75)
				p4 = Point(4.75,3.25)
				line1 = Line(p1,p2)
				line2 = Line(p3,p4)
				line1.setOutline('red')
				line2.setOutline('red')
				line1.setWidth(3)
				line2.setWidth(3)

				line1.draw(win)
				line2.draw(win)

				#draw_X(p1,p2,p3,p4)
			if turn == '0' and move == 'midM' :
				centre = Point(4,4)
				my_circle = Circle(centre, 0.75)
				my_circle.setOutline('blue')
				my_circle.setWidth(3)
				my_circle.draw(win)

				#draw_O(centre,1.25)

			if turn == 'X' and move == 'midR':
				p1 = Point(5.25,3.25)
				p2 = Point(6.75,4.75)
				p3 = Point(5.25,4.75)
				p4 = Point(6.75,3.25)
				line1 = Line(p1,p2)
				line2 = Line(p3,p4)
				line1.setOutline('red')
				line2.setOutline('red')
				line1.setWidth(3)
				line2.setWidth(3)

				line1.draw(win)
				line2.draw(win)

				#draw_X(p1,p2,p3,p4)
			if turn == '0' and move == 'midR' :
				centre = Point(6,4)
				my_circle = Circle(centre, 0.75)
				my_circle.setOutline('blue')
				my_circle.setWidth(3)
				my_circle.draw(win)

				#draw_O(centre,1.25)

			if turn == 'X' and move == 'lowL':
				p1 = Point(1.25,1.25)
				p2 = Point(2.75,2.75)
				p3 = Point(1.25,2.75)
				p4 = Point(2.75,1.25)
				line1 = Line(p1,p2)
				line2 = Line(p3,p4)
				line1.setOutline('red')
				line2.setOutline('red')
				line1.setWidth(3)
				line2.setWidth(3)

				line1.draw(win)
				line2.draw(win)

				#draw_X(p1,p2,p3,p4)
			if turn == '0' and move == 'lowL' :
				centre = Point(2,2)
				my_circle = Circle(centre, 0.75)
				my_circle.setOutline('blue')
				my_circle.setWidth(3)
				my_circle.draw(win)

				#draw_O(centre,1.25)

			if turn == 'X' and move == 'lowM':
				p1 = Point(3.25,1.25)
				p2 = Point(4.75,2.75)
				p3 = Point(3.25,2.75)
				p4 = Point(4.75,1.25)
				line1 = Line(p1,p2)
				line2 = Line(p3,p4)
				line1.setOutline('red')
				line2.setOutline('red')
				line1.setWidth(3)
				line2.setWidth(3)

				line1.draw(win)
				line2.draw(win)

				#draw_X(p1,p2,p3,p4)
			if turn == '0' and move == 'lowM' :
				centre = Point(4,2)
				my_circle = Circle(centre, 0.75)
				my_circle.setOutline('blue')
				my_circle.setWidth(3)
				my_circle.draw(win)

				#draw_O(centre,1.25)

			if turn == 'X' and move == 'lowR':
				p1 = Point(5.25,1.25)
				p2 = Point(6.75,2.75)
				p3 = Point(5.25,2.75)
				p4 = Point(6.75,1.25)
				line1 = Line(p1,p2)
				line2 = Line(p3,p4)
				line1.setOutline('red')
				line2.setOutline('red')
				line1.setWidth(3)
				line2.setWidth(3)

				line1.draw(win)
				line2.draw(win)

				#draw_X(p1,p2,p3,p4)
			if turn == '0' and move == 'lowR' :
				centre = Point(6,2)
				my_circle = Circle(centre, 0.75)
				my_circle.setOutline('blue')
				my_circle.setWidth(3)
				my_circle.draw(win)

				#draw_O(centre,1.25)
			if turn == "X":
				turn = "0"
			else:
				turn = "X"
			

			#Check if a player has already won, if yes display result and break.

		if (Board['topL']== Board['topM']==Board['topR']== "X") or (Board['midL']==Board['midM']==Board['midR']=="X") or (Board['lowL']==Board['lowM']==Board['lowR']=="X") or (Board['topL']==Board['midL']==Board['lowL']=="X") or (Board['topM']==Board['midM']==Board['lowM']=="X") or (Board['topR']==Board['midR']==Board['lowR'] =="X") or (Board['topL']==Board['midM']==Board['lowR']=="X") or (Board['topR']==Board['midM']==Board['lowL']=="X"):
		
			flag = 1
			message.setText("Game Over!!! \'X\' Wins")
			#message.draw(win)
			win.getMouse()
			break
		
		if (Board['topL']== Board['topM']==Board['topR']== "0") or (Board['midL']==Board['midM']==Board['midR']=="0") or (Board['lowL']==Board['lowM']==Board['lowR']=="0") or (Board['topL']==Board['midL']==Board['lowL']=="0") or (Board['topM']==Board['midM']==Board['lowM']=="0") or (Board['topR']==Board['midR']==Board['lowR'] =="0") or (Board['topL']==Board['midM']==Board['lowR']=="0") or (Board['topR']==Board['midM']==Board['lowL']=="0"):
		
			flag = 1
			message.setText("Game Over!!! \'0\' Wins")
			#message.draw(win)
			win.getMouse()
			break
		if count == 7:
			message.setText('Game Draw')
win.getMouse()

		
