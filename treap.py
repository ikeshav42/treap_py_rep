from random import randrange
 
 
class TreapNode:
    def __init__(self, data, priority=100, left=None, right=None):
        self.data = data
        self.priority = randrange(priority) #set a random priority
        self.left = left
        self.right = right
 
 
def rotateLeft(root):
 
    R = root.right
    X = root.right.left
 
    # rotate
    R.left = root
    root.right = X
 
    # set a new root
    return R
 
 
def rotateRight(root):
 
    L = root.left
    Y = root.left.right
 
    # rotate
    L.right = root
    root.left = Y
 
    # set a new root
    return L
 

def insertNode(root, data):
 
    if root is None:
        return TreapNode(data)
 
    # if the given data is less than the root node, insert in the left subtree else, insert in the right subtree
    if data < root.data:
        root.left = insertNode(root.left, data)
 
        # rotate right if heap is violated
        if root.left and root.left.priority > root.priority:
            root = rotateRight(root)
    else:
        root.right = insertNode(root.right, data)
 
        # rotate left if heap is violated
        if root.right and root.right.priority > root.priority:
            root = rotateLeft(root)
 
    return root
 
 
def searchNode(root, key):
 
    
    if root is None: # if the key is not present in the tree
        return False
 
    
    if root.data == key: # if the key is found
        return True
 
    
    if key < root.data: # if the key is less than the root node, search in the left subtree
        return searchNode(root.left, key)
 
    
    return searchNode(root.right, key) # otherwise, search in the right subtree
 
 
def deleteNode(root, key):
 
    
    if root is None: # base case: the key is not found in the tree
        return None
 
    
    if key < root.data: # if the key is less than the root node, recur for the left subtree
        root.left = deleteNode(root.left, key)
 
    
    elif key > root.data: # if the key is more than the root node, recur for the right subtree
        root.right = deleteNode(root.right, key)
 
    
    else:
 
        
        if root.left is None and root.right is None: # It is a leaf node
            root = None
 
        
        elif root.left and root.right: # Node to be deleted has two children
            
            if root.left.priority < root.right.priority: # left child has less priority than the right child
                root = rotateLeft(root)
                root.left = deleteNode(root.left, key) # delete left node
            else:
                root = rotateRight(root)
                root.right = deleteNode(root.right, key) # delete right node
 
        else: # only one child
            child = root.left if (root.left) else root.right
            root = child
 
    return root

def printTreap(root, space):
 
    if root is None:
        return

    printTreap(root.left, space)
    print((root.data, root.priority))
    printTreap(root.right, space)
    
 
 
if __name__ == '__main__':
 
    keys = [5, 2, 1, 4, 9, 8, 10]

    root = None
    for key in keys:
        root = insertNode(root, key)
 
    print("Constructed treap :\n")
    printTreap(root, 0)
 
    print("\nDeleting node 1:\n\n")
    root = deleteNode(root, 1)
    printTreap(root, 0)
 
    print("\nDeleting node 6:\n\n")
    root = deleteNode(root, 6)
    printTreap(root, 0)
 
    print("\nDeleting node 9:\n\n")
    root = deleteNode(root, 9)
 
    printTreap(root, 0)