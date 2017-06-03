import java.util.Arrays;

public class Removeduplicates {
	public void removeDups(int[] inputarray){
		int length = inputarray.length;
		System.out.println(length);
		Arrays.sort(inputarray);
		int[] array2 = {};
		int j = 0;
		for(int i = 0 ; i<length-1 ; i++){
			System.out.println(inputarray[i+1]);
			if(inputarray[i] == inputarray[i+1]){
				System.out.println("Enterd here");
				array2[j] = inputarray[i];
				
				j++;
			}
			else{
				System.out.println("Enterd else");
				array2[j] = inputarray[i];
				i++;
			}
			array2[j++] = inputarray[length-1];
		}
		
		for(int s =0 ; s<=length-1 ; s++){
			inputarray[s] = array2[s];
			System.out.println(inputarray[s]);
		}
		
	}
}

class mainMethod{
	public static void main(String[] args){
		int[] inputarray = {-6, -12,7,-6, 0, 2,8,3, 3, 6,2};
		Removeduplicates rmd = new Removeduplicates();
		rmd.removeDups(inputarray);
	}
}