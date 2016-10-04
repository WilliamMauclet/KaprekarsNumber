#This class prints the mappings with the mappings one below the other.


class MappingsPrinter():

	def __init__(self, digitsNr):
		self.digitsNr = digitsNr
		self.fileWriter = open(str(digitsNr) + '-Digits-Prototypes.txt', 'w')
		
	def printPrototypes(self, prototypes):
		self.fileWriter.write('------PROTOTYPES---------\n')
		self.fileWriter.write('length: ' + str(len(prototypes)) + '\n')
		for proto in prototypes:
			self.fileWriter.write(proto + '\n')

	def printMappings(self, prototypeMapping):
		"""Recursive method"""
		self.printNewMapping(prototypeMapping)
		if hasattr(prototypeMapping, "successor"):
			self.printMappings(prototypeMapping.successor)
		else:
			self.printFinalText(prototypeMapping.iterationCount)

	def printNewMapping(self, prototypeMapping):	
		self.fileWriter.write('\n------------------ITERATION ' + str(prototypeMapping.iterationCount) + '---------------\n')	
		self.fileWriter.write('size image: ' + str(len(set(x[1] for x in prototypeMapping.prototypeMaps))) + '\n')
		for protoMap in prototypeMapping.prototypeMaps:
			self.fileWriter.write(protoMap[0] + ' -> ' + protoMap[1] + '\n')
			
	def printFinalText(self, iterationCount):
		self.fileWriter.write('\n------------------DONE---------------\n')
		self.fileWriter.write('Number of iterations for a Kaprekar number with ' + str(self.digitsNr) + ' digits is: ' + str(iterationCount))
		self.fileWriter.write('\n')
		self.fileWriter.close()	
	