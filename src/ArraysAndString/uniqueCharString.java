package ArraysAndString;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;

public class uniqueCharString {

	public static void combineToUnique(String str1 , String str2){
		
		HashMap<Character , Integer> hmap = new HashMap<Character, Integer>();
		for(int i = 0 ; i<str1.length() ; i++){
			if(hmap.containsKey(str1.charAt(i))){
				hmap.put(str1.charAt(i), hmap.get(str1.charAt(i))+1);
			}
			else{
				hmap.put(str1.charAt(i), 1);
			}
		}
		
		for(int i = 0 ; i<str2.length() ; i++){
			if(hmap.containsKey(str2.charAt(i))){
				hmap.put(str2.charAt(i), hmap.get(str2.charAt(i))+1);
			}
			else{
				hmap.put(str2.charAt(i), 1);
			}
		}
		StringBuilder sb = new StringBuilder();
		for(char ch : hmap.keySet()){
			if(hmap.get(ch) == 1){
				sb.append(ch);
			}
		}
		System.out.println("Print non-repeating chars from both string as on string using HashMAP : "+sb);
	}
	
	public static void otherTry(String str1 , String str2){
		HashSet<Character> hset = new HashSet<Character>();
		
		for(char ch : str1.toCharArray()){
			hset.add(ch);
		}
		StringBuilder res = new StringBuilder();
		for(char ch1 : str2.toCharArray()){
			if(!hset.contains(ch1)){
				hset.add(ch1);
			}
		}
		for(char ch : hset){
			res.append(ch);
		}
			
			System.out.println("Print all characters once using HashSET : "+res.toString());
	}
	
	public static void main(String[] args){
		String str1 = "abdc23$%123Preeti";
		String str2 = "frged456*7adb43Sharad";
		combineToUnique(str1 , str2);
		otherTry(str1 , str2);
	}
}
