package ArraysAndString;

import java.util.HashSet;

public class commonOfAll3 {

	public static void findCommon(int[] arr1, int[] arr2, int[] arr3, int m, int n, int o){

		HashSet<Integer> hset1 = new HashSet<Integer>();
		HashSet<Integer> hset2 = new HashSet<Integer>();
		HashSet<Integer> hset3 = new HashSet<Integer>();


		for(int i : arr1){
			hset1.add(i);
		}
		for(int j : arr2){
				if(hset1.contains(j) ){
					hset2.add(j);
				}
			}
		for(int k : arr3){
			if(hset2.contains(k) ){
				hset3.add(k);
			}
		}
		
		
		System.out.println("Common element in all 3 arrays is : " + hset3);


	}
	public static void main(String[] args){

		int arr1[] = {1, 2, 3, 5 ,6, 7 };
		int arr2[] = {3, 6, 7, 8, 20};
		int arr3[] = {3, 17,7, 18, 20};

		int m = arr1.length;
		int n = arr2.length;
		int o = arr3.length;

		findCommon(arr1 , arr2 , arr3, m ,n , o);
	}
}
