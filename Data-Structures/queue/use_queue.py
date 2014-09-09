import queue

#create a Q
q = queue.Queue()


#isEmpty()
print q.isEmpty()

#enqueue
for i in range(10,101,10):
	q.enqueue(i)

#show
q.show()

#dequeue
for i in range(3):
	print "dequeue item = ", q.dequeue()

#peek
print "first element = ", q.peek()

#display
q.show()

#size
print "size = ", q.size()


