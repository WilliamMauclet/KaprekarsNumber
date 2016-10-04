#!/usr/bin/python

import sys

def initPrototypes(digitsNr):
	prototypes = set()
	
	prototypesNr = (10**digitsNr)-1
	
	for counter in range(0, prototypesNr):
		prototypes.add(numberToSortedString(digitsNr)(counter))
		
	return sorted(list(prototypes))

def numberToSortedString(digitsNr):
	def numberToSortedFixedDigitsString(number): 
		numberString = sortString(str(number), True)
		while len(numberString) < digitsNr:
			numberString = '0' + numberString
		return numberString
	return numberToSortedFixedDigitsString

def sortString(given, incrNotDecr):
	return ''.join(sorted(given,reverse=not(incrNotDecr)))
	
def printPrototypes(fileWriter, prototypes):
	fileWriter.write('------PROTOTYPES---------\n')
	fileWriter.write('length: ' + str(len(prototypes)) + '\n')
	for proto in prototypes:
		fileWriter.write(proto + '\n')

def printMappings(prototypeMapping):
	previousNumberOfPrototypes = prototypeMapping.numberOfPrototypes
	numberOfPrototypes = prototypeMapping.countUniqueTargets()
	
	printNewMapping()

	if(numberOfPrototypes == previousNumberOfPrototypes):
		printFinalText()

def printNewMapping(fileWriter, prototypeMaps):
	fileWriter.write('\n------------------NEW MAP---------------\n')	
	fileWriter.write('size image: ' + str(len(set(x[1] for x in self.prototypeMaps))) + '\n')
	for protoMap in self.prototypeMaps:
		fileWriter.write(protoMap[0] + ' -> ' + protoMap[1] + '\n')

def printFinalText(self, fileWriter, digitsNr, iterationCount):
	fileWriter.write('\n------------------DONE---------------\n')
	fileWriter.write('Number of iterations for a Kaprekar number with ' + str(digitsNr) + ' digits is: ' + str(self.iterationCount))
	fileWriter.write('\n')
	fileWriter.close()
	
####################################### PrototypeMapping class ############################
## The iterations are represented by objects, which contains the mappings of the iteration. These objects form a linked 
## list, with each element pointing towards its successor. This reduces memory usage and makes it easier to subsequently
## visualise the mappings.

class PrototypeMapping:
	def __init__(self, previousMapping = None, initPrototypes = None, numberToSortedString = None):
		if(previousMapping == None):
			self.iterationCount = 1
			self.previousPrototypeMaps = []
			for proto in initPrototypes:
				self.previousPrototypeMaps.append((None, proto))
			self.numberToSortedString = numberToSortedString
		else:			
			self.iterationCount = previousMapping.iterationCount + 1
			self.previousPrototypeMaps = previousMapping.prototypeMaps
			self.numberToSortedString = previousMapping.numberToSortedString

	def performMapping(self):
		sources = self.getSortedTargets(self.previousPrototypeMaps)
		self.prototypeMaps = [(prototype, self.calculateTarget(prototype)) for prototype in sources]
		self.prototypeMaps.sort(lambda x,y: cmp(x[1], y[1])) 
		if self.countUniqueTargets(self.prototypeMaps) != self.countUniqueTargets(self.previousPrototypeMaps):
			self.propagateMapping()
		
	def getSortedTargets(self, prototypeMaps):
		return sorted(list(set([protoMap[1] for protoMap in prototypeMaps])))
		
	def calculateTarget(self, prototype):
		high = sortString(prototype, False)
		low = sortString(prototype, True)
		result = int(high)-int(low)
		return self.numberToSortedString(result)
	
	def countUniqueTargets(self, prototypeMaps):
		return len(set(x[1] for x in prototypeMaps))
		
	def propagateMapping(self):
		self.successor = PrototypeMapping(self)
		self.successor.performMapping()
		
	
####################################### FLOW #########################

# digitsNr = 	int(raw_input('Please choose how many digits you want: '))

# prototypes = initPrototypes(digitsNr)


# fileWriter = open(str(digitsNr) + '-Digits-Prototypes.txt', 'w')
# printPrototypes(fileWriter, prototypes)
	

# hasta quel numero de grupos sigue el mismo
# previousNumberOfPrototypes = 9999999999
# numberOfPrototypes = 1999999
# iterationsCount = 0
# while previousNumberOfPrototypes != numberOfPrototypes:
	# performMapping()
	# printMappings()?
	

	


	
