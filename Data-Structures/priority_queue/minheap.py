class MinHeap:
	"""This is a MinHeap class
	"""

	def __init__(self):
		self.items = []

	def add(self, item):
		if self.isEmpty():
			self.items.insert(0,item)
		else:
			self.items.append(item)
			#self.show()
			idx = len(self.items) - 1
			while idx > 0:
				parent = self.getParent(idx)
				#print idx, parent
				if item < self.items[parent]:
					self.items[idx] = self.items[parent]
					idx = parent
					#self.show()
				else:
					break
			self.items[idx] = item


	def peek(self):
		if not self.isEmpty():
			return self.items[0]

	def remove(self, idx=0):
		if not self.isEmpty():
			min = self.items[idx]
			self.items[idx] = self.items[-1]
			self.percolateDown(idx)
			del self.items[-1]
			return min

	def delete(self, item):
		idx = None
		for i, val in enumerate(self.items):
			if val == item:
				idx = i
				break

		if idx:
			self.remove(idx)
				
	def percolateDown(self, idx):
		li = idx * 2 + 1
		ri = idx * 2 + 2

		min = idx

		if min <= (len(self.items) - 2) / 2:
			if li < len(self.items) and self.items[li] < self.items[min]:
				min = li

			if ri < len(self.items) and self.items[ri] < self.items[min]:
				min = ri

			if min == idx:
				return

			self.items[min], self.items[idx] = self.items[idx], self.items[min]
			self.percolateDown(min)
					
			

	def makeMinHeap(self, source_list):
		pass

	def isEmpty(self):
		if not self.items:
			return True
		return False

	def show(self):
		print self.items

	def getLeft(self, idx):
		return 2*idx + 1

	def getRight(self, idx):
		return 2*idx + 2

	def getParent(self, idx):
		return int((idx - 1)/float(2))



def main():
	print "This is main() ..."
	
	min_heap = MinHeap()
	
	#add()
	min_heap.add(20)
	min_heap.show()
	min_heap.add(15)
	min_heap.add(13)
	min_heap.add(10)
	min_heap.add(9)
	min_heap.show()
	#remove
	print min_heap.remove()	
	print "print heap..."
	min_heap.show()

	mh = MinHeap()
	for i in range(0, 7):
		mh.add(10000)

	mh.add(0)
	mh.show()
if __name__ == "__main__":
	main()
