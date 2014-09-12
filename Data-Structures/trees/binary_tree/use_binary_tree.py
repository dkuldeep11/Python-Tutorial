import binary_tree

#create object
bt1 = binary_tree.BinaryTree(20)
bt1.insert(18)
bt1.insert(25)
bt1.insert(30)
bt1.insert(23)
bt1.insert(10)
bt1.insert(19)
print "inorder"
bt1.traverse(2) #1-preorder, 2-inorder, 3-postorder
print "preorder"
bt1.traverse(1) #1-preorder, 2-inorder, 3-postorder
print "postorder"
bt1.traverse(3) #1-preorder, 2-inorder, 3-postorder
print bt1.search(100)
for i in (18,25,30,20,23,10,19):
	print bt1.search(i)

print "preorder NR"
bt1.traverse_NR(1)
print "inorder NR"
bt1.traverse_NR(2)



