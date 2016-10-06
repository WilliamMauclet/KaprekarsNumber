## TreeDrawer

from turtle import *
from types import *


s = 50;
startpos = (20,120)

def drawTree(tree):
	loops = tree['loops']
	del tree['loops']
	
	i = 0
	for key in tree:
		startpos = (20, -300 + i*120)
		myTree = [key, tree[key]]
		drawMyTree(myTree, startpos, 1)
		i += 1


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

up()