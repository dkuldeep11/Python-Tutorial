import SLL

link_list = SLL.LinkList()

#isEmpty()
print link_list.isEmpty()

#add()
print "Add().."
link_list.add(30)
link_list.add(25)
link_list.add(35)

#display()
print "display()"
link_list.display()

#remove()
print "remove()"
link_list.remove(25)
print "add()"
link_list.add(40)
link_list.add(50)
print "display()"
link_list.display()

#insert()
print "insert()"
link_list.insert(1, 5)
print "dispplay()"
link_list.display()

print "insert()"
link_list.insert(3, 300)
print "display()"
link_list.display()

#size
print "size = ", link_list.size()

#index
print "index of item 5 is ", link_list.index(5)
print "index of item 50 is ", link_list.index(50)
print "index of item 300 is ", link_list.index(300)

#pop
print "popped element = ", link_list.pop()
link_list.display()

#pop(pos)
print "popped element at 3 = ", link_list.pop(3)
link_list.display()


#search
print "search()"
print link_list.search(100)
print link_list.search(50)

#bubble sort
print "bubble sort"
link_list.sort()
link_list.display()

