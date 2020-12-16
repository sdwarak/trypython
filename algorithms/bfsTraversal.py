class Node:
   def __init__(self,data):
       self.left = None
       self.right = None
       self.data = data

def inOrder(node):
   if node:
       inOrder(node.left)
       print (node.data)
       inOrder(node.right)

def preOrder(node):
   if node:
       print (node.data)
       preOrder(node.left)
       preOrder(node.right)

def postOrder(node):
   if node:
       postOrder(node.left)
       postOrder(node.right)
       print (node.data)

#making the tree

#        1
#     2     3
#    4 5
node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)

print(inOrder(node))
#4 2 5 1 3
print(preOrder(node))
#1 2 4 5 3
print(postOrder(node))
#4 5 2 3 1

