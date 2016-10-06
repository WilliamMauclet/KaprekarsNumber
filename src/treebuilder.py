## This class traverses the mappings' linked list and builds a number of trees from the mappings.
## The trees are a list of dictionaries

def buildTree(prototypeMapping):
	tree = initialTree(prototypeMapping)
	if not hasattr(prototypeMapping, 'successor'):
		return tree
	else:
		return growTree(prototypeMapping.successor, tree)
	
def initialTree(prototypeMapping):
	firstDictionary = {}
	for protoMap in prototypeMapping.prototypeMaps:
		if protoMap[1] not in firstDictionary:
			firstDictionary[protoMap[1]] = [protoMap[0]]
		else:
			firstDictionary[protoMap[1]].append(protoMap[0])
	return firstDictionary
	
def growTree(prototypeMapping, tree):
	if hasattr(prototypeMapping, 'successor'):
		newTree = {}
		for protoMap in prototypeMapping.prototypeMaps:
			payload = tree[protoMap[0]]
			if protoMap[1] not in newTree:
				newTree[protoMap[1]] = [[protoMap[0], payload]]
			else:
				newTree[protoMap[1]].append([protoMap[0], payload])
		return growTree(prototypeMapping.successor, newTree)
	else:
		tree["loops"] = prototypeMapping.loops
		return tree


	
# HOW A TREE SHOULD BE BUILT:  => always dictionary
# 1->2		3->1		
# 2->3		4->2		
# 3->1		2->3		
# 4->2
# 5->4

# >>>

# {
	# 1:[3]
	# 2:[1,4],
	# 3:[2],
	# 4:[5]
# }

# >>>

# {
	# 1:[3,[2]],
	# 2:[4,[5]],
	# 3:[2,[1,4]]
# }

# >>>

# [1,[3,[2]]]
# [2,[4,[5]]]
# [3,[2,[1,4]]]

# ADD LOOPS

	