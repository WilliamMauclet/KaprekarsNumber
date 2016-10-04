## This class traverses the mappings' linked list and builds a number of trees from the mappings.
## The trees are a list of dictionaries

def buildTree(prototypeMapping, tree=None):
	if prototypeMapping.iterationCount == 1:
		newTree = initialTree(prototypeMapping)
	else:
		newTree = {}
		for protoMap in prototypeMapping.prototypeMaps:
			if protoMap[1] not in newTree:
				newTree[protoMap[1]] = [protoMap[0]]
			else:
				newTree[protoMap[1]].append(protoMap[0])
	if hasattr(prototypeMapping, 'successor'):
		return buildTree(prototypeMapping.successor, newTree)
	else:
		return newTree
		

def initialTree(prototypeMapping):
	return dict( (x[1],x[0]) for x in prototypeMapping.prototypeMaps)

	