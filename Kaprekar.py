#!/usr/bin/python

import sys

digitsNr = 	int(raw_input('Please choose how many digits you want: '))

def initPrototypes():
	prototypes = set()
	
	global digitsNr
	prototypesNr = (10**digitsNr)-1
	
	for counter in range(0, prototypesNr):
		prototypes.add(numberToSortedString(counter))
		
	return sorted(list(prototypes))

def numberToSortedString(number):
	numberString = sortString(str(number), True)
	while len(numberString) < digitsNr:
		numberString = '0' + numberString
	return numberString

def sortString(given, incrNotDecr):
	return ''.join(sorted(given,reverse=not(incrNotDecr)))
	
def printPrototypes(prototypes):
	global f
	f.write('------PROTOTYPES---------\n')
	f.write('length: ' + str(len(prototypes)) + '\n')
	for proto in prototypes:
		f.write(proto + '\n')
		
			
def printMappings(nextPrototypeMaps):
	global f, previousNumberOfPrototypes, numberOfPrototypes, iterationsCount
	previousNumberOfPrototypes = numberOfPrototypes
	numberOfPrototypes = countImageCardinality(nextPrototypeMaps)

	printNewMapping(numberOfPrototypes, nextPrototypeMaps)

	if(numberOfPrototypes == previousNumberOfPrototypes):
		printFinalText()
		return
	iterationsCount += 1
	
def printNewMapping():
	f.write('\n------------------NEW MAP---------------\n')	
	f.write('size image: ' + str(numberOfPrototypes) + '\n')
	for protoMap in nextPrototypeMaps:
		f.write(protoMap[0] + ' -> ' + protoMap[1] + '\n')
		
def printFinalText():
	global f, iterationsCount, digitsNr
	f.write('\n------------------DONE---------------\n')
	f.write('Number of iterations for a Kaprekar number with ' + str(digitsNr) + ' digits is: ' + str(iterationsCount))
	f.write('\n')
	f.close()
	
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
		
f = open(str(digitsNr) + '-Digits-Prototypes.txt', 'w')
printPrototypes(prototypes)
	
#Now calculate mappings breadth-first	
nextPrototypeMaps = []
for proto in prototypes:
	nextPrototypeMaps.append((None, proto))

# hasta quel numero de grupos sigue el mismo
previousNumberOfPrototypes = 9999999999
numberOfPrototypes = 1999999
iterationsCount = 0
while previousNumberOfPrototypes != numberOfPrototypes:
	performMapping()




	


	
