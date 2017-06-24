package ProblemsToNote;

import java.util.HashMap;

class Node {

	int key , value = 0;
	Node prev = null;
	Node next = null;

	public Node (int key , int value){
		this.key = key;
		this.value = value;
	}
}

public class implementLRU {

	int capacity = 0;
	Node head;
	Node end;

	HashMap<Integer , Node> cache = new HashMap<Integer, Node>();

	public implementLRU(int capacity) {
        this.capacity = capacity;
    }
	
	public int get(int key){
		/* FETCH THE KEY AND MAKE SURE THE NODE IS SHIFTED IN FRONT COZ 
		 * IT IS RECENTLY USED*/
		
		if(cache.containsKey(key)){
			Node n = cache.get(key);
			remove(n);
			setHead(n);
			return n.value;
		}
		
		return -1;
	}

	public void remove(Node n){
		/* IF PREVIOUS NODE FOR 'n' EXISTS THEN MAKE SURE THAT NEXT OF PREVIOUS POINTS TO
		 * NEXT OF NODE n*/
		if(n.prev != null){
			n.prev.next = n.next;
		}
		/*ELSE IF THERE IS NO PREVIOUS IT MEANS n WAS HEAD SO MAKE THE NEXT NODE AS HEAD */
		else{
			head = n.next;
		}
		/*NEXT CONDITION TO BE CHECKED IS WHETHER NEXT OF n IS NOT NULL, IF NOT NULL THEN 
		 * PREVIOUS NODE IS POINTED TO NEXT OF n.*/
		if(n.next != null){
			n.next.prev = n.prev;
		}
		/*ELSE IF IT WAS LAST NODE THEN PREVIOUS NODE IS SET TO END*/
		else{
			end = n.prev;
		}


	}
	public void setHead(Node n){

		n.next = head;
		n.prev = null;

		if(head != null){
			head.prev = n;
		}
		head = n;
		
		
		if(end == null){
			end=head;
		}
	}	

	public void set(int key , int value){

		/*IF THE KEY EXISTS IN THE HASHMAP THEN REMOVE THAT NODE FROM ITS PLACE AND THEN 
		 * ADD IN THE FRONT OF THE QUEUE, PURPOSE BEING MAKING IT SURE THAT KEYS AT THE END OF 
		 * DOUBLY LINKED LIST ARE THE ONE'S WHICH ARE LEAST RECENTLY USED.*/ 
		if(cache.containsKey(key)){   
			Node old = cache.get(key);
			old.value = value;
			remove(old);
			setHead(old);
		}

		/* IF HASHMAP DOES NOT CONTAIN THE KEY, THEN WE NEED TO ADD IT. BUT BEFORE THAT CREATE
		 * A NODE AND THEN CHECK IF THE CACHE SIZE IS LESS THAN OR EQUAL TO CAPACITY GIVEN.
		 * IF IT IS LESS THAN OR EQUAL TO THE CAPACITY, THEN REMOVE THE NODES FROM END AND THEN
		 * SET HEAD TO THE NEW ONE CREATED. IF THERE IS NO PROBLEM OF SIZE THEN SET HEAD AND 
		 * ENTER THE PAIR IN THE HASHMAP*/
		else{
			Node created = new Node(key, value);
			if(cache.size() >=capacity){
				cache.remove(end.key);
				remove(end);
				setHead(created);
			}
			else{
				setHead(created);
			}

			cache.put(key, created);
		}


	}

}
