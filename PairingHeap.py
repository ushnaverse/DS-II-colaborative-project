# Heap structure
class HeapNode:
    # creates a new node
    def __init__(self, key_=None, leftChild_=None, nextSibling_=None):
        # print("obj")
        self.key = key_.priority
        # print(key_)
        self.value = key_.task
        self.todo = key_
        self.leftChild = leftChild_
        self.nextSibling = nextSibling_
        
    # Adds a child and sibling to the node
    def addChild(self, node):
        if(self.leftChild == None):
            self.leftChild = node
        else:
            node.nextSibling = self.leftChild
            self.leftChild = node
# Function to merge two heaps
def Merge(A, B):
    
    # If any of the two-nodes is None
    # the return the not None node
    if(A == None):
        return B
    if(B == None):
        return A

    # To maintain the min heap condition compare
    # the nodes and node with minimum value become
    # parent of the other node
    if(A.key < B.key):
        A.addChild(B)
        return A
    B.addChild(A)
    return B

def TwoPassMerge(node):
    if(node == None or node.nextSibling == None):
        return node
    A = node
    B = node.nextSibling
    newNode = node.nextSibling.nextSibling

    A.nextSibling = None
    B.nextSibling = None

    return Merge(Merge(A, B), TwoPassMerge(newNode))

class PairingHeap:
    def __init__(self):
        self.root = None
        self.size = 0
        self.tasks = []

    # Returns true if root of the tree
    # is None otherwise returns false
    def Empty(self):
        return (self.root == None)

    # Returns the root value of the heap
    def Top(self):
        return (self.root.todo)

    # Function to insert the new node in the heap
    def Insert(self, key):
        self.size+=1
        self.root = Merge(self.root, HeapNode(key))
  
    # Function to delete the root node in heap
    def Delete(self):
        self.root = TwoPassMerge(self.root.leftChild)
        
    def Join(self, other):
        self.root = Merge(self.root, other.root)
    
    def Size(self):
        return self.size
    
    def traverse(self, node):
        if not node:
            return self.tasks
        self.tasks.append(node.todo)
        # print(node.value, node.key)
        # print(self.tasks)
        if node.leftChild:
            self.traverse(node.leftChild)
        if node.nextSibling:
            self.traverse(node.nextSibling)
  
    

# Driver Code
# if __name__ == '__main__':

#     heap1, heap2 = PairingHeap(), PairingHeap()
#     heap2.Insert((5,1))
#     heap2.Insert((2,3))

#     heap2.Insert((6,0))
#     heap1.Insert((8,4))
#     heap1.Insert((4,99))
#     heap1.Insert((4,"hij"))
#     heap1.Insert((4,"'''k'''"))
#     heap1.traverse(heap1.root)
#     # heap1.Join(heap2)
#     print(heap1.Top())
#     heap1.Delete()
#     print(heap1.Top())
#     heap1.Insert((1,6))
#     print(heap2.Top())
#     print(heap1.Top())
#     print(heap1.Empty())