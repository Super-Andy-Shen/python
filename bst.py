import math
class Node:
	def __init__(self,key,value):
         self.left = None
         self.right = None
         self.val = key
         self.info = value

def BinarySearch(arr,k,low,high):
     if low <= high :
        mid = (low + high) // 2
        if(k == arr[mid]):
           return mid
        elif(k > arr[mid]):
            return BinarySearch(arr,k,mid + 1,high)
        elif(k < arr[mid]):
            return BinarySearch(arr,k,low,mid - 1)
     else:
         return -1
def insert(root,key,value):
    if root == None:
        root = Node(key,value)
        return root
    else:
        if root.val == key:
           newnode = Node(key,value)
           left = root.left
           root.left = newnode
           newnode.left = left
        elif root.val > key:
            root.left = insert(root.left,key,value)
        else:
            root.right = insert(root.right,key,value)
        return root
def bstsearch(root,key):
    if root == None:
        return None
    else:
        if key == root.val:
            return root.info
        elif key < root.val:
            return bstsearch(root.left,key)
        else:
            return bstsearch(root.right,key)
  
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.info,end='')
        print(" ",end='')
        printInorder(root.right)
def findmin(root,m):
    if root:
        m = root.val
        return findmin(root.left,m)
    else:
        return m
def findmax(root,m):
    if root:
        m = root.val
        return findmax(root.right,m) 
    else:
        return m
    

# A=[1,2,3,4,5,6,7,8,9,10]
# a = BinarySearch(A,11,0,len(A) - 1)
# print(a)
r = Node(50,'d')
r = insert(r, 30,'b')
r = insert(r, 20,'a')
r = insert(r, 40,'c')
r = insert(r, 40,'c')
r = insert(r, 10,'f')
r = insert(r, 50,'e')
r = insert(r, 60,'e')
r = insert(r, 80,'g')
 
# Print inoder traversal of the BST
print(findmin(r,r.val))
print(findmax(r,r.val))