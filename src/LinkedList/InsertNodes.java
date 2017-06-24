package LinkedList;
import LinkedList.LinkeListImp;
import LinkedList.LinkeListImp.Node;;
public class InsertNodes {
	static LinkeListImp llist = new LinkeListImp();
	public static void insertAtFront(int n){
		
		Node new_node = new Node(n);
		new_node.next = llist.head;
		llist.head = new_node;
		
	}
	
	public static void insertAfter(Node prevNode , int new_node){
		
		Node newNode = new Node(new_node);
		
		if(prevNode == null){
			System.out.println("Previous Node does not Exist !!");
		}
		else{
			newNode.next = prevNode.next;
			prevNode.next=newNode;
		}
	}
	
	public static void insertAtEnd(int newNode){
		
		Node tempNode = new Node(newNode);
		
		if(llist.head == null){
			llist.head = tempNode;
		}
		
		tempNode.next = null;
		Node last = llist.head;
		while(last.next!=null){
			last = last.next;
		}
		
		last.next = tempNode;
	}
	
	public static void main(String[] args){
		llist.head = new Node(10);
		Node second = new Node(20);
		Node third = new Node(30);
		Node fourth = new Node(40);
		Node fifth = new Node(60);
		
		llist.head.next = second;
		second.next = third;
		third.next = fourth;
		fourth.next = fifth;	
		insertAtEnd(40);
		insertAtEnd(50);
		System.out.println("Original list:");
		llist.printLinkedList();
				
		insertAtFront(1);
		System.out.println("\n After inserting at FRONT :");
		llist.printLinkedList();
		
		insertAfter(fourth , 50);
		System.out.println("\n After after specific NODE :");
		llist.printLinkedList();
		
		insertAtEnd(100);
		System.out.println("\n After at END :");
		llist.printLinkedList();
		
		System.out.println("********************************************************");
		
		insertAtFront(-1);
		System.out.println("\n After inserting at FRONT :");
		llist.printLinkedList();
		
		insertAfter(third , 35);
		System.out.println("\n After after specific NODE :");
		llist.printLinkedList();
		
		insertAtEnd(200);
		System.out.println("\n After at END :");
		llist.printLinkedList();
	}
	
	
}
