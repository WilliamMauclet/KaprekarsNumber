## TreeDrawer

from turtle import *
from types import *
from math import sqrt


s = 50;

rootPositions = {}

## start keeping the positions of tree roots

def drawTree(tree):
	up()
	loops = tree['loops']
	del tree['loops']
	speed('fastest')
	
	i = 0
	for key in tree:
		rootPosition = (200*i,  i*1000)
		rootPositions[key] = rootPosition
		myTree = [key, tree[key]]
		drawMyTree(myTree, rootPosition, 1)
		i += 1
	
	drawLoops(loops)
	up()

def cntstrs(list):
	return len([item for item in list if type(item) is StringType])
	
def drawMyTree(tree, pos, head=0):
	c = cntstrs(tree)
	while len(tree):
		goto(pos)
		item = tree.pop(0)
		if head:
			write(item,1)
			drawMyTree(tree.pop(0),pos)
		else:
			if type(item) is StringType:
				newpos = (pos[0] + s*c/4 - s*cntstrs(tree), pos[1] - s)
				down()
				goto((newpos[0], newpos[1] + 15))
				up()
				goto(newpos)
				write(item,1)
			elif type(item) is ListType:
				drawMyTree(item,newpos)
		
def drawLoops(loops):
	for loop in loops:
		for i in range(len(loop)):
			drawArc(rootPositions[loop[i]], rootPositions[loop[(i+1)%len(loop)]])
			
def drawArc(posOne, posTwo):
	color("red")
	setpos(posOne[0], posOne[1])
	
	down()
	if posOne == posTwo:
		circle(20)
		drawArrowHead()
		up()
		return
	
	## 114.59 is the radius of a cirle for _ range(180): forward(1); left(1)
	forwardIncrement = abs((posTwo[1] - posOne[1]) / 114.59)
	
	leftNotRight = (heading() == 0) != (posTwo[1] < posOne[1])
	
	directionTurn = left if leftNotRight else right
	
	for _ in range(180):
		directionTurn(1)
		forward(forwardIncrement)
	drawArrowHead()
	up()

def drawArrowHead():
	BREADTH_TRIANGLE = 10
	forward(-BREADTH_TRIANGLE)
	fill(True)
	left(90)
	forward(BREADTH_TRIANGLE)
	right(135)
	forward(sqrt(2)*BREADTH_TRIANGLE)
	right(90)
	forward(sqrt(2)*BREADTH_TRIANGLE)
	right(135)
	forward(BREADTH_TRIANGLE)
	right(90)
	fill(False)
	forward(BREADTH_TRIANGLE)