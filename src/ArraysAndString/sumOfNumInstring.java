package ArraysAndString;

public class sumOfNumInstring {

	private static long SumOfNumbers(String str) {
	    int digit = 0, number = 0;
	    long sum = 0;
	    // Iterate through each character in the input string
	    for (int i = 0; i < str.length(); i++) {
	    	
	        // Convert the character to integer
	        digit = Integer.valueOf(str.charAt(i)) - '0';
	        // Check if the character is a integer
	        // add the digits till a non-integer is encountered
	        if (digit >= 0 && digit <= 9) {
	            number = number + digit;
	        } else {
	            sum += number;
	            number = 0;
	        }
	    }
	    sum += number;
	    return sum;
	}
	
	public static void main(String[] args){
		String str = "123abc$-287F";
		long valueSum = SumOfNumbers(str);
		System.out.println("Summation is equal to : " + valueSum);
	}
	
}
