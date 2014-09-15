class Node:
	"""This is Binary Tree Node class"""

	def __init__(self, item=None):
		self.data = item
		self.left = None
		self.right = None
		self.height = 0

	def setData(self, item):
		"""This is setter for data"""
		self.data = item

	def getData(self):
		"""This is getter for data"""
		return self.data

	def setLeft(self, item):
		"""This is setter for left"""
		self.left = item

	def getLeft(self):
		"""This is getter for left"""
		return self.left

	def setRight(self, item):
		"""This is setter for right"""
		self.right = item

	def getRight(self):
		"""This is getter for right"""
		return self.right

	def setHeight(self, h):
		self.height = h

	def getHeight(self):
		return self.height

	def show(self):
		s1 = "data = " + str(self.data)
		if self.left:
			s1 = s1 + "left = " + str(self.left.getData())
		if self.right:
			s1 = s1 + "right = " + str(self.right.getData())
		print s1






