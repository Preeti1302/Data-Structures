package ArraysAndString;

import java.util.Scanner;

public class ReverseWords {

	/*****************REVERSE OF A STRING char by char using char array*******************************/ 
	public String stringRev1(String newString){

		int n = newString.length();
		char[] charString = new char[n];
		charString = newString.toCharArray();
		//		for(int j=0 ; j<n ; j++)
		//			System.out.println("this is char string : "+charString[j]);
		String newString1 = "";
		for(int i= n-1 ; i>=0 ; i--){
			newString1 = newString1 + charString[i];
		}

		return newString1;
	}

	/******************REVERSING a string char by char using StringBuffer.******************************/
	public String stringRev2(String newString){
		int m = newString.length();
		String newString2 = "";

		StringBuffer sb = new StringBuffer();
		sb.append(newString);
		sb.reverse();
		newString2 = sb.toString();
		return newString2;
	}

	/******************REVERSING a string char by char inplace using StringBuffer.******************************/
	public String stringRev4(String newString){
		String newString2 = "";
		String[] str = new String[newString.length()];
		str = newString.split(" ");
		String revChar = "";
		StringBuffer sb2 = new StringBuffer();
		for(int i = 0 ; i < str.length; i++){
			int strLen = str.length;
			char[] charString = new char[strLen];
			charString = str[i].toCharArray();
			for(int j = charString.length -1 ; j>=0 ; j--){
				revChar = revChar +charString[j];
			}
			newString2 = newString2 + " " + revChar;
		}
		
		return newString2;
	}

	/******************REVERSING a string word by word using StringBuffer.******************************/
	public String stringRev3(String newString){
		int m = newString.length();
		String newString2 = "";
		String[] str = new String[m];
		str = newString.split(" ");
		int n = str.length;
		//		for(int j=0 ; j<n ; j++)
		//			System.out.println("this is char string : "+str[j]);
		StringBuffer sb = new StringBuffer();
		//sb.append(newString);
		for(int i = n-1 ; i>=0 ; i--){     /*****Reverse using StringBuffer*******/
			sb.append(str[i] + " ");
		}	
		for(int i = n-1 ; i>=0 ; i--){    /******Reverse using string and array******/
			newString2 = newString2 + " " +str[i];
		}	
		//newString2 = sb.toString();
		return newString2;
	}


}


class revString{
	public static void main(String[] args){
		Scanner inputString = new Scanner(System.in);
		String inputStr = inputString.next();
		inputStr += inputString.nextLine();
		//System.out.println(inputStr);
		ReverseWords revW = new ReverseWords();
		/************************************************/
		String outputString = revW.stringRev1(inputStr);
		System.out.println(outputString);
		/************************************************/
		String outputString2 = revW.stringRev2(inputStr);
		System.out.println(outputString2);
		/************************************************/
		String outputString3 = revW.stringRev3(inputStr);
		System.out.println(outputString3);
		/************************************************/
		String outputString4 = revW.stringRev4(inputStr);
		System.out.println(outputString4);
	}
}
