package ArraysAndString;

public class isPalindrome {

	public static boolean isPalindromee(String str1){

		int len = str1.length();

		for(int i=0; i<len ; ){
			for(int j=len-1; j>0 ; ){
				if(i!=j){
					if(str1.charAt(i) == str1.charAt(j)){
						i++;
						j--;
					}
					else{
						return false;
					}
				}
				else if(i==j){
					return true;
				}

			}
		}
		return false;
	}

	public static void main(String[] args){
		String str1 = "abcedcba";
		boolean value = isPalindromee(str1);
		System.out.println("Is Palindrome : "+value);
	}


}
