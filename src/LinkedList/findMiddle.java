package LinkedList;

import LinkedList.DeleteNodes.Node;

public class findMiddle {

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
	
	public int findMiddle(){
		
		Node temp = head;
		int len =0;
		while(temp != null)
		{
			temp = temp.next;
			len++;
		}
		//System.out.println(len);
		temp = head;
		int mid = Math.abs((1+len)/2);
		//System.out.println(mid);
		for(int i = 1 ; i <=len ;){
			while(i != mid){
				//System.out.println("I is :" +i + "and Mid :" +mid);
				temp=temp.next;
				 i++;
			}
			//System.out.println(temp.data);
			return temp.data;
		}
		return -1;
	}
	
	
	public int findMiddle1(){
		
		Node slow = head ; Node fast = head;
		
		while(fast.next !=null && fast != null){
			fast = fast.next.next;
			slow = slow.next;
		}
		
		if(slow != null){
			return slow.data;
		}
		return -1;
	}
	
	
	
	public static void main(String[] args){
		findMiddle allStuff = new findMiddle();

		/*  All operations : 1. Push , 2. Pop , 3. Search*/

		allStuff.push(10); allStuff.push(20); allStuff.push(30); allStuff.push(40); allStuff.push(50);
		allStuff.push(60);allStuff.push(70);allStuff.push(80);allStuff.push(90);
		//allStuff.push(160);allStuff.push(170);allStuff.push(180);allStuff.push(190);
		allStuff.printList();
		int mid = allStuff.findMiddle();
		if(mid == -1)
		{
			System.out.println("Something went wrong !!");
		}
		else{
			System.out.println("Middle here is : " + mid);
		}
				
		int mid1 = allStuff.findMiddle1();
		if(mid1 == -1)
		{
			System.out.println("Something went wrong !!");
		}
		else{
			System.out.println("Middle here is : " + mid1);
		}
		
		}
	
	
	
}
