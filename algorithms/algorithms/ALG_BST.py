import math
 
# We traverse the array from right to left and insert all elements in an AVL tree. 
# While inserting a new key in an AVL tree, first compare the key with the root. If the key is greater than the root, then it is greater than all the nodes in the left subtree of the root. 
# So we add the size of the left subtree to the count of smaller elements for the key being inserted. 
# We recursively follow the same approach for all nodes down the root. 

class S_balanced_BST:
    def __init__(self) -> None:
        pass
    # An AVL tree node
    class node:
        key = 0
        left = None
        right = None
        height = 0
        # size of the tree rooted
        # with this node
        size = 0
    countSmaller = None
    count = 0
    # A utility function to get
    # height of the tree rooted with N
    
    @staticmethod
    def height(N):
        if (N == None):
            return 0
        return N.height
    # A utility function to size
    # of the tree of rooted with N

    @staticmethod
    def size(N):
        if (N == None):
            return 0
        return N.size
    # A utility function to
    # get maximum of two integers

    @staticmethod
    def max(a,  b):
        return a if (a > b) else b
    # Helper function that allocates a
    # new node with the given key and
    # null left and right pointers.

    @staticmethod
    def newNode(key):
        node = S_balanced_BST.node()
        node.key = key
        node.left = None
        node.right = None
        # New node is initially added at leaf
        node.height = 1
        node.size = 1
        return (node)
    # A utility function to right rotate
    # subtree rooted with y

    @staticmethod
    def rightRotate(y):
        x = y.left
        T2 = x.right
        # Perform rotation
        x.right = y
        y.left = T2
        # Update heights
        y.height = max(S_balanced_BST.height(y.left), S_balanced_BST.height(y.right)) + 1
        x.height = max(S_balanced_BST.height(x.left), S_balanced_BST.height(x.right)) + 1
        # Update sizes
        y.size = S_balanced_BST.size(y.left) + S_balanced_BST.size(y.right) + 1
        x.size = S_balanced_BST.size(x.left) + S_balanced_BST.size(x.right) + 1
        # Return new root
        return x
    # A utility function to left rotate
    # subtree rooted with x

    @staticmethod
    def leftRotate(x):
        y = x.right
        T2 = y.left
        # Perform rotation
        y.left = x
        x.right = T2
        #  Update heights
        x.height = max(S_balanced_BST.height(x.left), S_balanced_BST.height(x.right)) + 1
        y.height = max(S_balanced_BST.height(y.left), S_balanced_BST.height(y.right)) + 1
        # Update sizes
        x.size = S_balanced_BST.size(x.left) + S_balanced_BST.size(x.right) + 1
        y.size = S_balanced_BST.size(y.left) + S_balanced_BST.size(y.right) + 1
        # Return new root
        return y
    # Get Balance factor of node N

    @staticmethod
    def getBalance(N):
        if (N == None):
            return 0
        return S_balanced_BST.height(N.left) - S_balanced_BST.height(N.right)
    # Inserts a new key to the tree rotted with
    # node. Also, updates *count to contain count
    # of smaller elements for the new key

    @staticmethod
    def insert(node,  key,  count):
        # 1. Perform the normal BST rotation
        if (node == None):
            return (S_balanced_BST.newNode(key))
        if (key < node.key):
            node.left = S_balanced_BST.insert(node.left, key, count)
        else:
            node.right = S_balanced_BST.insert(node.right, key, count)
            # UPDATE COUNT OF SMALLER ELEMENTS FOR KEY
            S_balanced_BST.countSmaller[count] = S_balanced_BST.countSmaller[count] + \
                S_balanced_BST.size(node.left) + 1
        # 2.Update height and size of this ancestor node
        node.height = max(S_balanced_BST.height(node.left), S_balanced_BST.height(node.right)) + 1
        node.size = S_balanced_BST.size(node.left) + S_balanced_BST.size(node.right) + 1
        # 3. Get the balance factor of this
        # ancestor node to check whether this
        # node became unbalanced
        balance = S_balanced_BST.getBalance(node)
        # If this node becomes unbalanced,
        # then there are 4 cases
        # Left Left Case
        if (balance > 1 and key < node.left.key):
            return S_balanced_BST.rightRotate(node)
        # Right Right Case
        if (balance < -1 and key > node.right.key):
            return S_balanced_BST.leftRotate(node)
        # Left Right Case
        if (balance > 1 and key > node.left.key):
            node.left = S_balanced_BST.leftRotate(node.left)
            return S_balanced_BST.rightRotate(node)
        # Right Left Case
        if (balance < -1 and key < node.right.key):
            node.right = S_balanced_BST.rightRotate(node.right)
            return S_balanced_BST.leftRotate(node)
        # Return the (unchanged) node pointer
        return node
    # The following function updates the
    # countSmaller array to contain count of
    # smaller elements on right side.

    @staticmethod
    def constructLowerArray(arr,  n):
        i = 0
        j = 0
        root = None
        # Initialize all the counts in
        # countSmaller array as 0
        i = 0
        while (i < n):
            S_balanced_BST.countSmaller[i] = 0
            i += 1
        # Starting from rightmost element,
        # insert all elements one by one in
        # an AVL tree and get the count of
        # smaller elements
        i = n - 1
        while (i >= 0):
            root = S_balanced_BST.insert(root, arr[i], i)
            i -= 1
    # Utility function that prints out an
    # array on a line

    @staticmethod
    def printArray(arr,  size):
        i = 0
        print("\n", end="")
        i = 0
        while (i < size):
            print(str(arr[i]) + " ", end="")
            i += 1
    # Driver code

    @staticmethod
    def main(args):
        arr = [4, 3, 0, 1, 0]
        n = len(arr)
        S_balanced_BST.countSmaller = [0] * (n)
        S_balanced_BST.constructLowerArray(arr, n)
        S_balanced_BST.printArray(S_balanced_BST.countSmaller, n)


if __name__ == "__main__":
    S_balanced_BST.main([])