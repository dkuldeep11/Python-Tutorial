class Graph:
	"""This is a graph class using dictionary
	"""
	
	def __init__(self):
		self.vertices = {}

	def addVertex(self, item):
		self.vertices[item] = {}

	def removeVertex(self, item):
		if item in self.vertices:
			#remove vertex from vertices
			del self.vertices[item]

			#remove the relevant edges
			for u in self.vertices:
				if item in self.vertices[u]:
					del self.vertices[u][item]

	def addEdge(self, u, v, wt=0):
		if u not in self.vertices:
			self.addVertex(u)
		if v not in self.vertices:
			self.addVertex(v)

		self.vertices[u][v] = wt
		self.vertices[v][u] = wt

	def removeEdge(self, u, v):
		if u in self.vertices and v in self.vertices:
			del self.vertices[u][v]
			del self.vertices[v][u]

	def getVertex(self, u):
		if u in self.vertices:
			return self.vertices[u]

		return None

	def getVertices(self):
		return self.vertices.keys()

	def getAdjacent(self, u):
		return self.vertices[u].keys()

	def show(self):
		for u in self.vertices.keys():
			s1 = str(u) + " => "
			for v in self.vertices[u]:
				s1 = s1 + str(v) + ":" + str(self.vertices[u][v]) + ", "

			print s1[:-2]

	def bfs(self, start):
		"""This is a function for BFS"""
		import queue

		q = queue.Queue()
		q.enqueue(start)
		visited = [start]

		while not q.isEmpty():
			u = q.dequeue()
			print u

			for v in self.vertices[u]:
				if v not in visited:
					q.enqueue(v)
					visited.append(v)

	def dfs(self, start):
		"""This is a function for DFS"""
		import stack

		s = stack.Stack()
		s.push(start)		
		visited = [start]

		while not s.isEmpty():
			u = s.pop()
			print u

			for v in self.vertices[u]:
				if v not in visited:
					visited.append(v)
					s.push(v)


	def dijkstra(self, start):
		dist = {}
		prev = {}
		visited = []
		import minheap
		min_heap = minheap.MinHeap()

		#initialize section
		for u in self.getVertices():
			if u != start:
				dist[u] = 10000
				prev[u] = None
				min_heap.add(10000)

		dist[start] = 0
		visited.append(start)
		min_heap.add(dist[start])
		min_heap.show()
		#actual algo
		#while not min_heap.isEmpty():
		while len(visited) != len(self.vertices):
			min_dist = min_heap.remove()
			u = 0
			for k in dist.keys():
				if dist[k] == min_dist:
					u = k
					break

			visited.append(u)

			for v in self.getAdjacent(u):
				if v not in visited:
					print u, "->", v
					temp = dist[u] + self.vertices[u][v]
					if temp < dist[v]:
						min_heap.delete(dist[v])
						dist[v] = temp
						prev[v] = u	
						min_heap.add(dist[v])
			print "after ", u
			print dist
			min_heap.show()
	
		print prev
		print dist

		for node in self.getVertices():
			if node != start:
				l1 = []
				curr = node
				while curr != start:
					l1.append(curr)
					curr = prev[curr]
				l1.append(start)
				print "shortes path to node ", node, " from ", start, " is ", l1[::-1]


def main():
	g = Graph()
	g.addEdge(1,2)
	g.addEdge(1,3)	
	g.addEdge(1,4)	
	g.addEdge(2,5)	
	g.addEdge(3,5)	
	g.addEdge(3,6)	
	g.addEdge(4,6)	

	g.show()

	#getVertex
	d1 = g.getVertex(1)
	print d1

	#getVertices
	print g.getVertices()

	#removeVertex
	g.removeVertex(3)
	g.show()

	#remove edge
	g.removeEdge(4, 6)
	g.show()

	g.addEdge(1,2,6)
	g.addEdge(1,3,7)	
	g.addEdge(1,4,8)	
	g.addEdge(2,5,5)	
	g.addEdge(3,5,2)	
	g.addEdge(3,6,3)	
	g.addEdge(4,6,3)	
	g.addEdge(5,7,3)	
	g.addEdge(6,7,1)	
	print "Reset the graph..."
	g.show()

	#bfs
	print "BFS..."
	g.bfs(1)
	
	#dfs
	print "DFS..."
	g.dfs(1)

	#dijkstra
	print "dijkstra..."
	g.dijkstra(1)
if __name__ == "__main__":
	main()
		
	
