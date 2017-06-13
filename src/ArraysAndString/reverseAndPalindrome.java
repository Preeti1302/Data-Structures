package ArraysAndString;

import java.util.Scanner;

public class reverseAndPalindrome {

	/*REVERSE A NUMBER*/

	public static int reverse(int number){
		int reverseNum =0, remainder = 0;
		while(number !=0){
			
			remainder = number % 10;
			reverseNum = reverseNum*10 + remainder;
			number = number/10;
			
		}
		System.out.println(reverseNum);
		return reverseNum;
	}
	
	/* CHECK IF A PALINDROME */
	public static boolean isPalindrome(int number){
		int rev = reverse(number);
		if(number == rev){
			return true;
		}
		else{
			return false;
		}
	}
	
	public static void revAndPalindrom(int number){
		int sum = 0 , rev = 0;
		if(isPalindrome(number)){
			System.out.println("Number already a Palindrome !!!");
		}
		else{			
			rev = reverse(number);
			while(!isPalindrome(number)){
				number = number + rev;
			}
			System.out.println(number);
		}

	}



	public static void main(String[] args){
		Scanner numScan = new Scanner(System.in);
		int num = numScan.nextInt();
		revAndPalindrom(num);
	}

}
