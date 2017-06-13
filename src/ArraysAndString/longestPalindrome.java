package ArraysAndString;

import java.util.HashMap;
import java.util.TreeMap;

import ArraysAndString.*;

public class longestPalindrome {
/*PALINDROME CHECKER*/
	public static boolean issPalindrome(String str){
		
		StringBuffer sb = new StringBuffer();
		for(int i=str.length()-1 ; i >=0 ; i--){
			sb.append(str.charAt(i));
		}
		if(str.equals(sb.toString())){
			System.out.println(sb.toString());
			return true;
		}
		else {
			return false;
		}
		
	}
/*USING HASHMAP : FIND LONGEST PALINDROME*/	
	public static String longPalindrome(String str1){
		
		HashMap<String , Integer> hmap = new HashMap<String, Integer>();
		String[] arrString = str1.split(" ");
		isPalindrome is = new isPalindrome();
		
		int maxLength = 0;
		for(String st : arrString){
			System.out.println(is.isPalindromee(st));
			if(is.isPalindromee(st)){				//isPalindrome(st)){
				hmap.put(st, st.length());
				maxLength = Math.max(maxLength, st.length());
			}
		}
		
		for(String str : hmap.keySet()){
			if(hmap.get(str) == maxLength){
				return str;
			}
		}
		
		
		return null;
		
		
	}
	
	public static void main(String[] args){
		String str= "madam, the board written in malayalam directs you to the third level of the civic center buliding";
		String result = longPalindrome(str);
		System.out.println("The longest Palindrome is : " + result);
	}
	
}
