#!/usr/bin/python

#first find groups up to 9999

def initPrototypes():
	prototypes = set()

	for counter in range(0,9999):
		prototypes.add(numberToSortedString(counter))
		
	return sorted(list(prototypes))

def numberToSortedString(number):
	numberString = sortString(str(number), True)
	while len(numberString) < 4:
		numberString = '0' + numberString
	return numberString

def sortString(given, incrNotDecr):
	return ''.join(sorted(given),reverse=incrNotDecr)

def printPrototypes(prototypes):
	global f
	f.write('------PROTOTYPES---------\n')
	f.write('length: ' + str(len(prototypes)) + '\n')
	for proto in prototypes:
		f.write(proto + '\n')
		
			
def printMappings(nextPrototypeMaps):
	global f
	f.write('\n------------------NEW MAP---------------\n')	
	f.write('size image: ' + str(countImageCardinality(nextPrototypeMaps)) + '\n')
	for protoMap in nextPrototypeMaps:
		f.write(protoMap[0] + ' -> ' + protoMap[1] + '\n')


def makeCalculation(prototype):
	high = sortString(prototype, False)
	low = sortString(prototype, True)
	result = int(high)-int(low)
	return numberToSortedString(result)

def countImageCardinality(prototypeMaps):
	imageProtos = set()
	for protoMap in prototypeMaps:
		imageProtos.add(protoMap[1])
	return len(imageProtos)

def performMapping():
	global nextPrototypeMaps
	prototypeMaps = makeNewList(nextPrototypeMaps)
	nextPrototypeMaps = []

	for prototype in prototypeMaps:
		nextPrototypeMaps.append((prototype, makeCalculation(prototype)))
		
	nextPrototypeMaps.sort(lambda x,y: cmp(x[1], y[1])) 

	printMappings(nextPrototypeMaps)
	
def makeNewList(prototypeMaps):
	return sorted(list(set([protoMap[1] for protoMap in prototypeMaps])))

	
####################################### FLOW #########################

prototypes = initPrototypes()
		
f = open('prototypes.txt', 'w')
printPrototypes(prototypes)
	
#Now calculate mappings breadth-first	
nextPrototypeMaps = []
for proto in prototypes:
	nextPrototypeMaps.append((None, proto))

for i in range(1,8):
	performMapping()



	


	
