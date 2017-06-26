package LinkedList;
import java.util.LinkedList;
public class findKthElement {

	public static void findElement(LinkedList<Integer> list , int n){
		int size = list.size();
		int findIndex = size - n;
		System.out.println(list.get(findIndex));
	}
		
	
	
	
	public static void main(String[] args){

		LinkedList<Integer> list = new LinkedList<Integer>();
		list.add(10); list.add(20);
		list.add(30); list.add(40);
		list.add(50); list.add(60);
		System.out.println(list);
		System.out.println(list.size());
		int n = 3;
		findElement(list , n);
		
	}

}
