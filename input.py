# This file will take continuous input and print accordingly
from graphics import *
import math

def main():
    print """
    Welcome to Plogo
    Plogo is the LOGO langauge implemented in python.
    Uses Tkinter for Graphical interface.
    Developed by 
    ++ Mayuresh Waykole ( 31 October 2015 )

    Hope you have a good time.
    Type your commands below. \n\n
    """
    win = GraphWin("pylogo",700,700)
    win.setCoords(0,0,700,700)
    angle = 90
    turtle= [50,50]
    #Inital angle with respect to origin 

    cmd = "start"
    while cmd != "EXIT":
        cmd = raw_input("### ")
        if cmd=="EXIT":
        	win.close()
        	print "GoodBye, See you again"
        	break

        # Parses the input , generates and sends to draw
        tokens = parse(cmd,angle)

        if tokens[0]:
            angle,turtle = drawOnCanvas(win, angle, turtle, tokens[1])
        else:
            print ">> : Wrong Input"




def parse(cmd,angle):
    """ Returns tokens.
    Token format is as below
    [validity, other parsed tokens...]

    validity=0 => Invalid input 
    validity=1 => Valid input

	FD x 	BK x	LT x	RT x 	--exit
    """
    token = cmd.split()

    if len(token)==2:
        if token[0] in ['FD','BK','RT','LT','CIR']:
        	token[1] = float(token[1])
        	return [1,token]
    else:
        return [0]

    return [0]

def drawOnCanvas(win, angle, turtle, token):
	PI = 3.14159

	if token[0]=='FD':
		x1=turtle[0]  #current x coordinate of turtle
		y1=turtle[1]  # current y coordinate of turtle
		dist = float(token[1])
		x2 =x1+ dist * math.cos((PI*angle)/180)
		y2 =y1+ dist * math.sin((PI*angle)/180)

		p1 = Point(x1,y1)
		p2 = Point(x2,y2)

		line = Line(p1,p2)
		line.draw(win)
		turtle[0] = x2
		turtle[1] = y2

	if token[0]=='BK':
		x1=turtle[0]  #current x coordinate of turtle
		y1=turtle[1]  # current y coordinate of turtle
		dist = float(token[1])
		x2 =x1- dist * math.cos((PI*angle)/180)
		y2 =y1- dist * math.sin((PI*angle)/180)

		p1 = Point(x1,y1)
		p2 = Point(x2,y2)

		line = Line(p1,p2)
		line.draw(win)
		turtle[0] = x2
		turtle[1] = y2

	if token[0]=="CIR":
		radius = token[1]
		x = turtle[0]
		y = turtle[1]
		circle = Circle(Point(x,y),radius)
		circle.draw(win)

	if token[0]=="RT":
		angle -=float(token[1])
		return angle,turtle

	if token[0]=="LT":
		angle+=float(token[1])
		return angle,turtle

	return angle,turtle


if __name__ == '__main__':
	main()