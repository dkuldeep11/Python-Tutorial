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

	def remove(self, item):
		"""This is a remove function which uses removeHelper recursive nction
		"""
		if self.root.getData() == item:
			self.root = null
		else:
			return self.removeHelper(self.root, item) != False

	def removeHelper(self, node, item):
		if not node:
			return None

		print node.getData(), item
		#go to left
		if node.getData() < item:
			node.setRight(self.removeHelper(node.getRight(), item))	
			return node
		#go to right
		elif node.getData() > item:
			node.setLeft(self.removeHelper(node.getLeft(), item))
			return node
		else:
			#found it
			print "got it", node.getData(), item, node.getLeft(), node.getRight()
			#case: leaf node
			if not (node.getLeft() and node.getRight()):
				print "this case"
				return None
			elif not node.getLeft():
				#only has right child
				temp = node.getRight()
				return temp
			elif not node.getRight():
				#only left is present
				temp = node.getLeft()
				return temp
			else:
				#both are present
				temp = self.getMax(node.getLeft())
				node.setData = temp.getData()
				node.setLeft(self.removeHelper(node.getLeft(), temp.getData()))
				return node

	def getMax(self, node):
		"""get max value node"""
		while(node.getRight() != None):
			node = node.getRight()

		return node

	def getMin(self, node):
		"""this is the function to get min value node from the tree below the given node
		"""
		while(node.getLeft() != None):
			node = node.getLeft()

		return node

	def BFS(self):
		"""This is the function for BFS traversal
		"""
		import queue
		Q = queue.Queue()
		Q.enqueue(self.root)
		#l1 = [self.root]
		while not Q.isEmpty():
		#while len(l1) > 0:
			#print "Q is ", Q.show()
			node = Q.dequeue()
			#node = l1[0]
			#del l1[0]
			print node.getData()
		
			if node.getLeft():
				#print "putting in Q ", node.getLeft().getData()
				Q.enqueue(node.getLeft())
				#l1.append(node.getLeft())
			if node.getRight():
				#print "putting in Q ", node.getRight().getData()
				Q.enqueue(node.getRight())
				#l1.append(node.getRight())

	def count(self):
		if self.isEmpty():
			return 0
		return self.countHelper(self.root)

	def countHelper(self, node):
		if not node:
			return 0
		return 1 + self.countHelper(node.getLeft()) + self.countHelper(node.getRight())

	
	def height(self):
		if self.isEmpty():
			return 0
		return self.heightHelper(self.root)

	def heightHelper(self, node):
		if not node or not (node.getLeft() and node.getRight()):
			return 0
		#return 1 + self.max(self.heightHelper(node.getLeft()), self.heightHelper(node.getRight())
		return 1 + self.max(self.heightHelper(node.getLeft()), self.heightHelper(node.getRight()))

	def max(self, a, b):
		return a if a > b else b
