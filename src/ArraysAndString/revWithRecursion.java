package ArraysAndString;

//public class revWithRecursion {

public class revWithRecursion 
{
	public String reverse(String str) 
	{     
		if ((str==null)||(str.length() <= 1) )
			return str;
		return reverse(str.substring(1)) + str.charAt(0);
	}
	public static void main(String[] args) 
	{
		revWithRecursion obj=new revWithRecursion();
		String str = "Preeti";
		System.out.println("Reverse of \'"+str+"\' is \'"+obj.reverse(str)+"\'");    
	}    
}
