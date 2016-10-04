####################################### PrototypeMapping class ##############################
## The iterations are represented by objects, which contains the mappings of the iteration. These objects form a linked	##
## list, with each element pointing towards its successor. This reduces memory usage and makes it easier to subsequently	##
## visualise the mappings.																	##
######################################################################################

class PrototypeMapping:
	def __init__(self, previousMapping = None, initPrototypes = None, numberToSortedString = None):
		if(previousMapping == None):
			self.initFirstMapping(initPrototypes, numberToSortedString)
		else:			
			self.iterationCount = previousMapping.iterationCount + 1
			self.previousPrototypeMaps = previousMapping.prototypeMaps
			self.numberToSortedString = previousMapping.numberToSortedString
			
	def initFirstMapping(self, initPrototypes, numberToSortedString):
		self.iterationCount = 1
		self.previousPrototypeMaps = []
		for proto in initPrototypes:
			self.previousPrototypeMaps.append((None, proto))
		self.numberToSortedString = numberToSortedString

	def performMapping(self):
		sources = self.getSortedTargets(self.previousPrototypeMaps)
		self.prototypeMaps = [(prototype, self.calculateTarget(prototype)) for prototype in sources]
		self.prototypeMaps.sort(lambda x,y: cmp(x[1], y[1])) 
		if self.countUniqueTargets(self.prototypeMaps) != self.countUniqueTargets(self.previousPrototypeMaps):
			self.propagateMapping()
		
	def getSortedTargets(self, prototypeMaps):
		return sorted(list(set([protoMap[1] for protoMap in prototypeMaps])))
		
	def calculateTarget(self, prototype):
		high = self.sortString(prototype, False)
		low = self.sortString(prototype, True)
		result = int(high)-int(low)
		return self.numberToSortedString(result)
		
	def sortString(self, given, incrNotDecr):
		return ''.join(sorted(given,reverse=not(incrNotDecr)))
	
	def countUniqueTargets(self, prototypeMaps):
		return len(set(x[1] for x in prototypeMaps))
		
	def propagateMapping(self):
		self.successor = PrototypeMapping(self)
		self.successor.performMapping()
	
	def getNumberOfDigits(self):
		"""Hack, but it always works."""
		return len(self.previousPrototypeMaps[0][1])