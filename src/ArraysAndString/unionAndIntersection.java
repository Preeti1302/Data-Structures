package ArraysAndString;

import java.util.HashMap;
import java.util.HashSet;

public class unionAndIntersection {

	public static void findUnion(int[] arr1, int[] arr2, int m, int n){
		
		HashSet<Integer> hset = new HashSet<Integer>();
		for(int i : arr1){
			hset.add(i);
		}

		for(int j : arr2){
			if(!hset.contains(j)){
				hset.add(j);
			}
		}

		
			System.out.println("Union of these 2 arrays is : " + hset);
		
	}

	public static void findIntersection(int[] arr1, int[] arr2, int m, int n){
		
		HashSet<Integer> hset = new HashSet<Integer>();
		HashSet<Integer> hset1 = new HashSet<Integer>();
		for(int i : arr1){
			hset.add(i);
		}

		for(int j : arr2){
			if(hset.contains(j)){
				hset1.add(j);
			}
		}

		
			System.out.println("Union of these 2 arrays is : " + hset1);
		

	public static void main(String[] args){
//		int arr1[] = {7, 1, 5, 2, 3, 6};
//		int arr2[] = {3, 8, 6, 20, 7};
		
//		int arr1[] = {1, 5, 2};
//		int arr2[] = {3, 8, 6, 20, 7};
		
		int arr1[] = {1, 2, 3, 5 ,6, 7 };
		int arr2[] = {3, 6, 7, 8, 20};
		
		int m = arr1.length;
		int n = arr2.length;

		findUnion(arr1 , arr2 , m ,n);
		findIntersection(arr1 , arr2 , m ,n);
	}
}
