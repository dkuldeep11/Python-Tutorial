import vertex

class Graph:
	"""This is Graph class"""

	def __init__(self):
		self.vertices = {}
		self.count = 0

	def addVertex(self, v):
		self.vertices[v] = vertex.Vertex(v)
		self.count = self.count + 1

	def	getVertex(self, k):
		if k in self.vertices:
			return self.vertices[k]
		return None 

	def addEdge(self, u, v, c=0):
		if u not in self.vertices:
			nu = vertex.Vertex(u)
			self.vertices[u] = nu
		if v not in self.vertices:
			nv = vertex.Vertex(v)
			self.vertices[v] = nv

		self.vertices[u].addNeighbour(v, c)

	def getVertices(self):
		return self.vertices.keys()

	def show(self):
		for u in self.getVertices():
			for v in self.vertices[u].getConnections():
				print u, " => ", v

