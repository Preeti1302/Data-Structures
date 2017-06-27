package LinkedList;

public class swapNodes {
	class Node
	{
		int data;
		Node next;
		Node(int d)
		{
			data = d;
			next = null;
		}
	}

	Node head; // head of list
	
	/* Function to add Node at beginning of list. */
	public void push(int new_data)
	{
		/* 1. alloc the Node and put the data */
		Node new_Node = new Node(new_data);

		/* 2. Make next of new Node as head */
		new_Node.next = head;

		/* 3. Move the head to point to new Node */
		head = new_Node;
	}

	/* This function prints contents of linked list starting
	       from the given Node */
	public void printList()
	{
		Node tNode = head;
		while (tNode != null)
		{
			System.out.print(tNode.data+" ");
			tNode = tNode.next;
		}
	}


	/* Function to swap Nodes x and y in linked list by
	       changing links */
	public void swapNodesHere(int x , int y){

		Node prevX = null , prevY = null, currentX = head , currentY = head;
		if(x == y){
			System.out.println("Both are similar values, No need to Swap !!");
		}

		while(currentX != null && currentX.data != x){
			prevX = currentX;
			currentX = currentX.next;
		}

		while(currentY != null && currentY.data != y){
			prevY = currentY;
			currentY = currentY.next;
		}
		
		if(prevX !=null){
			prevX.next = currentY;
		}else{
			head = currentY;
		}
		
		if(prevY !=null){
			prevY.next = currentX;
		}else{
			head = currentX;
		}
		
		Node temp = currentX.next;
		currentX.next = currentY.next;
		currentY.next = temp;
	}



	/* Druver program to test above function */
	public static void main(String[] args)
	{
		swapNodes llist = new swapNodes();

		/* The constructed linked list is:
	            1->2->3->4->5->6->7 */
		llist.push(7);
		llist.push(6);
		llist.push(5);
		llist.push(4);
		llist.push(3);
		llist.push(2);
		llist.push(1);

		System.out.print("\n Linked list before calling swapNodes() ");
		llist.printList();

		llist.swapNodesHere(6, 3);

		System.out.print("\n Linked list after calling swapNodes() ");
		llist.printList();
	}
}

