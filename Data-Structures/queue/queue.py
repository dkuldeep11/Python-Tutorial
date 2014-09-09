class Queue:
	"""This is class queue
	ADT:
	Queue
	isEmpty
	enqueue
	dequeue
	peek
	size
	show
	"""

	def __init__(self):
		"""Constructor"""
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		"""This is enqueue function
		input: item
		Adds the item at the front in the items list
		"""
		self.items.insert(0, item)

	def dequeue(self):
		"""This is dequeue function
		returns and deletes the first item from items list
		"""
		if not self.isEmpty():
			item = self.items[0]
			del self.items[0]
			return item
		return None

	def peek(self):
		"""This is peek function
		Returns  the first element from the items list
		"""
		if not self.isEmpty():
			return self.items[0]
		return None

	def size(self):
		"""This is a size function
		Returns the size of Q
		"""
		return len(self.items)

	def show(self):
		"""Displays the Queue"""
		for item in self.items:
			print item	
