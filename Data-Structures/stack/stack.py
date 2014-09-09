class Stack:
	"""This is a Stack class

	ADT is as follows:
	Stack()
	isEmpty()
	push()
	pop()
	peek()

	"""

	def __init__(self):
		"""This is a constructor
		Initialises the emplt list
		"""
		self.items = []
	
	def isEmpty(self):
		"""This is a function isEmpty()
		Returns True if empty else False
		"""
		return self.items == []
 
	def push(self, item):
		"""This is a push function
		Input- item
		Appends the items to the list
		"""
		self.items.append(item)
	
	def pop(self):
		"""This is a pop function
		Returns and delete the last element from items list
		"""
		if self.isEmpty():
			return False
		item = self.items[-1]
		del self.items[-1]
		return item

	def peek(self):
		"""This is a peek function
		Returns the last elemet from items
		"""
		if self.isEmpty():
			return False
		return self.items[-1]

	def display(self):
		"""This is a display function
		Prints the items list
		"""
		for idx in range(len(self.items)-1, 0, -1):
			print self.items[idx]



