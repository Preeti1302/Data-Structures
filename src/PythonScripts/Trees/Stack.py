class Stack:
    def __init__(self ):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
        
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size (self):
        return len(self.items)
    

newStack = Stack()
newStack.push(10)
newStack.push(20)
newStack.push(30)
newStack.push(40)
newStack.push(50)
newStack.push(60)
print(newStack.peek())
print(newStack.size())
while(newStack.size()>0):
    print(newStack.pop())