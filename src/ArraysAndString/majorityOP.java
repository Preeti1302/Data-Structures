package ArraysAndString;

import java.util.HashMap;

public class majorityOP {

	public static void findMaxOccured(int[] inpuArray){
		HashMap<Integer , Integer> hmap = new HashMap<Integer, Integer>();
		int max = 0;
		for(int i=0; i<inpuArray.length ; i++){
			if(hmap.containsKey(inpuArray[i])){
				hmap.put(inpuArray[i], hmap.get(inpuArray[i])+1);
			}
			else{
				hmap.put(inpuArray[i], 1);
			}
		}

		for(int k : hmap.keySet()){			
			max = Math.max(max, hmap.get(k));
		}
		for(int k : hmap.keySet()){			
			if(max == hmap.get(k)){
				System.out.println("Maximum occurrance : " + k +" and that is about " + hmap.get(k) + " times.");
			}
		}
	}

	public static void main(String[] args){
		int[] array1 = {3, 3, 4, 2, 4, 4, 2, 4, 4 , 2,2,2,2,2,2,2 };
		findMaxOccured(array1);
	}
}
