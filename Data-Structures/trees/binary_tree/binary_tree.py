import tree_node
import stack

class BinaryTree:
	"""This is Binary Tree Class
	ADT:
	isEmpty()
	insert()
	traverse() - inorder, preorder, postorder
	search()
	delete()
	"""
	
	def __init__(self, item=None):
		"""This is constructor"""
		self.root = tree_node.Node(item)
		
	def isEmpty(self):
		"""Function isEmpty
		returns True/False
		"""
		return self.root == None

	def insert(self, item):
		"""This is insert function
		It inserts the item in BST way
		"""
		if self.isEmpty():
			self.root = tree_node.Node(item)
		else:
			self.insertHelper(self.root, item)

	def insertHelper(self, node, item):
		"""This is a function
		It is used by insert() function in recursive way to insert an item in BST way
		"""
		#print item, node.getData()
		if item <= node.getData():
			if not node.getLeft():
				node.setLeft(tree_node.Node(item))
				#node.show()
			else:
				self.insertHelper(node.getLeft(), item) 
		else:
			if not node.getRight():
				node.setRight(tree_node.Node(item))
			else:
				self.insertHelper(node.getRight(), item)

	def preorder(self, node):
		"""This is a preorder function
		It prints the tree data in LDR way
		"""
		if not node:
			return
		print node.getData()
		self.preorder(node.getLeft())
		self.preorder(node.getRight())

	def inorder(self, node):
		"""This is a inorder function
		It prints the tree data in LDR way
		"""
		if not node:
			return
		self.inorder(node.getLeft())
		print node.getData()
		self.inorder(node.getRight())

	def postorder(self, node):
		"""This is a postorder function
		It prints the tree data in LDR way
		"""
		if not node:
			return
		self.postorder(node.getLeft())
		self.postorder(node.getRight())
		print node.getData()

	def traverse(self, type):
		"""This is traverse function
		type = 1-pre, 2-in, 3-post
		"""
		if type == 1:
			self.preorder(self.root)
		elif type == 2:
			self.inorder(self.root)
		else:
			self.postorder(self.root)

	def traverse_NR(self, type):
		"""This is traverse function
		type = 1-pre, 2-in, 3-post
		"""
		if type == 1:
			self.preorder_NR()
		elif type == 2:
			self.inorder_NR()
		else:
			self.postorder_NR()


	def preorder_NR(self):
		"""This is a preorder Non Recursive function
		"""
		stk = stack.Stack()
		stk.push(self.root)
		while(not stk.isEmpty()):
			node = stk.pop()
			print node.getData()
			if node.getRight():
				stk.push(node.getRight())
			if node.getLeft():
				stk.push(node.getLeft())
				
	def inorder_NR(self):
		"""This is a inorder Non Recursive function
		"""
		stk = stack.Stack()
		curr = self.root
		while(1):
			if curr:
				stk.push(curr)
				curr = curr.getLeft()
			else:
				if stk.isEmpty():
					break
				node = stk.pop()
				print node.getData()
				if node.getRight():
					curr = node.getRight()

	def search(self, item):
		if self.root.getData() == item:
			return True
		return self.searchHelper(self.root, item) == True

	def searchHelper(self, node, item):
		if node:
			if node.getData() == item:
				return True
			if self.searchHelper(node.getLeft(), item):
				return True
			return self.searchHelper(node.getRight(), item) == True
