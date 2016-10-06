#!/usr/bin/python

import sys, prototypemapping, mappingsprinter, treebuilder, treedrawer

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
	

def createFirstMapping(digitsNr):
	return prototypemapping.PrototypeMapping(None, initPrototypes(digitsNr), numberToSortedString(digitsNr))

def printMapping(prototypeMapping):
	mappingsPrinter = mappingsprinter.MappingsPrinter(prototypeMapping.getNumberOfDigits())
	mappingsPrinter.printMappings(prototypeMapping)


	
	
first = createFirstMapping(2)
first.performMapping()
printMapping(first)

tree = treebuilder.buildTree(first)
treedrawer.drawTree(tree)
	
