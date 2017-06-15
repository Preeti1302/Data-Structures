package ArraysAndString;

import java.util.ArrayList;

public class evenOdd {

	public static void separateEvenOdd(int[] arr , int m){
		
		ArrayList<Integer> hset = new ArrayList<Integer>();
		ArrayList<Integer> arrayEven = new ArrayList<Integer>();
	    
		for(int i = 0; i<m ; i++){
			if(arr[i]%2 == 0){
				arrayEven.add(arr[i]);
			}
			else{
				hset.add(arr[i]);
			}
		}
		
		for(int i : hset){
			arrayEven.add(i);
		}
		
		System.out.println(arrayEven);
	}
	
	public static void main(String[] args){
		int[] arr1 = {3,5,6,4,7,9,11,32,13};
		int len = arr1.length;
		separateEvenOdd(arr1 , len);
	}
}
