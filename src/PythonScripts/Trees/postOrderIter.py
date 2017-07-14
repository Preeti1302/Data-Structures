
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data



def postOrder(root):
        if root is None:
            return
        
        s1 = []
        s2 = []
        
        s1.append(root)
        
        while(len(s1) >0):
            node = s1.pop()
            s2.append(node)
            
            if(node.left is not None):
                s1.append(node.left)
            if node.right is not None:
                s1.append(node.right)
                
                
        while(len(s2)>0):
            nodeValue = s2.pop()
            print(nodeValue.data)
            
def preorder(root):
    if root is None:
        return
    
    s1 = []
    s1.append(root)
    
    while(len(s1)>0):
        node = s1.pop()
        print(node.data)
        
        if node.right is not None:
            s1.append(node.right)
        if node.left is not None:
            s1.append(node.left)
            
                        
def inorder(root):
    
    if root is None:
        return
    
    s1 = []
    current = root
    done = 0
    while(not done):
            if current is not None:
                s1.append(current)
                current = current.left
            else:
                if(len(s1)>0):
                    current = s1.pop()
                    print(current.data)
                    
                    current = current.right
                else:
                    done = 1
                
            
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
postOrder(root)
print("***********************************")
preorder(root)
print("***********************************")
inorder(root)