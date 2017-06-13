package ArraysAndString;

import java.util.Scanner;

public class printChars {

	
	public static void shortenStirng(String str1){
		
		int len = str1.length();
		char[] Chars = str1.toCharArray();
		StringBuilder sbuilder = new StringBuilder();
		sbuilder.append(Chars[0]);
		int count = 0;
		for(int i=1; i<len-1 ; i++){
			count++;
		}
		sbuilder.append(count);
		sbuilder.append(Chars[len-1]);
		
		System.out.println(sbuilder.toString());
		
	}
	
	public static void main(String[] args){
		Scanner scanInput = new Scanner(System.in);
		String scanIn = scanInput.next();
		
		shortenStirng(scanIn);
	}
}
