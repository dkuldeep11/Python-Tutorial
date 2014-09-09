import stack

#creae an object
stack = stack.Stack()

#isEmpty()
print stack.isEmpty()

#display()
stack.display()

#push()
for n in range(0,101,10):
	stack.push(n)

#display()
stack.display()

#pop()
for i in range(5):
	print "popped element", stack.pop()

stack.display()

#peek()
print "top element = ", stack.peek()
stack.display()

print "popped element ", stack.pop()
print "top element = ", stack.peek()
stack.display()
