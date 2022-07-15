class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

def printE(root):
    if root:
        if root.left == None and root.right == None:
            print(root.val,end='')
        else:
           print('(',end='')
           printE(root.left)
           print(root.val,end='')
           printE(root.right)
           print(')',end='')
         
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.val,end='')
        printInorder(root.right)
        
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val,end='')
   
def printPreorder(root):
    if root:

       print(root.val,end='')
       printPreorder(root.left)
       printPreorder(root.right)

def calculate(root):
    if root:
        if(root.val == '-'):
            return calculate(root.left) - calculate(root.right)
        elif(root.val == '*'):
            return calculate(root.left) * calculate(root.right)
        elif(root.val == '/'):
            return calculate(root.left) / calculate(root.right)
        elif(root.val == '+'):
            return calculate(root.left) + calculate(root.right)
        else:
            return int(root.val)

def height(root):
    if root:
        h = max(height(root.left),height(root.right))
        return h + 1
    else:
        return 0

stack = []
express = "31+3*95-2+/374-*6+-"
for i in range(0,len(express)):
    if express[i] == '+' or express[i] == '-' or express[i] == '*' or express[i] == '/':
        right = stack.pop()
        left = stack.pop()
        newnode = Node(express[i])
        newnode.left = left
        newnode.right = right
        stack.append(newnode)
    else:
        newnode = Node(express[i])
        stack.append(newnode)
root = stack.pop()
print ("Preorder traversal of binary tree is")
printPreorder(root)
print ("\nInorder traversal of binary tree is")
printInorder(root)
print ("\nPostorder traversal of binary tree is")
printPostorder(root)
print ("\nEtraversal of binary tree is")
printE(root)
print(f"={int(calculate(root))}")
print(height(root))