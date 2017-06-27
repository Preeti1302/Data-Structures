package LinkedList;

public class reverseALinkedList {

	 class Node{
		int data;
		Node next;

		public Node (int n){
			this.data = n;
			this.next = null;
		}
	}

	static Node head;

	public void push(int n){
		Node newNode = new Node(n);

		if(head == null){
			head = newNode;
		}
		else{
			Node temp = head;
			while(temp.next != null){
				temp = temp.next;
			}
			if(temp.next == null){
				temp.next = newNode;
			}
		}
	}

	public void printList(){
		Node temp = head;
		while(temp != null){
			System.out.println(temp.data);
			temp = temp.next;
		}		
	}

	public void reverseList(int n){
		Node current , prev = null , next;
		Node node = new Node(n);
		current = head;
		while(current != null){
			next = current.next;
			current.next = prev;
			prev = current;
			current = next;
		}
		
		node = prev;
	
	}
	
	public static void main(String[] args){
		reverseALinkedList allStuff = new reverseALinkedList();

		/*  All operations : 1. Push , 2. Pop , 3. Search*/

		allStuff.push(10); allStuff.push(20); allStuff.push(30); allStuff.push(40); allStuff.push(50);
		System.out.println("*****Original List*****");
		
		allStuff.push(60);
		allStuff.push(70);
		allStuff.push(80);
		allStuff.printList();
		allStuff.reverseList(10);

		System.out.println("*****Reverse List*****");
		allStuff.printList();
	}
}
