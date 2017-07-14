package ArraysAndString;

import java.util.ArrayList;
import java.util.Scanner;

public class addDigitsNumbers {

	public static void addDigits(int number){
		ArrayList<Integer> remainder = new ArrayList<Integer>();
		while(number!=0){

			//remainder = number%10;
			remainder.add(number%10);
			number = number / 10;
			//sum+=remainder;
		}
		int sum = 0;
		for(int k : remainder){
			sum = sum + k;
		}

		System.out.println("Addition of Integers : " + sum);
	}

	public static void main(String[] args){
		Scanner scaninput = new Scanner(System.in);
		int number = scaninput.nextInt();
		addDigits(number);
	}
}
