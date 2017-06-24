package LinkedList;

public class DeleteNodes {

	static class Node{
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

	public void deleteNode(int n){

		//Node deleteNode = new Node(n);
		Node temp = head , previous = null;
		System.out.println("Head : " + head.data);
		if(temp !=null && temp.data == n){
			head = temp.next;
		}
		
		while(temp != null && temp.data != n){
			System.out.println("Here");
			
			previous = temp;
			temp = temp.next;
		}


		previous.next = temp.next;
	}



	public static void main(String[] args){
		DeleteNodes allStuff = new DeleteNodes();

		/*  All operations : 1. Push , 2. Pop , 3. Search*/

		allStuff.push(10); allStuff.push(20); allStuff.push(30); allStuff.push(40); allStuff.push(50);
		System.out.println("*****Original List*****");
		allStuff.printList();
		allStuff.deleteNode(40);
		System.out.println("*****After deleting 40*****");
		allStuff.printList();
		System.out.println("*****Push some *****");
		allStuff.push(60);
		allStuff.push(70);
		allStuff.push(80);
		System.out.println("*****After new insertion*****");
		allStuff.printList();
		allStuff.deleteNode(70);
		System.out.println("*****After deleting 70*****");
		allStuff.printList();
	}
}
