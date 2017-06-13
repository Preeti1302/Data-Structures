package ArraysAndString;

public class swapWoTemp {

	public void swap(int x, int y){
		x = x^y; //x assigned with XOR value
		y = x^y;
		x = x^y;
		
		System.out.println("After swapping : \'x : \'"  + x + " and \'y : \'" + y );
	}
	
	public void swap1(int x, int y){
		x = x+y; //x assigned with XOR value
		y = x-y;
		x = x-y;
		
		System.out.println("After swapping : \'x : \'"  + x + " and \'y : \'" + y );
	}
	
	public void swap2(int x, int y){
		x = x*y; //x assigned with XOR value
		y = x/y;
		x = x/y;
		
		System.out.println("After swapping : \'x : \'"  + x + " and \'y : \'" + y );
	}
	
	
	public static void main(String[] args){
		
		int x =100 , y = 200, a =300 , b= 400, p =500 , s = 600;
		swapWoTemp sw = new  swapWoTemp();
		sw.swap(x , y);
		sw.swap1(a , b);
		sw.swap1(p , s);
	}
}
