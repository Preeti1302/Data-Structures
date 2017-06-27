package LinkedList;
/*DELETE COMPLETE LINKED LIST BY SUBSTITUTING HEAD TO nULL*/
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

	public void deleteList(){
		head  = null;
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

	public void findFromLast(int n){
		
		Node temp = head;
		int len =0;
		
		while(temp != null){
			temp = temp.next;
			len ++;
		}
		System.out.println(len);
		if(len < n){
			System.out.println("LinkedList is small");
		}
		/* RESET TEMP TO HEAD*/
		temp = head;
		for(int i = 1 ; i < len-n +1 ; i++){
			temp = temp.next;
		}
		
		System.out.println(temp.data);
		
	}
	
public int findElementNode(int value){
		
		Node temp = head;
		int length = 0;
		while(temp !=null){
			temp = temp.next;
			length++;
		}
		
		temp=head;
		for(int i=1 ; i <= length ; i++){
			
			if(temp.data == value){
				return i;
			}		
			else{
				temp = temp.next;
			}
		}
		return 0;
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
	//	allStuff.deleteList();
		allStuff.push(60);
		allStuff.push(70);
		allStuff.push(80);
		System.out.println("*****After new insertion*****");
		allStuff.printList();
		allStuff.deleteNode(70);
		System.out.println("*****After deleting 70*****");
		allStuff.printList();
		int k = 3;
		System.out.println("Find kth element");
		allStuff.findFromLast(k);
		
		int index = allStuff.findElementNode(90);
		if(index == 0){
			System.out.println("Element not in list");
		}
		else
			System.out.println("Element found at Index :" +index);
		
	}
}
