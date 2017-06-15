package ArraysAndString;

import java.util.HashMap;

public class isAnaPali {

	public static boolean isAnagram(String str1 , String str2){
		boolean value = false;
		HashMap<Character,Integer> hmap = new HashMap<Character, Integer>();
		for(int i=0 ; i<str1.length() ; i++){
			if(hmap.containsKey(str1.charAt(i))){
				hmap.put(str1.charAt(i), hmap.get(str1.charAt(i))+1);
			}
			else{
				hmap.put(str1.charAt(i), 1);
			}
		}
		for(int i =0 ; i<str2.length();i++){
			if(hmap.containsKey(str2.charAt(i)) && hmap.get(str2.charAt(i))!=0){
				hmap.put(str2.charAt(i), hmap.get(str1.charAt(i))-1);
			}
//			else if(hmap.containsKey(str2.charAt(i)) && hmap.get(str2.charAt(i))==0){
//				hmap.put(str2.charAt(i), 1);
//			}
			else{
				hmap.put(str2.charAt(i), 1);
			}
		}
		for(char ch : hmap.keySet()){
			if(hmap.get(ch)==0){
				value = true;
			}
			else{
				value =false;
			}
		}
		return value;
	}

	public static boolean isPalindrome(String str){

		StringBuffer sb = new StringBuffer();
		String strArray = str.trim();

		char[] charStr = str.toCharArray();
		for(int i = charStr.length-1 ; i>=0 ; i--){
			sb.append(charStr[i]);
		}
//		System.out.println(sb.toString());
//		System.out.println(strArray);
		if(strArray.equalsIgnoreCase(sb.toString())){
			return true;
		}

		return false;
	}

	public static boolean checkBoth(String str){
		// [Rats, live, on, no, evil, star]
		String[] value = str.split(" ");
		//System.out.println(value.toString());
		StringBuffer sb2 = new StringBuffer();
		for(int i=0 ; i<value.length ; i++){
			for(int j=value.length-1 ; j>=0 ; j--){
				if(isAnagram(value[i] , value[j])){
					if(isPalindrome(str)){
						return true;
					}			
				}
			}
		}
		return false;

	}




	public static void main(String[] args){
		String toBeTested= "Rats live on no evil star";
		boolean value = checkBoth(toBeTested);
		if(value){
			System.out.println("String is Anagram of Palindrome !!");
		}
		else{
			System.out.println("Sorry its not what you wanted !!");
		}
	}
}
