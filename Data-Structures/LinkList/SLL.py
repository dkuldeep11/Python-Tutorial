import Node
class LinkList:

	def __init__(self):
		self.head = None

	def isEmpty(self):
		if self.head == None:
			return True

	def add(self, item):
		node = Node.Node(item)
		if self.isEmpty():
			self.head = node
		else:
			node.setNext(self.head)
			self.head = node

		print "Item ", item, " added.."


	def display(self):
		curr = self.head
		while curr != None:
			print curr.getData()
			curr = curr.getNext()

	def remove(self, item):
		prev = None
		curr = self.head
		
		while curr.getData() != item:
			prev = curr
			curr = curr.getNext()
	
		if prev == None:
			self.head = curr.getNext()
		else:
			prev.setNext(curr.getNext())

		print "Item ", item, " removed..."


	def insert(self, pos, item):
		if pos < 1:
			print "Invalid position"
			return
		else:
			temp = Node.Node(item)
			i = 1
			curr = self.head
			prev = None
			while i != pos:
				prev = curr
				curr = curr.getNext()
				i = i + 1

			if prev == None:
				temp.setNext(self.head)
				self.head = temp	
			else:
				prev.setNext(temp)
				temp.setNext(curr)

			print "Item ", item, " inserted at position ", pos



			
	
	def size(self):
		size = 0
		curr = self.head
		while curr != None:
			size = size + 1
			curr = curr.getNext()
		
		return size


	def index(self, item):
		idx = 1
		curr = self.head

		while curr.getData() != item and curr :
			idx = idx + 1
			curr = curr.getNext()

		if idx == 0:
			return -1
		else:
			return idx


	def pop(self, pos=None):
		idx = 1
		prev = None
                curr = self.head

		if pos:
			while idx != pos and curr:
				prev = curr     
				curr = curr.getNext()
				idx = idx + 1
		else:
			while curr.getNext() != None:
				prev = curr     
				curr = curr.getNext()

		if prev == None:
			self.head = curr.getNext()
		else:
			prev.setNext(curr.getNext())

		return curr.getData()
		

	def search(self, item):
		curr = self.head
		while curr and curr.getData() != item:
			curr = curr.getNext()

		if curr != None:
			return True
		return False

	#Bubble Sort
	def sort(self):
		i = self.head
		while i.getNext() != None:
			j = i
			while j.getNext() != None:
				if j.getData() > j.getNext().getData():
					temp = j.getData()
					j.setData(j.getNext().getData())
					j.getNext().setData(temp)


				j = j.getNext()

			i = i.getNext()
	
