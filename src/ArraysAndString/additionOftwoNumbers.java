package ArraysAndString;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class additionOftwoNumbers {

	public static int[] getsum(int[] nums, int target){
		HashSet<Integer> sumsrr=new HashSet<Integer>();
		int[] res=new int[2];
		for(int i=0;i<nums.length;i++)
		{
		  if(sumsrr.contains(target-nums[i]))
		   {
		   res[1]=nums[i];
		   res[0]=target-nums[i];
		   }
		    else{
		     sumsrr.add(target-nums[i]);
		    }
		}
		return res;
		}

	
	public static void findAddition(int[] inputArr){

		HashMap<Integer,Integer> hmap = new HashMap<Integer,Integer>();
		int size = inputArr.length;
		int sum = 32;
		int diff=0;
		for(int i=0; i<size ; i++){
			diff = sum - inputArr[i];
			if(hmap.containsKey(inputArr[i])){
				hmap.put(inputArr[i],diff);
			}
			else{
				hmap.put(diff, inputArr[i]);
			}
		}
		
		for(int k = 0 ; k<hmap.size() ; k++){
			if(hmap.containsKey(inputArr[k])){
				System.out.println("Numbers that add upto 32 are :" +hmap.get(inputArr[k]) + " and " + inputArr[k]);
			}
		}
		
	}

	public static void main(String args[]){
		int[] inputArray ={23, 12, 27, 15, 18, 7, 9, 10};
		findAddition(inputArray);
		int[] output = getsum(inputArray , 32);
		
		for(int i : output){
			System.out.println("Output from HashSet : "+ output[i]);
			i++;
		}
		
	}
}
