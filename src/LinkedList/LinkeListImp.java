package LinkedList;

public class LinkeListImp {

	static class Node{
		int data;
		Node next;
		
		public Node(int d){
			this.data = d;
			this.next = null;
		}
	}
	
	
	Node head;
	public void push(int new_data)
    {
        Node new_node = new Node(new_data);
        new_node.next = head;
        head = new_node;
    }
	public void printLinkedList(){
		Node start = head;
		while( start != null){
			System.out.println(" Data here is : " + start.data);
			start = start.next;
		}
	}
	
	public static void main(String[] args){
		LinkeListImp linkedlist = new LinkeListImp();
		
		Node second = new Node(45);
		Node third = new Node(50);
		Node fourth = new Node(42);
		linkedlist.head = new Node(40);
		
		 /* Three nodes have been allocated  dynamically.
        We have refernces to these three blocks as first,  
        second and third

        llist.head        second              third
           |                |                  |
           |                |                  |
       +----+------+     +----+------+     +----+------+
       | 1  | null |     | 2  | null |     |  3 | null |
       +----+------+     +----+------+     +----+------+ */
				
		linkedlist.head.next = second;
		
		 /*  Now next of first Node refers to second.  So they
        both are linked.

     llist.head        second              third
        |                |                  |
        |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  | null |     |  3 | null |
    +----+------+     +----+------+     +----+------+ */
		
		second.next= third;
		second.next = fourth;
		fourth.next = third;
		 /*  Now next of second Node refers to third.  So all three
        nodes are linked.

     llist.head        second              third
        |                |                  |
        |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  |  o-------->|  3 | null |
    +----+------+     +----+------+     +----+------+ */
		
		linkedlist.printLinkedList();
	}
}
