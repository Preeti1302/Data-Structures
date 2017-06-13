package ArraysAndString;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedHashSet;

public class removeDuplicate {

	public static void remDup(String str1){
		StringBuffer sb = new StringBuffer();
		LinkedHashSet<Character> hset = new LinkedHashSet<Character>();
		for(int i = 0; i<str1.length() ; i++){
			hset.add(str1.charAt(i));
		}

		for(char ch : hset){
			sb.append(ch);
		}

		System.out.println(sb.toString());
	}

	public static void useArray(String str1){

		ArrayList<String> arrList = new ArrayList<String>();
		StringBuffer sb = new StringBuffer();
		String[] string1 = str1.split("");

		for(int i = 0 ; i<str1.length() ; i++){
			if(!arrList.contains(string1[i])){
				arrList.add(string1[i]);
			}
		}

		for(String ch : arrList){
			sb.append(ch);
		}
		System.out.println(" Other Attempt: " +sb.toString());
	}

	public static void main(String[] args){
		String dups = "eeeefggkkorss";
		remDup(dups);
		useArray(dups);
	}
}
