class Node:
    def __init__(self,init_data):
        self.data =init_data;
        self.next = None;
        
    def get_data(self):
        return self.data;
    
    def get_next(self):
        return self.next;
    
    def set_data(self, newdata):
        self.data = newdata;
    
    def set_next(self,  newnext):
        self.next = newnext;
##############################################################################        
#    INSERT AT THE HEAD OF LINKED LIST 
class UnOrderedList:    
    
    def __init__(self ):
        self.head = None
    
    def isEmpty(self):
        self.head = None
##############################################################################        
    def insert_at_head(self , value):
        value = Node(value);
        if(self.head != None):
            temp = value;
            temp.set_next(self.head);
            self.head = temp;
            return
        else:
            self.head = value;
            return
    
##############################################################################    
    def insert_at_end(self , value):
        newNode = Node(value);
        last = self.head;
        if(self.head == None):
            self.head = newNode;
            return
        else:
            while(last.get_next()):
                last = last.get_next();
            last.set_next(newNode)             
##############################################################################    
    def insert_at_specific(self, prev_Node, new_Node):
       
        current = self.head
        prevNode = Node(prev_Node)
        if(prevNode == None):
            print("Given previous node is not present");
        while(current.get_data() != prevNode.get_data()):
            current = current.get_next();
        print(current.get_data())   
        if(current.get_data() == prevNode.get_data()):
            prevNode = current;
            newNode = Node(new_Node);
            newNode.set_next(prevNode.get_next());
            prevNode.set_next(newNode);
##############################################################################               
           
    def size(self):
        count = 0;
        currentNode= self.head
        if(currentNode == None):
            count = 0;
        while(currentNode.get_next()):
            count = count + 1;
            currentNode = currentNode.get_next();
        if(currentNode.get_next() == None):
            count = count + 1;
        return count;
##############################################################################    
    def search(self , searchValue):
        currentNode = self.head;
        searchValue = Node(searchValue);
        foundValue = False;
        while(currentNode != None):
            if(currentNode == searchValue):
                foundValue = True;
                print(foundValue);
                return
            else:
                currentNode = currentNode.get_next();
                if(currentNode == searchValue):
                    foundValue = True;
                    print(foundValue);
                    return 
##############################################################################   
    def remove(self,item):
        current = self.head;
        previous = None;
        foundVal = False;
        while not foundVal:
            if(current.get_data() == item):
                foundVal = True;
                print(foundVal);
            else:
                previous = current;
                current = current.get_next();
        if previous == None:
            self.head = current.get_next();
        else:
            previous.set_next(current.get_next());
            
##############################################################################    
    def printList(self):
        temp = self.head;
        while(temp.get_next()):
            print(temp.get_data())
            temp = temp.get_next();
            if(temp.get_next()==None):
                print(temp.get_data());    
            
##############################################################################            
    
if __name__=='__main__':  
      
    myList = UnOrderedList();
    myList.insert_at_head(10);
    myList.insert_at_head(20);
    myList.insert_at_head(30);
    myList.insert_at_head(40);
    myList.insert_at_end(60);
    myList.insert_at_end(70);
    myList.insert_at_specific(30, 35)
    myList.printList()
    count= myList.size();
    print('Count = ' , count);
    myList.remove(40);
    myList.printList();
    
    
    
    