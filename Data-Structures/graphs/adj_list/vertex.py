class Vertex:
	"""This is the class of Vertx for a graph
	"""

	def __init__(self, value=None):
		"""This is constructor:
		class has 2 attributes- 1) id 2) connections dict i.e. vertex->weight
		"""
		self.id = value
		self.connections = {}


	def addNeighbour(self, nbr, wt=0):
		self.connections[nbr] = wt

	def getWeight(self, nbr):
		if nbr in self.connections:
			return self.connections[nbr]
		return None

	def getConnections(self):
		return self.connections.keys()

	def getId(self):
		return self.id
	
