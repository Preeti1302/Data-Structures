import java.util.Arrays;

public class Removeduplicates {
	public void removeDups(int[] inputarray){
		int length = inputarray.length;
		System.out.println("Length :"+length);
		Arrays.sort(inputarray);
		int[] array2 = new int[length];
		int j = 0;
		
		for(int i = 0 ; i<length-1 ; i++){
			if(inputarray[i] != inputarray[i+1])
				array2[j++] = inputarray[i];
		}
		array2[j++] = inputarray[length-1];

		for(int s=0 ; s<j ; s++){
			inputarray[s] = array2[s];
			System.out.print(inputarray[s]+" ");
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